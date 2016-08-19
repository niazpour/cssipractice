def GoGetDinner(food):
	print 'Close Computer'
	print 'Stand up'
	print 'Walk out the door'
	if food =='salad':
		print 'Ew, no thanks!'
		return 0
	print 'Eat ' + food
	return 1 
print "eating pizza: %s" % GoGetDinner('pizza')
GoGetDinner('tacos')
GoGetDinner('salad')
