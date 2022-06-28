import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="Mirage@123", database="employee_details")

mycursor = mydb.cursor()

sql = "DELETE FROM employee Where name='nitu'"

mycursor.execute(sql)

mydb.commit()