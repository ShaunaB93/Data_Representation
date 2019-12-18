# Shauna Byrne
# Code adapted from Lab instructions from Lab06.2 given by Andrew Beatty - GMIT - Computing & Data Analytics 2019
# Write python script that will get the information from a private repository 

import requests
import json

# remove the minus sign
apiKey = 'b55d312da577ba479f7dc4f8f3f5b1384bdf3b2-e'
url = 'https://api.github.com/repos/datarepresentationstudent/aPrivateOne'
filename ="repo.json"

response = requests.get(url, auth=('token',apiKey))

repoJSON = response.json()
#print (response.json())

file = open(filename, 'w')
json.dump(repoJSON, file, indent=4)
