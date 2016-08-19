class Houseplant:
	def __init__ (self, water_start):
		#Initialize property values
		#water goes from 0 to 10
		self.water_value = water_start
		self.alive = True
	#watering makes water go to max.
	def water(self):
		self.water_value = 10

	#how much water?
	def get_water(self):
		if self.alive:
			return self.water_value
		else:
			print "You killed me"
			return(0)
	def time_passes(self):
		self.water_value = self.water_value - 0.5

		if self.water_value <= 0:
			self.alive = False
			return
		if self.water_value <= 2:
			print "Water level low: %s!" % self.water_value

plant = Houseplant(3)
print plant.get_water()
plant.time_passes()
print plant.get_water()
plant.time_passes()
print plant.get_water()
plant.time_passes()
print plant.get_water()
plant.time_passes()
print plant.get_water()
plant.time_passes()
print plant.get_water()
plant.water()
print plant.get_water()