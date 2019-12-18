# Shauna Byrne
# Code adapted from Lab instructions from Lab06.2 given by Andrew Beatty - GMIT - Computing & Data Analytics 2019
# Write a script to get information from your repository 

import requests
import json

# remove the minus sign
apiKey = '778c2e5453c46de2cbbd4589ceb73d45791331--6d'
url = 'https://github.com/ShaunaB93'
filename ="repo2.json"

response = requests.get(url, auth=('token',apiKey))

repoJSON = response.json()
#print (response.json())

file = open(filename, 'w')
json.dump(repoJSON, file, indent=4)