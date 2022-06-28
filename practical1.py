# Create a list A with numbers in it
l1 = [0,77,93,53,42,56,6,7,8,9]
print(l1[1])

# adding an elemnt
a=33
l1.append(a)
print(l1)

# Create a list A with names in it
n1 = ["mirage","sahil","aditya"]
print(n1[1])

# removing an element using remove
n1.remove("mirage")
print(n1)

# removing an element using pop
n2 = ["mango","cherry","apple","banana"]
n2.pop(0)
n2.pop()
print(n2)

# deleting
n3 = ["this","is","an","example"]
del n3

# clear the elements of the list
n4 = ["this","is","another","example"]
n4.clear()
print(n4)

n5= ["this","is","another","example"]
extended = ("this","is","another","extended")

n5.extend(extended)
print(n5)
print(type(n5))

# list can have different datatypes
list1 = ["this","is","string"]
list2 = [1,2,3,4,5,6,7]
list3 = [True,False,True]


print(list1)
print(list2)
print(list3)

list4 = ["this",1,True]
print(list4)

# another way of creating a list
# can be changed
# is mutable
asd = list(("this",5,True))
print(type(asd))

# creating a tupple
# tupple cannot be changed
# it is immutable
wasd= (1,2,3,4,5)
print(type(wasd))

# ARRAY

car = ["ford","ferrari","lamborghini", "chevy","toyota"]
car1 = "ford"
print(len(car))

for x in car:
    print(x)

# again appending in array same as list
car.append("buggati")
print(car)

# poping the 4th element
car.pop(3)
print(car)

# printing a reversed list
car.reverse()
print(car)

carss = ["mcqueen","dinoco"]
toys = ["buzz","woody"]

for x in carss:
    print(x)
for y in toys:
    print(y)

# dictionaries
dictionary = {"car":"ford",
              "model":"mustang",
              "made in":"USA"
}
# printing keys
print(dictionary.keys())
# printing values
print(dictionary.values())
# poping and printing

print(dictionary.pop())
