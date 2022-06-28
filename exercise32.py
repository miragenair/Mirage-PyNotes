a = int(input("press 1 for mirage, press 2 for aditya and press 3 for sahil : "))

if a == 1:
    print("welcome to mirage's health log")
    with open("miragehealth.txt") as f:
        i = int(input("type 1 for workouts and 2 for diet"))
        if i==1:
            print("welcome to mirages workout plan")
            with open("miragehealth.txt") as f:
                b = f.read()
                print(b)
        elif i==2:
            print("welcome to mirages diet plan")
            with open("miragediet.txt") as f:
                b = f.read()
                print(b)
                c = input("add a new meal:")
                f = f.append()