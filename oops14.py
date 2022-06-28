class Employees:
    no_of_leaves = 8
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"the name is {self.name}. the salary is {self.salary}. and the role of the employee is {self.role}."

    @classmethod
    def changeleaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary/other.salary
        pass

    def __repr__(self):
        return f"the name is {self.name}. the salary is {self.salary}. and the role of the employee is {self.role}."



emp1 = Employees("harry",213,"programmer")
emp2: Employees = Employees("rohan",23,"cleaner")
print(emp1)





# -----------------------------------------------NOTES------------------------------------------------------------------
'''

                                                SPECIAL METHODS
                                                
    Jo bhi methods double underscore se start hote h usse dunder methods bolte h
    
    
    mapping ooperators to functions:
    https://docs.python.org/3/library/operator.html

'''