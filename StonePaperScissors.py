import random

chances = 10
count_u = 0
count_c = 0
# functions:

# this is the computer choosing rock papaer and scissors
def comp_out(comp):
    if comp == 1:
        print("Rock")
    elif comp == 2:
        print("Paper")
    elif comp==3:
        print("Scissors")

# this is the winning and tie conditions of user and computer
def winning(user,comp):
    global count_u,count_c
    if comp==user:
        print("\n try again you've chosen the same")
    elif user == 1 and comp == 3:
        print("you won this round")
        count_u = count_u + 1
    elif user == 2 and comp == 1:
        print("you won this round")
        count_u = count_u + 1
    elif user == 3 and comp == 2:
        print("you won this round")
        count_u = count_u + 1
    else:
        print("the computer has won this round")
        count_c = count_c + 1

# this is the loop of the game consisting 10 chances
while(chances>=1):
    # taking input from user
    user = int(input(" 1 for Rock\n 2 or Paper\n 3 for Scissors \nEnter a number:"))
    # computer generating random output
    comp = random.randint(1,3)
    # printing the move of the computer
    print("the computer choose : ")
    comp_out(comp)
    # printing the winner of the round
    winning(user, comp)
    # printing the score as of now
    print(f"your score is {count_u} and the computer's score is {count_c}")

    #chances left for the loop
    chances = chances - 1
    print(f"chances left are {chances}\n")

#Printing the final result
if count_c == count_u:
    print("It's a tie")
elif count_c > count_u:
    print("Computer has won the game")
else:
    print("You have won the game")