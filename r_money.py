
def add(q, d, n, p):
    q = q * 25
    d = d * 10
    n = n * 5
    total = q + d + n + p
    return total
print"the cash that you are about to type in MUST equal less then a dollar"
a = int(raw_input("Enter amount of qurters "))
b = int(raw_input("Enter amount of dimes "))
c = int(raw_input("Enter amount of nickels "))
e = int(raw_input("Enter amount of penies "))
x=add(a, b, c, e)
print"the answer is "+str(x)+" cents"

## 31


