import easygui
code='orcas_live_in_h2o'
print"enter password"
u=raw_input("")
print"checking code..."
#print "code= ", code
#print "u= ", u
if code != u:
    easygui.msgbox("nice try")
else:
    print"welcome ryan boyle"
