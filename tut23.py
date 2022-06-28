# a=8
# b=9
# c=sum((a,b)) #built in function
# def function1(a,b):
#     print("hello youre in function 1", a+b)
# (function1(5,7))

def function2(a,b):
    """This is a function which calculates the average of two numbers
    this function doesnt work for three numbers"""
    average= (a+b)/2
    # print(average)
    return average

n = function2( 5  ,7)
print(function2.__doc__)