"""
Card class
By Adam Ainsworth
"""

class card:
	def __init__(self, suit, rank, point_value, name):
		self.suit = suit
		self.rank = rank
		self.point_value = point_value
		self.name = name
	def get_value(self):
		return self.rank
	def get_suit(self):
		return self.suit
	def get_point_value(self):
		return self.point_value
	def __str__(self):
		return self.name