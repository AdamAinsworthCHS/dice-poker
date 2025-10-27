"""
Card class
by Adam Ainsworth
"""

class card:
	def __init__(self, suit, rank, point_value, name):
		self.suit = suit
		self.rank = rank
		self.point_value = point_value
		self.name = name
	def __str__(self):
		return self.name