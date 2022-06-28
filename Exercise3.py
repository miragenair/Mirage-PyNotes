# guess the number
while(True):
    n = 18
    i = int(input("enter the mystery number : "))
    if i == 18:
        print("congrats you've won! :)")
        break

    elif i < 18:
        print("your number is less than the mystery number")
        print("try again :(\n")
        continue
    elif i > 18:
        print("your number is greater than the mystery number")
        print("try again :(\n")
        continue
