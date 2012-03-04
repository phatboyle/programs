# ask the user what level of difficulty
# ask the user the math problem
# if right, print you are correct
# if wrong, print you are wrong, and give a new problem
import random
import easygui
e='yes'    
while e=='yes':
    a=easygui.buttonbox("which level of difficulty would you like?",
              choices=['easy', 'hard'] )
    if a=='easy':
        b=random.randint(1,10)
        c=random.randint(1,10)
        print"what is "+str(b)+"+"+str(c)            
        d=raw_input("")
        e=c+b    
        if d==str(e):
            print"you are correct"
        else:
            print"nope"
    elif a=='hard':
        b=random.randint(1,20)
        c=random.randint(1,20)
        print"what is "+str(b)+"+"+str(c)
        d=raw_input("")
        e=c+b
        if d==str(e):
            print"you are correct"
        else:
            print"nope"
    print"do you want to play again yes or no"
    e=raw_input("")
    
    


