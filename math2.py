import random
import easygui
# next step is to reduce duplicated code
# makes a variable
e='yes'
# start    
while e=='yes':
	# creates box with buttons
    a=easygui.buttonbox("which level of difficulty would you like?",
              choices=['easy', 'hard'] )
    # if choice=easy
    if a=='easy':
    # makes a random number between 1 and 10
        b=random.randint(1,10)
        c=random.randint(1,10)
        # asks math problem
        print"what is "+str(b)+"+"+str(c)            
        # takes in user answer
        d=raw_input("")
        # makes a variable
        e=c+b
        # checks user answer    
        if d==str(e):
        # says if user answer is right or wrong
            print"you are correct"
        else:
            print"nope"
         # if choice=hard   
    elif a=='hard':
		# makes a random number between 10 and 20    
        b=random.randint(10,20)
        c=random.randint(10,20)
        # asks math problem
        print"what is "+str(b)+"+"+str(c)
        # takes in user answer
        d=raw_input("")
        # makes a variable
        e=c+b
        # checks user answer
        if d==str(e):
            # says if user answer is right or wrong
            print"you are correct"
        else:
            print"nope"
            # start over
    print"do you want to play again yes or no"
    e=raw_input("")
    
    


