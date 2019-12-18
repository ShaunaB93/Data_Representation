# Shauna Byrne
# Code adapted from Lab instructions from Lab06 given by Andrew Beatty - GMIT - Computing & Data Analytics 2019

import requests
import json
from xlwt import *

url = "http://127.0.0.1:5000/cars"

response = requests.get(url)
data = response.json()

#output to the console
print(data)

#output cars individually to the screen
for car in data["cars"]:
    print(car)

#save to a file
filename = 'cars.json'
if filename:
    #Write JSON
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

#excel write
w = Workbook()
ws = w.add_sheet('cars')
row = 0
ws.write(row,0,"reg")
ws.write(row,1,"make")
ws.write(row,2,"model")
ws.write(row,3,"price")
row += 1 
for car in data["cars"]:
    ws.write(row,0, car["reg"])
    ws.write(row,1,car["make"])
    ws.write(row,2,car["model"])
    ws.write(row,3,car["price"])
    row += 1
w.save('cars.xls')
