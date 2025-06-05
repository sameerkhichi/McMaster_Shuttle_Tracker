import math
from datetime import datetime, timedelta, timezone

#file to calculate eta and nearest stop given the lat and lon
#in form of lat,lon
stops = {
    "MUSC": [43.2632, -79.9169], # +- 3m
    "A.B.B": [43.26, -79.9219], # +- 3m
    "Mary Keyes": [43.2631, -79.9231], # +- 4m
    "Lot P": [43.2639, -79.9281], # +- 4m
    "Lot M": [43.2632, -79.9286], # +- 3m
    "Inside Lot M": [43.2615, -79.9314], # +- 3m
    "Lot I": [43.26, -79.9217] # +- 4m
}

#if there are ever more pairs that are close together add the order logic here
STOP_ORDER = {
    "A.B.B": ["MUSC"], #if previous stop was musc choose ABB
    "Lot I": ["Lot M", "Inside Lot M"], #either one could come before lot I
    "MUSC": ["Lot I"],
    "Mary Keyes": ["A.B.B"],
    "Lot P": ["Mary Keyes"],
    "Lot M": ["Lot P"]
}

#duration of trip between stops - hardcoded for now - time in minutes
STOP_TIMES = {
    ("MUSC", "A.B.B"): 6,
    ("A.B.B", "Mary Keyes"): 2,
    ("Mary Keyes", "Lot P"): 2,
    ("Lot P", "Lot M"): 2,
    ("Lot M", "Lot I"): 4,
    ("Lot I", "MUSC"): 6 
}

#returns a list of valid next stops given a previous one
def get_valid_next_stops(prev_stop):
    return [stop for stop, allowed_prev in STOP_ORDER.items() if prev_stop in allowed_prev]


#calculates the threshold - for proximity location - returns distance in meters from coordinates
def get_distance(lat1, lon1, lat2, lon2):
    #Earth radius in meters
    R = 6378137
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = (math.sin(delta_phi/2) ** 2 +
         math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda/2) ** 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c  #distance in meters

#returns the closest stop - on frontend it will display it as there or as 'next stop'
def find_stop(lat, lon, prev_stop, threshold = 30): #proximity of 30m

    closest_stop = None
    closest_distance = float('inf')
    candidates = []

    for stop_name, (stop_lat, stop_lon) in stops.items():
        distance = get_distance(lat, lon, stop_lat, stop_lon)
        print(f"[DEBUG] distance from current location to any of the stops: {distance}")
        if distance <= threshold:
            candidates.append((stop_name, distance))
            if distance < closest_distance:
                closest_stop = stop_name
                closest_distance = distance

    #if there is more than one stop in proximity
    if len(candidates) > 1 and prev_stop:
        #failsafe to check and differentiate between lot I and ABB
        for stop_name, _ in candidates:
            expected_prev = STOP_ORDER.get(stop_name, [])
            if expected_prev == prev_stop:
                closest_stop = stop_name

    expected_stop = get_valid_next_stops(prev_stop)

    #combines inner and outter lot M - remove when accounting for this
    if closest_stop == "Inside Lot M":
        closest_stop = "Lot M"

    print(closest_stop)
    print(expected_stop)

    for items in expected_stop:
        if items != closest_stop:
            closest_stop = None

    print(closest_stop)
    
    return closest_stop #none if not within threshold

#this for now will be hard-coded - later you could add the prediction logic
#returns [eta in minutes, next stop]
def get_eta(lat, lon, stop, prev_stop): # stop is the current stop - none if not at one

    next_stop = None
    eta = [None, None]

    #if currently at stop return travel time to next stop
    if stop is not None:

        #gets the next stop based on the current stop
        for candidate_stop, prev_list in STOP_ORDER.items():
            if stop in prev_list:
                next_stop = candidate_stop
                break
        
        if next_stop:
            eta[0] = STOP_TIMES.get((stop, next_stop))
            eta[1] = next_stop
            if eta is not None:
                return eta
        else:
            return -1, None #incase of error

    #find next stop and estimate time till next stop
    if stop is None and prev_stop is not None:
        #gets the next stop based on the previous stop
        
        #if its the first time its seeing the bus it should set the previous stop before blowing up - this dumb thing ruined me
        if prev_stop == "N/A":
            if stop is not None:
                prev_stop = stop
            else:
                prev_stop = "Lot P" #Assuming busses start inside lot M their first stop should be lot P

        print(f"[DEBUG] prev_stop passed into get_eta: {prev_stop}")
        for candidate_stop, prev_list in STOP_ORDER.items():
            if prev_stop in prev_list:
                print(f"[DEBUG] next stop being set to: {candidate_stop}")
                next_stop = candidate_stop
                break

        #checking to make sure the next stop was actually found
        if next_stop and next_stop in stops:
            stop_lat, stop_lon = stops[next_stop]
            distance = get_distance(lat, lon, stop_lat, stop_lon)

            print(f"[DEBUG] checking distance calculated: {distance}")
            #assuming average speed through campus of 10 km/h
            time = (distance / 2.77778) / 60  #time in minutes
            print(f"[DEBUG] checking the time calculated: {time}")
            eta[0] = math.ceil(time)
            eta[1] = next_stop
            return eta
        else:
            return -1, None #error occurred

#Function that returns a dictionary of {bus_id: isRunning-true/false}
def getBusRunningDict(locations):
    now = datetime.now()  #naive datetime (still universal time)
    running_dictionary = {}

    for loc in locations:
        originalTimeStamp = loc.time_stamp - timedelta(hours=4) #you need this otherwise loc.timetamp is 4 hours ahead - this ruined me
        is_running = (now - originalTimeStamp) <= timedelta(minutes=10)

        if loc.eta >= 30: #failsafe incase tracker is on and out of range of campus (reasoning on backend notes)
            is_running = False

        running_dictionary[loc.bus_id] = is_running

    return running_dictionary