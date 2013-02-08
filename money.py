
# creates a function(used later in the program)
def add(q, d, n, p):
    # function text...
    q = q * 25
    d = d * 10
    n = n * 5
    total = q + d + n + p
    return total
# creates a function(used later in the program)
def helper(y):
    # funtion text...
    h = [0,0]
    z = 0
    while y > 99:
        z = z + 1
        y = y - 100
        dollars = z
        cents = y
        h = [dollars,cents] 
    return h
# start
j = 'yes'
while j == 'yes':        
    # asks how many quarters
    a = int(raw_input("Enter amount of quarters "))
    # asks how many dimes
    b = int(raw_input("Enter amount of dimes "))
    # asks how many nickels
    c = int(raw_input("Enter amount of nickels "))
    # asks how many pennies
    e = int(raw_input("Enter amount of pennies "))
    # uses a function
    x=add(a, b, c, e)
    # uses a function
    hel = helper(x)
    # pops a value out of a list
    cents = hel.pop()
    # pops another value out of list
    dollars = hel.pop(0)
    # if their is no dollars
    if dollars == 0:
        # say...
        print"the answer is "+str(x)+" cents"
        # otherwise
    else:
        # say...
        print"the answer is $"+str(dollars)+"."+str(cents)
        # asks if you want to play again    
    j = raw_input("Do you want to add again(yes or no) ")
# says goodbye
print"goodbye"
