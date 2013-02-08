import easygui
import time
code='falcon'
name='Ryan Boyle'
a = 0
e = 1
while e == 1:
	u=easygui.enterbox("enter password")
	e = easygui.enterbox("enter your name")
	print"checking code..."
	time.sleep(2)
	#print "code= ", code
	#print "u= ", u
	if code != u and name != e:
	    easygui.msgbox("incorrect password try again")
	    a = a + 1
	else:
	    easygui.msgbox("Welcome Ryan Boyle.")
	    e = 2
	if a = 5:
		easygui.msgbox("Nice try.")