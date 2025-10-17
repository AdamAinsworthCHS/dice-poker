"""
Dice Poker Game
by Adam Ainsworth
"""
import random


class Card:
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


cardsIndex =	{
	"0": ("spade", "2", 2, "2 of Spades"),
	"1": ("spade", "3", 3, "3 of Spades"),
	"2": ("spade", "4", 4, "4 of Spades"),
	"3": ("spade", "5", 5, "5 of Spades"),
	"4": ("spade", "6", 6, "6 of Spades"),
	"5": ("spade", "7", 7, "7 of Spades"),
	"6": ("spade", "8", 8, "8 of Spades"),
	"7": ("spade", "9", 9, "9 of Spades"),
	"8": ("spade", "10", 10, "10 of Spades"),
	"9": ("spade", "jack", 11, "Jack of Spades"),
	"10": ("spade", "queen", 12, "Queen of Spades"),
	"11": ("spade", "king", 13, "King of Spades"),
	"12": ("spade", "ace", 14, "Ace of Spades"),
	"13": ("club", "2", 2, "2 of Clubs"),
	"14": ("club", "3", 3, "3 of Clubs"),
	"15": ("club", "4", 4, "4 of Clubs"),
	"16": ("club", "5", 5, "5 of Clubs"),
	"17": ("club", "6", 6, "6 of Clubs"),
	"18": ("club", "7", 7, "7 of Clubs"),
	"19": ("club", "8", 8, "8 of Clubs"),
	"20": ("club", "9", 9, "9 of Clubs"),
	"21": ("club", "10", 10, "10 of Clubs"),
	"22": ("club", "jack", 11, "Jack of Clubs"),
	"23": ("club", "queen", 12, "Queen of Clubs"),
	"24": ("club", "king", 13, "King of Clubs"),
	"25": ("club", "ace", 14, "Ace of Clubs"),
	"26": ("diamond", "2", 2, "2 of Diamonds"),
	"27": ("diamond", "3", 3, "3 of Diamonds"),
	"28": ("diamond", "4", 4, "4 of Diamonds"),
	"29": ("diamond", "5", 5, "5 of Diamonds"),
	"30": ("diamond", "6", 6, "6 of Diamonds"),
	"31": ("diamond", "7", 7, "7 of Diamonds"),
	"32": ("diamond", "8", 8, "8 of Diamonds"),
	"33": ("diamond", "9", 9, "9 of Diamonds"),
	"34": ("diamond", "10", 10, "10 of Diamonds"),
	"35": ("diamond", "jack", 11, "Jack of Diamonds"),
	"36": ("diamond", "queen", 12, "Queen of Diamonds"),
	"37": ("diamond", "king", 13, "King of Diamonds"),
	"38": ("diamond", "ace", 14, "Ace of Diamonds"),
	"39": ("heart", "2", 2, "2 of Hearts"),
	"40": ("heart", "3", 3, "3 of Hearts"),
	"41": ("heart", "4", 4, "4 of Hearts"),
	"42": ("heart", "5", 5, "5 of Hearts"),
	"43": ("heart", "6", 6, "6 of Hearts"),
	"44": ("heart", "7", 7, "7 of Hearts"),
	"45": ("heart", "8", 8, "8 of Hearts"),
	"46": ("heart", "9", 9, "9 of Hearts"),
	"47": ("heart", "10", 10, "10 of Hearts"),
	"48": ("heart", "jack", 11, "Jack of Hearts"),
	"49": ("heart", "queen", 12, "Queen of Hearts"),
	"50": ("heart", "king", 13, "King of Hearts"),
	"51": ("heart", "ace", 14, "Ace of Hearts"),
}


#Main variables and lists
hand = []
playing = []
score = 0
dice = 2


#Draws a random card out of 52
def draw_card():
	card_id = random.randrange(0, 51)
	draw_card = str(card_id)
	card_list = list(cardsIndex[draw_card])

	new_card = Card(card_list[0], card_list[1], card_list[2], card_list[3])
	return new_card


#Shows what cards are in hand and which are being played.
def show_cards():
	print("")
	print("Score: " + str(score))
	print("Dice: " + str(dice))
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
	global dice
	hand_length = len(hand)
	cards_play_length = len(playing)
	play_cards = input("Draw Cards ('roll') Play Card ('#') Play Hand ('play') Quit ('q'): ")
	try:
		play_cards = int(play_cards)
	except ValueError:
		if play_cards == "roll":
			if dice >= 1:
				dice -= 1
				for i in range(random.randrange(1, 6)):
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
	global score
	for i in range (len(playing)):
		score = score + playing[i].get_point_value()
	playing.clear()
	show_cards()
	return


#Plays the card the player chose REWRITE NAME LATER
def process(play_cards):
	playing.append(hand[int(play_cards) - 1])
	hand.remove(hand[int(play_cards) - 1])
	show_cards()
	return


def main():
	global score
	global dice
	hand.clear()
	playing.clear()
	score = 0
	dice = 2
	for i in range(8):
		new_card = draw_card()
		hand.append(new_card)
	show_cards()
	return


if __name__ == "__main__":
	main()