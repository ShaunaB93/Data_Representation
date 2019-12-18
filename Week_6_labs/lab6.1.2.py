# Shauna Byrne
# Code adapted from Lab instructions from Lab06 given by Andrew Beatty - GMIT - Computing & Data Analytics 2019
# Write a python program that creates a car on the server by using the API

import requests
import json

dataString = {'reg':'08 C 1234','make':'Ford','model':'Galaxy','price':12324}
url = 'http://127.0.0.1:5000/cars'

response = requests.post(url, json=dataString)

print (response.status_code)
