num_guesses = 0

while num_guesses <3:
	input = raw_input("Enter guess:")
	num_guesses = num_guesses + 1
	inputnum = int(input)
	if inputnum >7:
		print "too big"
	elif inputnum <7:
		print "too small"
	else:
		print "just right"
		quit()
print "you suck"