# Exercise 2 - Faulty calculator

# false results: 45*3=555, 56+9=77, 56/6=4

a = int(input("enter the first number : "))
b = int(input("enter the second number : "))
f = input("enter the math function you want to perform : ")

if a==56 and b==9 and f=="add":
    print("77")
elif f=="add":
    print("the addition of the numbers gives you", int(a)+ int(b))

elif f == "substract":
    print("the substraction of the numbers gives you", int(a)- int(b))

if a==45 and b==3 and f=="multiply":
    print("555")
elif f=="multiply":
    print("the multipilcation of the numbers gives you", int(a)* int(b))

if a==56 and b==6 and f=="divide":
    print("4")
elif f=="divide":
    print("the division of the numbers gives you", int(a)/ int(b))

