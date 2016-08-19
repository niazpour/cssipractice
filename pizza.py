class Pizza:
	def __init__ (self, heat_start):
		self.heat_value = heat_start
		self.raw = True

	def overheat(self):
		self.heat_value >= 10
		print "I'm burnt..."

	def get_heat(self):
		if self.raw:
			return self.heat_value
		else:
			print "You haven't cooked me?"
			return(0)
	def cook(self):
		self.heat_value = self.heat_value + 0.5

		if self.heat_value <= 0:
			self.raw = True
			return
		if self.heat_value >=7:
			print "I'm burning!!"

cookingpizza = Pizza(10)
print cookingpizza.get_heat()
cookingpizza.cook()
print cookingpizza.get_heat()
cookingpizza.cook()
print cookingpizza.get_heat()
cookingpizza.cook()
print cookingpizza.get_heat()
cookingpizza.overheat()