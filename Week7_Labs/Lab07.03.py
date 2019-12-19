# Shauna Byrne
# Code adapted from Lab instructions from Lab07.3 given by Andrew Beatty - GMIT - Computing & Data Analytics 2019
# Pulls pressure from live weather URL

import requests
import json

url = "https://prodapi.metweb.ie/observations/newport-furnace/today"
response = requests.get(url)
data = response.json()

for event in data:
    print(event["pressure"])

#filename = 'weather.json'
#f = open(filename, 'w')
#json.dump(data,  f, indent=4)