"""
Card class
by Adam Ainsworth
"""

class Card:
	def __init__(self, suit, rank, point_value, name):
		self.suit = suit
		self.rank = rank
		self.point_value = point_value
		self.name = name
	
	
	#Returns name of the card as a string
	def __str__(self):
		return self.name
	

if __name__ == '__main__':
	print("This is the card class.")