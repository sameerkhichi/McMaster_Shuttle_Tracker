import requests
import time
from datetime import datetime

#Backend endpoint
BACKEND_URL = "http://localhost:5000/Live_Location"


bus_id = "1"


# Format: (lat, lon)
#these coordinates use the outside path not the internal bus route - but it should still function the same way.
coordinates = [
    (43.262939, -79.917004), #musc stop
    (43.262380, -79.916465), #at the stop sign off sterlin and forsyth
    (43.260092, -79.919821), # just before abb
    (43.260084, -79.922038), #abb stop first pass
    (43.261425, -79.923175), #just before keyes infront of the go station
    (43.263105, -79.923193), #at the keyes residence
    (43.263251, -79.925599), #jsut after the bridge on westaway before the turn to highway 8
    (43.263051, -79.928492), #after the turn towards lot p right infront of lot m (trying to see if it will ignore lot m since its not in order)
    (43.264045, -79.928248), # at lot p
    (43.263543, -79.928414), #between lot p and lot m
    (43.262920, -79.928551), #at lot m (top)
    (43.262297, -79.929667), #moving from lot m to inside lot m
    (43.261534, -79.931202), #at lot m inside
    (43.262522, -79.928549),#stop sign right out of lot m
    (43.263014, -79.923240), #on the way to lot I right infront of keyes
    (43.259944, -79.921782), #at lot I
    (43.259771, -79.919048), #on university avenue right next to the psych building 
    (43.259365, -79.915859), #forsyth and arnold
    (43.262660, -79.916117),#on stearn dr right after the crosswalk near the stop sign after the sharp turn
    (43.263131, -79.916975) #at the musc stop having completed a full cycle.
]

for lat, lon in coordinates:
    timestamp = int(time.time())

    payload = {
        "_type": "location",  
        "tid": bus_id,
        "lat": lat,
        "lon": lon,
        "tst": timestamp
    }

    try:
        response = requests.post(BACKEND_URL, json=payload)
        print(f"Sent: {lat}, {lon} at {timestamp} | Status: {response.status_code}")
        print("Response:", response.json())
    except Exception as e:
        print("Error sending request:", e)

    time.sleep(10)  #delay of 10 seconds to give time for calculation 
