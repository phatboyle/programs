import random
# ask the user ther name
# pick two random numbers between 1 and 20
# create a math question with the two random numbers
# have the user input their answer
# tell them whether they had it right or wrong


print("hello what is your name")
name=input()
y=random.randint(1,20)
x=random.randint(1,20)
print(name+ " had " +str(x)+ " mini stuffed orcas he got" +str(y)+ "more how many orcas did he have in all")
number=input()
if int(number)==(x+y):
    print("you are correct")
else:
    print("you are wrong")
