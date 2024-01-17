import mysql.connector

cnx = mysql.connector.connect(user="root", password="123", host="localhost")


mycursor = cnx.cursor()
mycursor.execute("create database mydatabase")
#cnx.close()