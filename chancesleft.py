# chances left
print("Find the mystery number which is between 1 and 20")
print("You only have 10 chances to guess the number")
i = int
t = 10

try:
    i=int(input())
except Exception as e:
    print(e)

while(t<=10):
    if t==0:
        print("GAME OVER :'( ")
        break
    if i == 18:
        print("Congrats you've won! :)")
        break

    else:
        # guess the number
        while (True):
            n = 18
            i = int(input("Enter the mystery number : \n"))
            if i == n:
                break
            elif i < n:
                print("You have to guess higher for the mystery number")
                print("Try again :(\n")
                break
            elif i > n:
                print("You have to guess lower for the mystery number")
                print("Try again :(\n")
                break

        t = t - 1
        print("Chances left", t, "/ 10")
        continue