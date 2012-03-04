import random

print("which one 1 2 3 4 5 6")
pick=input()
die=random.randint(1,6)
if pick==die:
    print("you are correct")
else:   
      print("you are wrong")


