import random

phrases = ['Is anyone there?', 'Who survived?', 'Somebody new?', 'Oh -Hi', 'Anyone else but you?!','Hi','hi',"hello"]
random_greeting = random.choice(phrases)

deep = ['Don\'t let me go alone', 'I depend on you','what','top secret']
responses = ['Let\'s never speak of this again','oh','great']
random_response = random.choice(responses)

while True:
	user = raw_input()
	if user in phrases:
		print(random_greeting)
	elif user in deep:
		print(random_response)
	else:
		print("Oh but I can't hear the sound")
		quit()
