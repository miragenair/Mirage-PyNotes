# var1 = 6
# var2 = 56
# var3 = int(input("enter the third number : "))
#
# if var3>var2:
#     print("greater")
# elif var3==var2:
#     print("equal")
# else:
#     print("lesser")

# list1 = [5,7,3]
# print(15 not in list1)
# if 15 not in list1:
#     print("no its not its in the list")

print("Eneter your age: ")
age = int(input())

if age<18:
    print("you are not eligible to drive")
elif age==18:
    print("get a driving test to assure you can drive")
elif age<5:
    print("how are you even using a computer?")
elif age>99:
    print("you sure you're alive?")
else:
    print("you are eligible to drive")
