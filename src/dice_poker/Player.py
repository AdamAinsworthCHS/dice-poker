"""
Game Manager Class
by Adam Ainsworth
"""

class Player:
	dice = 2
	score = 0
	def __init__(self, name):
		self.name = name
	
	
	def __str__(self):
		"""
		This method returns info about the player.
		"""
		return (self.name + " has " + str(self.score) + " points and " + str(self.dice) + " dice.")


if __name__ == '__main__':
	print("This is the player class.")