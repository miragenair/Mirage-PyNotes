a = input("enter your name : ")
b = input("enter your salary : ")
if int(b)==0:
    raise ZeroDivisionError("stopping the program because b is zero")

if a.isnumeric():
    raise Exception("numbers are not allowed")

print(f" Hello {a}")