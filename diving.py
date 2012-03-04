import random
import time
import sys
#ryimport pygame

startTime = 0
air=''

#def waitForPlayerToInput():
#    while True:
#        for event in pygame.event.get():
#            if event.key == ord('1'):
#                return 1
#            if event.type == ord('2'):
#                return 2

ryanpick='''
 ===
[0*$)   
 ===
$$$$
'''

def terminate():
    sys.exit()

def calcTime():
    return time.time() - startTime

def intro():
    print("You are right next to the water in the ocean")
    print("There is treasure in the bottom of the ocean")
    print("You want to get the treasure")
    print("You put on your diving gear")
    print("Now you are ready to go get the treasure")
    print("You dive in")
    print("You go down down down down down . . .")
    print("Then you reach the bottom")
    print("Which way will you go - 1 for right or 2 for left?")

def getAir():
    print("How much air do you want?")
    print("The range is: 5-20 seconds")
    air=input()
    print("You picked "+ air + " seconds." )
    return air

def checkAir():
    x=time.time()-startTime
    if x <= int(air):
        return True

rerun=1
while rerun==1:
    print("Hello, What is your name?")
    name=input()
    intro()
    air=getAir()
    startTime=time.time()
    computerpick = random.randint(1,2)
    pick=input("Pick a direction:")
    pick=int(pick)
    if checkAir() != True:
        print("You ran out of air")
          
    if pick == computerpick:
        print("good job " + name + " you got the treasure")
        print(ryanpick)
    
    if pick != computerpick:
        print("sorry, you didn't get the treasure")

    print("Do you want to play agin (yes or no)")
    fish=input()
    if fish=="yes":
        rerun=1
    if fish=="no":
        rerun=0

