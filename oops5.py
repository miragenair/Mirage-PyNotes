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

    @classmethod
    def change_str(cls, string):
        # param = string.split("-")
        # return cls(param[0],param[1],param[2])                        ----------ye ek bohot hee bada method h
        return cls(*string.split("-"))                                 #----------ye smart work h *args k help se kitne bhi numerals le sakte h


harry = Employees("Harry",45000,"Instructor")
rohan = Employees("Rohan",45321,"HR")
aditya = Employees.change_str("Aditya-000001-bhadwa")


harry.changeleaves(99)

print(harry.no_of_leaves)
print(aditya.role)



# -------------------------------------------NOTES----------------------------------------------------------------------
'''
    used split function and created another class which accepts string as a whole
    the split function returns the splitted string as individual objects or varialbe values in a list
    
    
    ye tabhi use karte h jab ek bohot bade text file me se data abstract karna hoga tabhi 
    kyuki waha sab data ek string k format me hee hota h
'''