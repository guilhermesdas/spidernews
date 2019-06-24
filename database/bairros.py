import json

with open("bairros", "r") as json_file:
    data = json.load(json_file)

print(data["hits"][0]["_geoloc"])