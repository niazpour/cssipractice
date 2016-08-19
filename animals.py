class Animal:
	def __init__(self,name):
		self.name = name
	def eat(self):
		print 'homf nomf'
class Cat(Animal):
	def noise(self):
		print 'meow'
	def call(self, message):
		print "...."
class Dog(Animal):
	def call(self,message):
		if message == ("Here, %s" % self.name):
			print "!!!!!!!"
		else:
			print "...."
	def eat(self):
		print 'nom nom nom nom nom nom nom'
