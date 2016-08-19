phone_number = raw_input("Enter phone number: ")
# Is phone_number a valid phone number?
# We say a valid phone number looks like 
# (111)111-1111
phone_number = phone_number.strip()

if len(phone_number) != 13:
	print "Bad"
	quit()

if phone_number[0] != '(':
	print "Bad"
	quit()
if phone_number[4] != ')':
	print "Bad"
	quit()

area_code = phone_number[1:4]
exchange = phone_number[5:8]
routing_number = phone_number[9:13]


digits = ['0','1','2','3','4','5','6','7','8','9']

for c in area_code:
	if c not in digits:
		print "Bad digit"
		quit()

for i in [1,2,3,4,5,6,7,8,9,10,11,12]:
	if phone_number[i] not in digits:
		print "Bad digit"
		
print "Good!"