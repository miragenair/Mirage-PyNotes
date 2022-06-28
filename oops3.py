class Employees:
    no_of_leaves = 8
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    # def printdetails(self):
    #     return f"the name is {self.name}. the salary is {self.salary}. and the role of the employee is {self.role}."

harry = Employees("Harry",45000,"Instructor")
# Harry.name = "Harry"
# Harry.salary = 45000
# Harry.role = "Instructor"

# Rohan = Employees()
# Rohan.name = "Rohan"
# Rohan.salary = 45321
# Rohan.role = "HR"

print(harry.name)