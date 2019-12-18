# Shauna Byrne
# Code adapted from Lab instructions from Lab06.2 given by Andrew Beatty - GMIT - Computing & Data Analytics 2019
# Write a python program that will read in a html page from a file and prints it out again 

import requests
import json

#html = '<h1>hello world</h1>This is html'
f = open("../../carviewer.html", "r")
html = f.read()
#print (html)

#Remove = before proceeding
apiKey = '46ceed910c24ff7cce8240e89ec7b71912f6f40f2ec55fd217ce150ad6d4f1c=4'
url = 'https://api.html2pdf.app/v1/generate'

data = {'html': html,'apiKey': apiKey}
response = requests.post(url, json=data)
print (response.status_code)

newFile = open("lab06.02.01.htmlaspdf.pdf", "wb")
newFile.write(response.content)
