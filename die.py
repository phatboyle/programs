import random

print("which one 1 2 3 4 5 6")
pick=input()
pick=int(pick)   #convert pick to an integer
die=random.randint(1,6)
if pick==die:
    print("you are correct")
else:   
      print("you picked",pick,"but the right answer is",die)


