# TIO_CH12_3.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------


nameList = []
print "Enter 5 names (press the Enter key after each name):"
for i in range(5):
    name = raw_input()
    nameList.append(name)

print "The third name is:", nameList[2]

