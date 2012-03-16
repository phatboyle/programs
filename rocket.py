import time
j = int(raw_input("countdown timer: how many seconds?  "))
for i in range(j,0, -1):
    print i,
    for k in range(i,0, -1):
        print "*",
        time.sleep(.15)
    print
print"blast of"    
