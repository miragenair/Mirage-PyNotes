import time
import datetime
import pygame
from pygame import mixer

pygame.init()

def printtime():
    localtime = time.asctime(time.localtime(time.time()))
    return localtime

def logrecord():
    f = open("logentries.txt","a")
    a = f.write(f"{printtime()}\n")
    f.close()

def writetask():
    f = open("logentries.txt", "a")
    b = f.write(f"{t}")
    f.close()

def enterdata():
    writetask()
    logrecord()

# task = input(" enter w for water \n enter e for eyes \n enter p for physical \n Enter your choice : ")
# user = input("Are you done?\n Enter Y or N: ")
# water = "w"
# eyes = "e"
# physical = "p"
t = str


a = 1
i = 1
j = 1
k = 1
clock=1

print("your day has been initiated:)")

timeee = datetime.datetime.now().time()
timeee1 = datetime.time(9,0,0)
timeee2 = datetime.time(17,0,0)
while(timeee1<timeee<timeee2):

# while(True):
    time.sleep(a)
    # print(f"the time is {clock} secs")
    # print("your entry has been recorded")
    if i==2100:
        mixer.music.load('waterisH2O.mp3')
        mixer.music.play()
        user = str(input("did you drink water? \nType drank or no"))
        if user == "drank":
            mixer.music.stop()
            t = "You drank water at this time:                                      "
            enterdata()
            print("your entry has been recorded")
            i=1
        elif user == "no":
            mixer.music.stop()
            print("your log is not updated. It will be updated when you complete the eye training exercise")
            i=1

    elif j==1800:
        mixer.music.load('eyes.mp3')
        mixer.music.play()
        user = str(input("did you do the eye exercise? \nType done or no"))
        if user == "done":
            mixer.music.stop()
            t = "You did the eye training exersise sucessfully at this time:        "
            enterdata()
            print("your entry has been recorded")
            j=1
        elif user == "no":
            mixer.music.stop()
            print("your log is not updated. It will be updated when you complete the eye training exercise")
            j=1

    elif k==2700:
        mixer.music.load('workout.mp3')
        mixer.music.play()
        user = str(input("Did you do the physical activity? \nType done or no"))
        if user == "done":
            mixer.music.stop()
            t = "You did the physical training exersise sucessfully at this time:   "
            enterdata()
            print("your entry has been recorded")
            k = 1
        elif user == "no":
            mixer.music.stop()
            print("your log is not updated. It will be updated when you complete the physical activity")
            k = 1
    i+=1
    j+=1
    k+=1
    clock+=1