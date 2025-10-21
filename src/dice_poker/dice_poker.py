"""
Dice Poker Game
by Adam Ainsworth
"""
import random
from card import Card




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
score = 0
dice = 2


#Draws a random card out of 52
def draw_card():
	card_suit_id = random.randrange(1, 4)
	card_value = random.randrange(2, 14)
	card_suit = suit_index[str(card_suit_id)]
	card_rank = cards_index[str(card_value)]
	card_name = card_rank + " of " + card_suit

	new_card = Card(card_suit, card_rank, card_value, card_name)
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