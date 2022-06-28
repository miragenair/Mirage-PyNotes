class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{self.fname}.{self.lname}@codewithharry.com"

    def explain(self):
        return f"the name of the employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return "email is not available"
        return f"{self.fname}.{self.lname}@codewithharry.com"

    @email.setter
    def email(self, str):
        print("Setting Now...")
        names = str.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

skillf = Employee("Skill","F")
print(type(skillf.email))
print(id(skillf.email))

o = "this is a string"
print(dir(o))

import inspect



#----------------------------------------------NOTES--------------------------------------------------------------------
'''
    TOPIC - object introspection
    
    kisi bhi object k baare me jaanna
    
    
'''