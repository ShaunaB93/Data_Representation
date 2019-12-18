# Shauna Byrne
# Code adapted from Lab instructions from Lab06.2 given by Andrew Beatty - GMIT - Computing & Data Analytics 2019
# Write a script that will make a change to the datarepresentationstudent git account

from github import Github

# remove the minus sign
gitT = Github("eb593f066ef0b1d2c797b5fc0cd4b27afa139b8--f")


repo = gitT.get_repo("datarepresentationstudent/aPrivateOne")

contents = repo.get_contents("shaunaTest.txt", ref="Shauna_Test")
repo.delete_file(contents.path, "remove test", contents.sha, branch="test")