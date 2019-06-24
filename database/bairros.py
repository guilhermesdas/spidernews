from geopy.geocoders import Nominatim
import json
import time

with open("neighborhood", "r") as file:
    lines = [line.rstrip('\n') for line in file]

for line in lines:
    geolocator = Nominatim()
    location = geolocator.geocode("Manaus",line)
    js = { "neighborhood": line, "lat": location.latitude, "long": location.longitude }
    print(js)
    time.sleep(2)