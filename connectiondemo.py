import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="Mirage@123")

mycursor = mydb.cursor()

mycursor.execute("show databases")

for db in mycursor:
    print(db)
