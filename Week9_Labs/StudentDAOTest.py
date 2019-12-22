from StudentDAO import StudentDAO

#create
latestid = StudentDAO.create('mark', 45)
# find by id
result = StudentDAO.findByID(latestid);
print(result)

#update
StudentDAO.update(('Fred',21,latestid))
result = StudentDAO.findByID(latestid);
print(result)

# get all 
allStudents = StudentDAO.getAll()
for student in allStudents:
  print(student)

# delete
StudentDAO.delete(latestid)

