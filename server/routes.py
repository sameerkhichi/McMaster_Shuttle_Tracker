#note that these routes arent designed for http theyre just api endpoints which work from terminal and react frontend
#there could be unexpected request formats, react and curl work fine so it shouldnt be a problem
#just dont try accessing the api endpoints through a raw browser
from flask import Flask, request, Blueprint, jsonify, make_response
from models import db, BusLocation

#blueprints for the routes
app_routes = Blueprint('app_routes', __name__)

@app_routes.route('/bus-locations', methods=['GET'])
def get_bus_locations():

    #get all the bus location records from the database
    locations = BusLocation.query.all()
    bus_data = []

    for loc in locations:
        bus_data.append({
            "bus_id": loc.bus_id,
            "lat": loc.latitude,
            "lon": loc.longitude,
            "time_stamp": loc.time_stamp
        })
    
    #I tried adding this so that it would stop throwing an error when accessing it (it didnt)
    #but this does stop different versioning of http headers
    response = make_response(jsonify(bus_data), 200)
    response.headers["Content-Type"] = "application/json"
    response.headers["Cache-Control"] = "no-cache"
    return response

#base url root - we dont have an html root, the flask server is just for api endpoints
@app_routes.route('/')
def web_interface():

    return "Flask server is running, use this server for API endpoint calls"

