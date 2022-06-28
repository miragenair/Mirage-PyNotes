def print2(str1):
    print("this is " + str1)

print2("nair")

def factorial(n):
    fac = 1
    for i in range(n):
        fac = fac*(i+1)
    return fac

number = int(input("enter the number you want th=o find the factorial of: "))
print(factorial(number))

def febonaci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return febonaci(n-1) + febonaci(n-2)

number = int(input("enter the number you want th=o find the factorial of: "))

print(febonaci(number))



number = int(input("enter the number you want to find the fibonnci series of"))