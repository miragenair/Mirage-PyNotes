# -----------------------------------------------MAP----------------------------------------------------------------

# numbers = ["3", "44", "56"]
#
# numbers = list(map(int,numbers))

# for i in range(len(numbers)):
#     numbers[i]  = int(numbers[i])

# a = numbers[1] + numbers[2]
# print(a)

# def sq(a):
#     return a*a

# num =[1,3,4,52,3,23,45,2,1]

# square = list(map(sq,num))
# print(square)

# square = list(map(lambda x : x*x,num))
# print(square)

# def sqare(a):
#     return a*a
#
# def cube(a):
#     return a*a*a
#
# func = [sqare,cube]
#
# for i in range(5):
#     val = list(map(lambda x:x(i), func))
#     print(val)

# -----------------------------------------------FILTER----------------------------------------------------------------

# list_1 = [1,2,3,4,5,6,7,8,9]
#
# def gr_than_5(a):
#     return a>5
#
# gr_than_5 = list(filter(gr_than_5, list_1))
# print(gr_than_5)


# -----------------------------------------------REDUCE----------------------------------------------------------------
from functools import reduce

list_1 = [1,2,3,4]

# the more pythonic way
num = reduce(lambda x,y:x+y, list_1)
print(num)


# the dumb way
num = 0
for i in list_1:
    num = num + i
print(num)