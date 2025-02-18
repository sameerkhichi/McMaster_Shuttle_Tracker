from flask import Flask, request, Blueprint, jsonify, redirect, url_for, render_template
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
            "timestamp": loc.timestamp
        })
    
    return jsonify(bus_data), 200

@app_routes.route('/test', methods=['GET'])
def test():
    return jsonify({'message': 'testing endpoint'})

#base url root
@app_routes.route('/')
def web_interface():

    locations = BusLocation.query.all()

    return render_template('placeholder', locations) #replace placeholder with the JS file for frontend

