# Shauna Byrne
# Code adapted from Lab instructions from Lab07 given by Andrew Beatty - GMIT - Computing & Data Analytics 2019
# Report List

import requests
import json
from xlwt import *

#url = "https://reports.sem-o.com/api/v1/documents/static-reports"
url= "https://reports.sem-o.com/api/v1/documents/static-reports?ReportName=Balancing%20and%20Imbalance%20Market%20Cost%20View&Date=>2019-11-08"
response = requests.get(url)
data = response.json()

totalPages = data["pagination"]["totalPages"]

listOfReports = []
# Output data to console
for item in data["items"]:
    listOfReports.append(item["ResourceName"])

pageNumber=1
while pageNumber <= totalPages:
    pageUrl = url + "&page="+ str(pageNumber)
    data = requests.get(pageUrl).json()
    for item in data["items"]:
        listOfReports.append(item["ResourceName"])

    pageNumber +=1

w = Workbook()
ws = w.add_sheet("items")
rowNumber = 0;
ws.write(rowNumber,0,"StartTime")
ws.write(rowNumber,1,"EndTime")
ws.write(rowNumber,2,"ImbalanceVolume")
ws.write(rowNumber,3,"ImbalancePrice")
ws.write(rowNumber,4,"ImbalanceCost")
rowNumber += 1 

for ReportName in listOfReports:
    url ="https://reports.sem-o.com/api/v1/documents/"+ReportName
    #print(url)
    response= requests.get(url)
    aReport= response.json()
    for row in aReport["rows"]:
        #print (row)
        ws.write(rowNumber,0,row["StartTime"])
        ws.write(rowNumber,1,row["EndTime"])
        if "ImbalanceVolume" in row:
            ws.write(rowNumber,2,row["ImbalanceVolume"])
        if "ImbalancePrice" in row:
            ws.write(rowNumber,3,row["ImbalancePrice"])
        if "ImbalanceCost" in row:
            ws.write(rowNumber,4,row["ImbalanceCost"])
        rowNumber += 1

# Saves data to a file
#filename = 'reports2.json'
#f =  open(filename, 'w')
#json.dump(data, f, indent=4)

w.save('final.xls')
