"""
Deck class
by Adam Ainsworth
"""
import random
from Card import Card

class Deck:
	cards_index =   {
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
	suit_index =    {
			"1": ("Spades"),
			"2": ("Diamonds"),
			"3": ("Clubs"),
			"4": ("Hearts")
		}
	def __init__(self, card_amount):
		self.card_amount = card_amount
	
	
	#Returns the amount of cards in the deck
	def __str__(self):
		return ("This deck has " + str(self.card_amount) + " possible card types.")
	

	#Draws a random card out of 52
	def draw_card():
		card_suit_id = random.randrange(1, 5)
		card_value = random.randrange(2, 15)
		card_suit = Deck.suit_index[str(card_suit_id)]
		card_rank = Deck.cards_index[str(card_value)]
		card_name = card_rank + " of " + card_suit

		new_card = Card(card_suit, card_rank, card_value, card_name)
		return new_card


if __name__ == '__main__':
	print("This is the deck class.")