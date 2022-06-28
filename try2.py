f1 = open("mirage.txt")
try:
    f = open("miragediet.txt")

except Exception as e:
    print(e)

else:
    print("this will run only if except is not running")

finally:
    print("this statement will print anyway")

print("exception handled successfully")



