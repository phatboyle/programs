def round_up(num):
	num2 = num
	num3 = num - int(num2)
	if num3 <> 0.0:
		num2 = num2 + 1
		num2 = num2 - num3
	return num2

def guess(low,high):
	between = high - low
	the_guess = low + between/2
	round_up(the_guess)
	return the_guess


# print guess to user
# ask user if it's the number.  They will reply, yes, or lower or higher
# if yes, then finish
# recalculate low/high based on what the user says
# loop
low = 1
high = 100
while True:
	g = guess(low,high)
	e = raw_input("Is this it?"+str(g)+" ")
	if e == 'lower':
		high = g
	if e == 'higher':
		low = g
	if e == 'yes':
		print"I guessed it you can't trick me nana nabooboo!"
		break