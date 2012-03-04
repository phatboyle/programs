import easygui
name=raw_input("hello what is your name ")
h=raw_input(name + " can you tell me how much degrees fahrenheit it is outside ")
h=int(h)
h=h-32
h=h*5
h=h/9
h=str(h)
print("this is how much degrees celsius it is " + name)
print(h)
