import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="Mirage@123", database="employee_details")

mycursor = mydb.cursor()

sql = "UPDATE employee SET sal=7000 where name='mirage'"

mycursor.execute(sql)

mydb.commit()