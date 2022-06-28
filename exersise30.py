a = int(input("enter the number of rows : "))
b = int(input("enter 1 for True and 0 for False : "))
c = 1
p = ("*")

if b==1:
    while(a>=0):
        print(p*a)
        a = a - 1

if b==0:
    while(c<=a):
        print(p * c)
        c = c + 1

