#goodfood = raw_input ('Enter the name of what\'s good:')
#food = food.upper()
#vowels = ['A','E','I','O','U']
#for vowel in vowels:
#	food = food.replace(vowel,vowel*5)
#print food

#badfood = raw_input ('Enter the name of what\'s bad:')
#badfood = badfood.upper()
#for vowel in vowels: 
#	badfood = badfood.replace (vowel,vowel*10)
#print badfood

vowels = ['A','E','I','O','U']
def yell(word,times):
	shout = word.upper()
	for vowel in vowels:
		shout = shout.replace(vowel, vowel * times)
	print shout
goodfood = raw_input ('Enter the name of what\'s good:')
badfood = raw_input ('Enter the name of what\'s bad:')
yell(goodfood,5)
yell(badfood,10)