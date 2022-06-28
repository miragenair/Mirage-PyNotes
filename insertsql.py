import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="Mirage@123", database="employee_details")

mycursor = mydb.cursor()

sqlform = "Insert Into employee(name,sal) values(%s,%s)"

employees = [("mirage", 200),("aditya", 200), ("nitu", 400), ]

mycursor.executemany(sqlform, employees)

mydb.commit()