import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="Mirage@123", database="employee_details")

mycursor = mydb.cursor()

mycursor.execute("Select name from employee")

myresult = mycursor.fetchone()

for row in myresult:
    print(row)

