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

class Programmer(Employees):
    no_of_holidays = 56
    def __init__(self, aname, asalary, arole, alanguages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = alanguages

    def printprog(self):
        return f"the prograammer's name is {self.name}. the salary is {self.salary}. and the role of the employee is {self.role}. and the languages that the programmer knows is {self.languages}"

harry = Employees("Harry", 45000, "Instructor")
rohan = Employees("Rohan", 45321, "HR")
karnik = Programmer("Karnik", 99999, "GameDeveloper", ["python"])
shishir = Programmer("Shishir", 10101, "Programmer", ["python"])
aditya = Employees.change_str("Aditya-000001-bhadwa")

print(aditya.role)
aditya.printname("mirage")
print(karnik.printprog())
print(karnik.no_of_holidays)

# -------------------------------------------NOTES----------------------------------------------------------------------
'''
     this OOPS tut was about inheritance
'''