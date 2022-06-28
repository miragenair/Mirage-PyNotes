class Employees:
    no_of_leaves = 8
    pass

Harry = Employees()
Harry.name = "Harry"
Harry.salary = 45000
Harry.role = "Instructor"

Rohan = Employees()
Rohan.name = "Rohan"
Rohan.salary = 45321
Rohan.role = "HR"
Rohan.no_of_leaves = 10


# print(Rohan.no_of_leaves)
print(Rohan.__dict__)