# Listing_23-3.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# Looking for 10 heads in a row

from random import *
coin = ["Heads", "Tails"]
heads_in_row = 0
ten_heads_in_row = 0
b=0
for i in range(1000):
    b += 1
    if choice(coin) == "Heads":                                     
        heads_in_row += 1
    else:
        heads_in_row = 0
    
    if heads_in_row == 10:
        break;
        #ten_heads_in_row += 1
        #heads_in_row = 0
if b==1000:
    b = 'unknown'
print"it takes ",b,"dice rolls until you get ten heads in a row"