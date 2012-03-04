print ("This is a decode the code game")
str1="a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
str2="1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23"

letters=str1.split(",")
numbers=str2.split(",")

code={}

k=0
for l in numbers:
    code[l]=letters[k]
    k += 1

print(code)
#for l in letters:
#    print(numbers[l])
    #print(numbers[l])
print("i am waiting for a code")8

secret=input()

for c in secret:
    print(code[c], end=''),



