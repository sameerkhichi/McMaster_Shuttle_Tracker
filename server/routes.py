#note that these routes arent designed for http theyre just api endpoints which work from terminal and react frontend
#there could be unexpected request formats, react and curl work fine so it shouldnt be a problem
#just dont try accessing the api endpoints through a raw browser
from flask import Flask, request, Blueprint, jsonify, make_response, send_from_directory, current_app
from server.models import db, BusLocation
from datetime import datetime, timedelta, timezone
from server import helper

#blueprints for the routes
app_routes = Blueprint('app_routes', __name__)

#base url root - we dont have an html root, the flask server is just for api endpoints
#this route and function serves the react app through the flask server so I can host them together rather than seperately 
@app_routes.route('/')
def home():

    return send_from_directory(current_app.static_folder, "index.html")

@app_routes.route("/<path:path>")
def catch_all(path):
    return send_from_directory(current_app.static_folder, "index.html")

@app_routes.route('/update', methods=['GET'])
def get_bus_locations():

    #get all the bus location records from the database
    locations = BusLocation.query.all()
    bus_data = []

    isRunningDict = helper.getBusRunningDict(locations)
    
    for loc in locations:
        bus_data.append({
            "bus_id": loc.bus_id,
            "nearest_stop": loc.nearest_stop,
            "previous_stop": loc.previous_stop,
            "next_stop": loc.next_stop,
            "eta": loc.eta,
            "time_stamp": loc.time_stamp,
            "isRunning": isRunningDict.get(loc.bus_id, False) #defaults to false
        })
    

    #This stops different versioning of http headers
    response = make_response(jsonify(bus_data), 200)
    response.headers["Content-Type"] = "application/json"
    response.headers["Cache-Control"] = "no-cache"
    return response

#to send a location manually hit the share then the send location now button
#MAKE SURE OWNTRACKS IS ON MOVE MODE SO YOU GET CONSTANT UPDATES set monitoring = 2 (check owntracks settings below)
#in move mode new location as soon as the device moves locatorDisplacement meters or after locatorInterval seconds
@app_routes.route('/Live_Location', methods=['POST'])
#this functions will get the live location, then use it for the calculations
def receive_gpsdata():
    
    data = request.json #owntracks sends json data
    update_prev_loc = True

    #this is basically checking and making sure the data being sent to the server is an actual location
    #making sure the data sent is of type location cuz owntracks can be a little silly
    if data.get("_type") != "location":
        return jsonify({"error": "No location data received"}), 400

    #extracting the relevant data - make sure this isnt a tuple
    bus_id = data.get("tid", "unknown")
    latitude = data.get("lat")
    longitude = data.get("lon")
    timestamp = data.get("tst")  #'tst' is the timestamp field in OwnTracks

    if latitude is None or longitude is None or timestamp is None:
        return jsonify({"error": "Missing required fields"}), 400

    #owntracks sends tst time stamps in UNIX format whereas mysql expects DATETIME type YYYY-MM-DD HH:MM:SS
    timestamp = datetime.utcfromtimestamp(timestamp) #universal time - converted to local timezone on frontend

    #inserting the new location - if the bus_id already exists then just update its location
    #Have to use mysql command: ALTER TABLE bus_locations ADD CONSTRAINT unique_bus UNIQUE (bus_id);
    existing_location = BusLocation.query.filter_by(bus_id=bus_id).first() #returns first matching record

    if existing_location:
        previous_stop = existing_location.previous_stop
    else:
        previous_stop = None  #No previous stop if new bus

    nearest_stop = helper.find_stop(latitude, longitude, previous_stop)
    if existing_location:
        next_info = helper.get_eta(latitude, longitude, nearest_stop, previous_stop)
        eta = next_info[0]
        next_stop = next_info[1]
        if next_info[2]:
            existing_location.previous_stop = next_info[2]

    if existing_location:
        #keeps track of the previous stop - if different from one stored in db
        if nearest_stop != existing_location.nearest_stop or nearest_stop is None:
            
            existing_location.nearest_stop = nearest_stop

            if existing_location.nearest_stop: #dont update the previous stop is the bus is still in transit
                
                #if the bus is newly active - avoid updating previous location till its at a stop
                if existing_location.previous_stop == "N/A" and nearest_stop is None:
                    update_prev_loc = False
                
                #if newly active but at a stop - this forces system to use newly calculated stop rather than the one in the database
                if existing_location.previous_stop == "N/A" and nearest_stop is not None:
                    existing_location.previous_stop = nearest_stop
                    update_prev_loc = False
                
                #otherwise just update like normal
                if update_prev_loc:
                    existing_location.previous_stop = existing_location.nearest_stop
                #runs the calculation again for the next stop info when previous stop is updated
                next_info = helper.get_eta(latitude, longitude, nearest_stop, existing_location.previous_stop)
                eta = next_info[0]
                next_stop = next_info[1]
                if next_info[2]:
                    existing_location.previous_stop = next_info[2]

            existing_location.next_stop = next_stop
        
        #note no need to update stop if its the same one as in the db currently
        existing_location.eta = eta
        existing_location.time_stamp = timestamp
    else:
        new_location = BusLocation(bus_id=bus_id, nearest_stop=nearest_stop, previous_stop="N/A", next_stop=None, eta=None, time_stamp=timestamp) 
        db.session.add(new_location)
    
    try:
        db.session.commit()
        return jsonify({"message": "Location updated"}), 200
    except Exception as e:
        current_app.logger.error(f"Commit failed: {e}")
        db.session.rollback()
        return jsonify({"error": "Database commit failed."}), 500