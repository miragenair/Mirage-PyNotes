class Employees:
    no_of_leaves = 8
    _protected = 9
    __private = 12

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


harry = Employees("Harry",459,"programmer")
print(harry._protected)
print(harry._Employees__private)


# ------------------------------NOTES-----------------------------------------------------------------------
'''

    PUBLIC => ghar k bahar paper chipka diya
    PROTECTED => ghar k andar paper chipka diya
    PRIVATE => sirf khudke pass paper ka access h

'''