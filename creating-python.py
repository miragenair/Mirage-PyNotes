import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="Mirage@123", database="employee_details")

mycursor = mydb.cursor()

mycursor.execute("show tables")

for tb in mycursor:
    print(tb)
