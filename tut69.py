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


hindustani_suppoter = Employee("Hindustani","Suppoter")
nikhil_raj_pandey = Employee("Nikhil","Raj Pandey")

print(hindustani_suppoter.email)

hindustani_suppoter.fname = "US"
print(hindustani_suppoter.email)

hindustani_suppoter.email = "this.that@codewithharry.com"
print(hindustani_suppoter.email)

del hindustani_suppoter.email

print(hindustani_suppoter.email)
#------------------------------------------------NOTES------------------------------------------------------------------
'''
    setter decorator

    generally we dont delete in oop
    we set the thing to null instead
    
'''