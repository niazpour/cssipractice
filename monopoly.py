import random


def monopoly_roll():
	total = 0
	for roll_number in range (1,4):
		die1 = randint(1,6)
		die2 = randint(1,6)
		total = total +die2 + die1
		if die1 != die2:
			#print "Doubles! Move " die1+die2 "spaces and roll again"
			return total
	return -1 
for i in range (1,20):
	print monopoly_roll