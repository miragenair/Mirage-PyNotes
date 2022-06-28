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

harry = Employees("Harry",45000,"Instructor")
rohan = Employees("Rohan",45321,"HR")

harry.changeleaves(99)

print(harry.no_of_leaves)



# -------------------------------------------NOTES----------------------------------------------------------------------
'''
employees ek class h
harry and rohan objects h ussi class k
unka naam, salary, division ek attribute h unhi ka
nno_of_leaves ek class ka instance h jo harry aur rohan k liye common h
and agar mene specifiaclly harry/rohan k ano of leaves change kiya toh vo ek instance hota h

'''