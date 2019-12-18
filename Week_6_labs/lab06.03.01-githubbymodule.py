# Shauna Byrne
# Code adapted from Lab instructions from Lab06.2 given by Andrew Beatty - GMIT - Computing & Data Analytics 2019

from github import Github

# remove the minus sign from the key
g = Github("b55d312da577ba479f7dc4f8f3f5b1384bdf3b2--e")

repo = g.get_repo("datarepresentationstudent/aPrivateOne")
#print(repo.clone_url)

fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
#print (urlOfFile)

response = requests.get(urlOfFile)
contentOfFile = response.text
#print (contentOfFile)

newContents = contentOfFile + " more stuff \n"
print (newContents)

gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",newContents,fileInfo.sha)
print (gitHubResponse)
