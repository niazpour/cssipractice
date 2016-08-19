# Happy Parrot - This parrot is so happy. It accepts a 'thing' as its argument and then returns a string where it says how happy it is about the thing!
def happy_parrot(thing):
  template = "I am so happy about %s!"
  speech = template % thing
  print speech

happy_parrot('carrots')
# Boring Parrot - Write a method for a boring parrot that just returns whatever string you give him as an argument.



# Math Parrot - Create a method that accepts two numbers as arguments and adds them together!
def math_parrot(x,y):
	print x +y

math_parrot(5,7)

# Friendly Parrot - This parrot greets people by returning their name and age (don't forget to pass that information in as arguments).
def friendly_parrot(name, age):
	print "Hello, %s! You are %s years old!" % (name,age)

friendly_parrot("Niaz",18)

# Favorites Parrot - Tell this parrot about your three favorite things and he will return "I love <that thing> too!" for each of them.
def favorites_parrot(thing1,thing2,thing3):
	template = "I love %s too!"
	faves = [thing1, thing2, thing3]
	speech = ""
	for fave in faves:
		speech = speech + template % fave
	print speech

favorites_parrot ("pilates", "djs", "coffee")

# Now try calling your methods below with any arguments of your choice and puts them to the screen. Like this:
print happy_parrot("waffles")
# call your methods here


# Now let's pretend you are a wizard and you want to place a spell on each of the parrots so that they speak backwards. How would you do that?
def backwardsparrots(speech)
	print speech
	
	happy_parrot('carrots')
	math_parrot(5,7)
	friendly_parrot("Niaz",18)
	favorites_parrot ("pilates", "djs", "coffee")


# The spell has been broken and everyone is speaking normally again. The parrots are really excited about it though - make them shout in all caps.