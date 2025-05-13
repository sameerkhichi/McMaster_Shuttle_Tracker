import math

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
    "ABB": ["MUSC"], #if previous stop was musc choose ABB
    "Lot_I": ["Lot M", "Inside Lot M"] #either one could come before lot I
}


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
        if distance <= threshold:
            candidates.append((stop_name, distance))
            if distance < closest_distance:
                closest_stop = stop_name
                closest_distance = distance

    if len(candidates) > 1 and prev_stop:
        #failsafe to check and differentiate between lot I and ABB
        for stop_name, _ in candidates:
            expected_prev = STOP_ORDER.get(stop_name, [])
            if expected_prev == prev_stop:
                return stop_name

    return closest_stop #none if not within threshold

def get_eta(lat, lon, time, stop):





    return eta