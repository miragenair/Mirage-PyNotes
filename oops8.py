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


class Player:
    no_of_games = 4
    def __init__(self, name, games):
        self.name = name
        self.games = games

    def printdetails(self):
        return f"the name of the player is {self.name}, and the games the player plays is {self.games}"

class CoolProgrammer(Employees, Player):
    language = "python"
    def languagess(self):
        print(f"the language that the CoolProgrammer knows is {self.language}")

harry = Employees("Harry", 45000, "Instructor")
rohan = Employees("Rohan", 45321, "HR")
aditya = Employees.change_str("Aditya-000001-bhadwa")
shivansh = Player("Shivansh", ["football","TableTennis"])

print(aditya.role)
aditya.printname("mirage")
print(shivansh.printdetails())

mirage = CoolProgrammer("Mirage", 19999, "CoolProgrammer")
print(mirage.printdetails())
mirage.languagess()


# -------------------------------------------NOTES----------------------------------------------------------------------
'''
    This OOPS tut is about multiple inheritance  
    
    jp bhi class pehele likhege uss class ka variable hee show karega as output and vo hee varaible ko sabse jyada importance dega
'''