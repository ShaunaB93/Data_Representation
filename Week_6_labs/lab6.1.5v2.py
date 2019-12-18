# Shauna Byrne
# Code adapted from Lab instructions from Lab06 given by Andrew Beatty - GMIT - Computing & Data Analytics 2019
# Create a spread sheet that gets all the users that are following me (datarepresentationcourseware) and outputs the users login and repos URL to a spreadsheet.

import requests, json 
from xlwt import *

#url = "https://api.github.com/users?since=100"
url = "https://api.github.com/users/andrewbeattycourseware/followers"
response = requests.get(url)
data = response.json()
#print(data)

#Get the file name for the new file to write
filename = 'githubusers.json'
with open(filename, 'w') as f:
    json.dump(data, f, indent=4)


filename2 = 'users.xls'
with open(filename2, 'w') as fp:
    w = Workbook()
    ws = w.add_sheet('githubUsers')
    row = 0
    f = open('githubusers.json')
    for u in f:
        L = u.strip().split()
        for login, repos_url in enumerate(L):
            ws.write(row, {'Login': f['login'], 'Repo_URL': f['repos_url']})
            row += 1
w.save('users2.xls')  
fp.close()     

