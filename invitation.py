name = raw input("Who's graduating?")

if name = "Percy":
	print percy_invitation = """
Dear Friend,
	The family of Percy Weasley proudly invite you to their graduation commencement on Saturday the 22nd of May 1993.
Festivities will be held at The Burrow. See you then!
RSVP by 15th
													Sincerely, 
														The Weasley Family
"""
elif name = "Ron":
	ron_invitation = percy_invitation.replace ("Percy","Ron").replace ("1993","1997").replace ("22nd","18th").replace ("Saturday","Sunday")
	print ron_invitation
elif name = "Ginny":
	ginny_invitation = percy_