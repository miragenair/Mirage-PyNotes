class Employees:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"the name is {self.name}. the salary is {self.salary}. and the role of the employee is {self.role}."

    @classmethod
    def changeleaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def change_str(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printname(string):
        print("this is a goof boy whose name is " + string)

harry = Employees("Harry", 45000, "Instructor")
rohan = Employees("Rohan", 45321, "HR")
aditya = Employees.change_str("Aditya-000001-bhadwa")

print(aditya.role)
aditya.printname("mirage")

# -------------------------------------------NOTES----------------------------------------------------------------------
'''

    ye same cheese hum self method se bhi kar sakte the lekin fir faltu me self arguement pass hoga and program ka excution time badh jaayega
    thats why we use static function so that we dont use useless arguements
    milliseconds of code matter when it comes to game development because it all can lead to lag   
'''