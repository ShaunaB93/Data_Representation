# Shauna Byrne
# Code adapted from Lab instructions from Lab06 given by Andrew Beatty - GMIT - Computing & Data Analytics 2019
# Write a python program that updates a car on the server using the API

import requests
import json

dataString = {'make':'Ford','model':'Kuga'}
url = 'http://127.0.0.1:5000/cars/test'

response = requests.put(url, json=dataString)

print (response.status_code)
print (response.text)
