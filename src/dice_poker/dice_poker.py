"""
Dice Poker Game
by Adam Ainsworth
"""
import random
from card import card
from game_manager import game_manager


cards_index =	{
	"2": ("2"),
	"3": ("3"),
	"4": ("4"),
	"5": ("5"),
	"6": ("6"),
	"7": ("7"),
	"8": ("8"),
	"9": ("9"),
	"10": ("10"),
	"11": ("Jack"),
	"12": ("Queen"),
	"13": ("King"),
	"14": ("Ace")
}


suit_index =	{
	"1": ("Spades"),
	"2": ("Diamonds"),
	"3": ("Clubs"),
	"4": ("Hearts"),
}


#Main variables and lists
hand = []
playing = []


#Draws a random card out of 52
def draw_card():
	card_suit_id = random.randrange(1, 5)
	card_value = random.randrange(2, 15)
	card_suit = suit_index[str(card_suit_id)]
	card_rank = cards_index[str(card_value)]
	card_name = card_rank + " of " + card_suit

	new_card = card(card_suit, card_rank, card_value, card_name)
	return new_card


#Shows what cards are in hand and which are being played.
def show_cards():
	print("")
	print("Score: " + str(game_manager.score))
	print("Dice: " + str(game_manager.dice))
	print("Cards in Hand:")
	for i in range (len(hand)):
		print(str(i + 1) + ": " + str(hand[i]))
	print("")
	print("Cards to be Played:")
	for i in range (len(playing)):
		print(str(i + 1) + ": " + str(playing[i]))
	game_process()
	return


#Asks the player what action they want to take
def game_process():
	hand_length = len(hand)
	cards_play_length = len(playing)
	play_cards = input("Draw Cards ('roll') Play Card ('#') Play Hand ('play') Quit ('q'): ")
	try:
		play_cards = int(play_cards)
	except ValueError:
		if play_cards == "roll":
			if game_manager.dice >= 1:
				game_manager.dice -= 1
				for i in range(random.randrange(1, 7)):
					new_card = draw_card()
					hand.append(new_card)
				show_cards()
				return
			else:
				print("No dice remaining")
				game_process()
				return
		elif play_cards == "play":
			play_hand()
			return
		elif play_cards == "q":
			return
		else:
			print("Unrecognized command")
			show_cards()
			return
	if cards_play_length < 5:
			if play_cards > hand_length or play_cards <= 0:
				print("Card not found")
				game_process()
				return
			else:
				process(play_cards)
				return
	else:
		print("Max hand size is 5")
		game_process()
		return


#Calculates the point value of played hand and updates the score
def play_hand():
	print("Calculating hand...")
	if calculate_flush() == True:
		if calculate_straight == True:
			print("Hand: Straight Flush! +5 dice +100 points")
			game_manager.dice += 5
			game_manager.score += 100
		else:
			print("Hand: Flush. +2 dice +40 points")
			game_manager.dice += 2
			game_manager.score += 30
	elif calculate_kinds() == 4:
		print("Hand: Four of a Kind. +4 dice +80 points")
		game_manager.dice += 4
		game_manager.score += 80
	elif calculate_full_house() == True:
		print("Hand: Full House. +2 dice +35 points")
		game_manager.dice += 2
		game_manager.score += 20
	elif calculate_straight() == True:
		print("Hand: Straight. +2 dice +30 points")
		game_manager.dice += 2
		game_manager.score += 30
	elif calculate_kinds() == 3:
		print("Hand: Three of a Kind. +1 dice +25 points")
		game_manager.dice += 1
		game_manager.score += 25
	elif calculate_pairs() == 2:
		print("Hand: Two Pair +1 dice +15 points")
		game_manager.dice += 1
		game_manager.score += 15
	elif calculate_pairs() == 1:
		print("Hand: Pair. +10 points")
		game_manager.score += 10
	else:
		print("Hand: High Card. No bonuses")
	for i in range (len(playing)):
		game_manager.score = game_manager.score + playing[i].point_value
	playing.clear()
	show_cards()
	return


#Checks if the current poker hand is a flush
def calculate_flush():
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
def calculate_straight():
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
def calculate_kinds():
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
def calculate_full_house():
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
def calculate_pairs():
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


#Plays the card the player chose
def process(play_cards):
	playing.append(hand[int(play_cards) - 1])
	hand.remove(hand[int(play_cards) - 1])
	show_cards()
	return


def main():
	for i in range(8):
		new_card = draw_card()
		hand.append(new_card)
	show_cards()
	return


if __name__ == "__main__":
	main()