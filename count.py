print("Enter how high you want to count:")
i=0
YourPick = input()
YourPick =int(YourPick)

print("Enter how many to skip each time:")
skip=input()
skip=int(skip)

while i <= YourPick:
    print(str(i))
    i=i+skip
    
