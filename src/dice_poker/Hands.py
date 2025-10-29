"""
Hands Class
by Adam Ainsworth
"""
from Player import Player

class Hands:
	def __init__(self, score_given, dice_given, description):
		self.score_given = score_given
		self.dice_given = dice_given
		self.description = description


	#Updates score and dice accordingly with the given hand
	def process_hand(self):
		Player.score += self.score_given
		Player.dice += self.dice_given
		print(self.description)
	
	#Checks if the current poker hand is a flush
	def calculate_flush(playing):
		if len(playing) != 5:
			return False
		first_suit = playing[0].suit
		flush = True
		for i in range (len(playing)):
			if playing[i].suit != first_suit:
				flush = False
				break
		return flush


	#Checks if the current poker hand is a straight
	def calculate_straight(playing):
		straight = True
		if len(playing) != 5:
			return False
		card_values = []
		for i in range(len(playing)):
			card_values.append(playing[i].point_value)
		card_values.sort()
		for i in range (len(playing)):
			if i != 4:
				if (card_values[i]) == (card_values[i + 1] - 1):
					pass
				else:
					straight = False
					break
		return straight


	#Checks if the current poker hand is a three or four of a kind
	def calculate_kinds(playing):
		first_rank = 0
		count = 0
		for i in range (len(playing)):
			first_rank = playing[i].point_value
			for a in range (len(playing)):
				if playing[a].point_value == first_rank:
					if playing.index(playing[a]) == playing.index(playing[i]):
						pass
					else:
						count += 1
			count += 1
			if count == 3:
				return 3
			elif count == 4:
				return 4
			else:
				count = 0
		if count == 0:
			return count

	#Checks if the current poker hand is a full house
	def calculate_full_house(playing):
		first_rank = 0
		pair_rank_1 = 0
		pair_rank_2 = 0
		total_1 = 0
		total_2 = 0
		pairs = 0
		for i in range (len(playing)):
			first_rank = playing[i].point_value
			for a in range (len(playing)):
				if playing[a].point_value == first_rank:
					if playing.index(playing[a]) == playing.index(playing[i]):
						pass
					else:
						if playing[a].point_value == pair_rank_1 or playing[a].point_value == pair_rank_2:
							pass
						else:
							pairs += 1
							if pair_rank_1 == 0:
								pair_rank_1 = playing[a].point_value
							elif pair_rank_2 == 0:
								if playing[a].point_value != pair_rank_1:
									pair_rank_2 = playing[a].point_value
		if pairs >= 2:
			for i in range (len(playing)):
				if playing[i].point_value == pair_rank_1:
					total_1 += 1
			for i in range (len(playing)):
				if playing[i].point_value == pair_rank_2:
					total_2 += 1
			if (total_1 + total_2) == 5:
				return True
		else:
			return False


	#Checks if the current poker hand is a pair or two pair
	def calculate_pairs(playing):
		first_rank = 0
		pairs = 0
		pair_rank = 0
		for i in range (len(playing)):
			first_rank = playing[i].point_value
			for a in range (len(playing)):
				if playing[a].point_value == first_rank:
					if playing.index(playing[a]) == playing.index(playing[i]):
						pass
					else:
						if playing[a].point_value == pair_rank:
							pass
						else:
							pairs += 1
							pair_rank = playing[a].point_value
		if pairs == 0:
			return 0
		elif pairs == 1:
			return 1
		elif pairs >= 2:
			return 2
	
	
	#Returns info about the hand.
	def __str__(self):
		return ("This hand gives  " + self.score_given + " points and  " + self.dice_given + " dice.")


if __name__ == '__main__':
	print("This is the hands class.")