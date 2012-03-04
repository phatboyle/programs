

quarters = raw_input("How many quarters? ")

dimes = raw_input("How many dimes?" )
pennies = raw_input("How many pennies?")
nickels = raw_input("How many nickels?")

quarters=int(quarters)
dimes=int(dimes)
pennies=int(pennies)
nickels = int(nickels)

change= quarters*25+dimes*10+pennies+nickels*5
change=str(change)

print("Here is how much money you have: " + change )
