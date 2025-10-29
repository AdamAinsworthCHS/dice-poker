"""
Dice Poker Game
by Adam Ainsworth
"""
import random
from Card import Card
from Player import Player
from Hands import Hands
from Deck import Deck

straight_flush = Hands(100, 5, "Hand: Straight Flush! +5 dice +100 points")
four_of_a_kind = Hands(80, 4, "Hand: Four of a Kind. +4 dice +80 points")
full_house = Hands(50, 3, "Hand: Full House. +3 dice +50 points")
flush = Hands(40, 2, "Hand: Flush. +2 dice +40 points")
straight = Hands(30, 2, "Hand: Straight. +2 dice +30 points")
three_of_a_kind = Hands(25, 1, "Hand: Three of a Kind. +1 dice +25 points")
two_pair = Hands(15, 1, "Hand: Two Pair. +1 dice +15 points")
pair = Hands(10, 0, "Hand: Pair. +10 points")
high_card = Hands(0, 0, "Hand: High Card. No bonuses")

deck = Deck(52)

user = Player("PlayerName")


#Main variables and lists
hand = []
playing = []


#Shows what cards are in hand and which are being played.
def show_cards():
	print("")
	print("Score: " + str(Player.score))
	print("Dice: " + str(Player.dice))
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
			if Player.dice >= 1:
				Player.dice -= 1
				for i in range(random.randrange(1, 7)):
					new_card = Deck.draw_card()
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
	if Hands.calculate_flush(playing) == True:
		if Hands.calculate_straight(playing) == True:
			straight_flush.process_hand()
		else:
			flush.process_hand()
	elif Hands.calculate_kinds(playing) == 4:
		four_of_a_kind.process_hand()
	elif Hands.calculate_full_house(playing) == True:
		full_house.process_hand()
	elif Hands.calculate_straight(playing) == True:
		straight.process_hand()
	elif Hands.calculate_kinds(playing) == 3:
		three_of_a_kind.process_hand()
	elif Hands.calculate_pairs(playing) == 2:
		two_pair.process_hand()
	elif Hands.calculate_pairs(playing) == 1:
		pair.process_hand()
	else:
		high_card.process_hand()
	for i in range (len(playing)):
		Player.score = Player.score + playing[i].point_value
	playing.clear()
	show_cards()
	return


#Plays the card the player chose
def process(play_cards):
	playing.append(hand[int(play_cards) - 1])
	hand.remove(hand[int(play_cards) - 1])
	show_cards()
	return


def main():
	for i in range(8):
		new_card = Deck.draw_card()
		hand.append(new_card)
	show_cards()
	return


if __name__ == "__main__":
	print(user)
	print(deck)
	main()