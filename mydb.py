import mysql.connector

dataBase= mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    passwd= 'pass'
)

#prepare cursor object
cursorObject= dataBase.cursor()

#create database
cursorObject.execute("CREATE DATABASE trunk")

print("DONE")