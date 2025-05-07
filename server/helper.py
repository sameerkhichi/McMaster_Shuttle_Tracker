#file to calculate eta and nearest stop given the lat and lon
#in form of lat,lon
musc = [43.2632, -79.9169] # +- 3m
lot_I = [43.26, -79.9217] # +- 4m
abb = [43.26, -79.9219] # +- 3m
lot_P = [43.2639, -79.9281] # +- 4m
keyes = [43.2631, -79.9231] # +- 4m
lot_M = [43.2632, -79.9286] # +- 3m
lot_M_inside = [43.2615, -79.9314] # +- 3m


#returns the closest stop - on frontend it will display it as there or as 'next stop'
def find_stop(lat, lon):

    if lat == musc[0] and lon == musc[1]:
        stop = "MUSC"

    if lat == abb[0] and lon == abb[1]:
        stop = "A.B.B"
    
    if lat == keyes[0] and lon == keyes[1]:
        stop = "Mary Keyes"
    
    if lat == lot_P[0] and lon == lot_P[1]:
        stop = "Lot P"
    
    if lat == lot_M[0] and lon == lot_M[1]:
        stop = "Lot M"
    
    if lat == lot_M_inside[0] and lon == lot_M_inside[1]:
        stop = "Inside Lot M"
    
    if lat == lot_I[0] and lon == lot_I[1]:
        stop = "Lot I"
    
    return stop

def get_eta(lat, lon, time, stop):


    return eta