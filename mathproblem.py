import random

print("Enter your name:")

yourname=input()

replay=1
while replay==1:
    x=random.randint(1,10)
    y=random.randint(1,10)

    print("yourname has " + str(x) + " turkeys " + " and " + str(y) + " chickens.  How many birds does he have?")

    answer = x+y

    i = input()
    i=int(i)

    if i==answer:
        print("correct!")
    else:
        print("wrong")
        print("The correct answer is: " + str(answer))

    print("Would you like to play again (yes, no)?")
    p=input()

    if p=="no":
        replay=0



              
              
              
    
