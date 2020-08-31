import json
import requests

lat = "36.1427"
long = "-86.8065"

r = requests.get(f"https://api.weather.gov/points/{lat},{long}")
json_data = json.loads(r.text)

w = requests.get(f"https://api.weather.gov/gridpoints/{json_data['properties']['cwa']}/{json_data['properties']['gridX']},{json_data['properties']['gridY']}")
weather = json.loads(w.text)

print(weather)
