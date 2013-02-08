# what do we need to know to solve the problem?


print "are you a girl or boy?"
gb = raw_input()
if gb=='girl':
    print "what is your age?"
    age = raw_input()
    if age==10:
        print "you are allowed to be on the soccer team"
    else:
        print "sorry, you are a girl but you are not 10, so you are not allowed to be on the soccer team."
else:
    print "sorry, you are not a girl so you are not allowed to be on the soccer team."
