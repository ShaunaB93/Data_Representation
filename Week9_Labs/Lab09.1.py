# Create a database called datarepresentation using a python script
import mysql.connector

mydb = mysql.connector.connect(
  host='127.0.0.1',
  user='root',
  password='root'
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE datarepresentation ")

mydb.close()