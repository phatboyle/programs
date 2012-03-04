import random
a=random.randint(1,10)
b=random.randint(1,10)
c=a+b
print"hello what is your name"
name=raw_input("")



print"well" , name , "I am going to give you a math problem and you are going to figure it out and I will if you are right or wrong"
print a , "+" , b


e=raw_input("")
e=int(e)
if c < e:
    print"you are wrong"
elif c > e:
    print"you are wrong"
else:
    print"you are right"

