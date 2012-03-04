import easygui


name=easygui.enterbox("what is your name?")
house=easygui.enterbox("what is your house number")
ave=easygui.integerbox("what is your ave/street(no letters)")
city=easygui.enterbox("what is your city")
state=easygui.enterbox("what is your state")
zipcode=easygui.enterbox("what is your zip code")
print "your address is "+name, house, str(ave) +"th"+ city, state

easygui.msgbox("your address is " + ", "+ name +", "+ house +", "+  str(ave) +"th" +", "+ city +", "+ state) 
