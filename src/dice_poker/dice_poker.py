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
	def getValue(self):
		return self.rank
	def getSuit(self):
		return self.suit
	def __str__(self):
		return "This card is a " + self.name + " worth " + str(self.point_value)

cards =	{
  "2s": ("spade", "2", 2, "2 of Spades"),
  "3s": ("spade", "3", 3, "3 of Spades"),
  "4s": ("spade", "4", 4, "4 of Spades"),
  "5s": ("spade", "5", 5, "5 of Spades"),
  "6s": ("spade", "6", 6, "6 of Spades"),
  "7s": ("spade", "7", 7, "7 of Spades"),
  "8s": ("spade", "8", 8, "8 of Spades"),
  "9s": ("spade", "9", 9, "9 of Spades"),
  "10s": ("spade", "10", 10, "10 of Spades"),
  "js": ("spade", "jack", 11, "Jack of Spades"),
  "qs": ("spade", "queen", 12, "Queen of Spades"),
  "ks": ("spade", "king", 13, "King of Spades"),
  "as": ("spade", "ace", 14, "Ace of Spades"),
  "2c": ("club", "2", 2, "2 of Clubs"),
  "3c": ("club", "3", 3, "3 of Clubs"),
  "4c": ("club", "4", 4, "4 of Clubs"),
  "5c": ("club", "5", 5, "5 of Clubs"),
  "6c": ("club", "6", 6, "6 of Clubs"),
  "7c": ("club", "7", 7, "7 of Clubs"),
  "8c": ("club", "8", 8, "8 of Clubs"),
  "9c": ("club", "9", 9, "9 of Clubs"),
  "10c": ("club", "10", 10, "10 of Clubs"),
  "jc": ("club", "jack", 11, "Jack of Clubs"),
  "qc": ("club", "queen", 12, "Queen of Clubs"),
  "kc": ("club", "king", 13, "King of Clubs"),
  "ac": ("club", "ace", 14, "Ace of Clubs"),
  "2d": ("diamond", "2", 2, "2 of Diamonds"),
  "3d": ("diamond", "3", 3, "3 of Diamonds"),
  "4d": ("diamond", "4", 4, "4 of Diamonds"),
  "5d": ("diamond", "5", 5, "5 of Diamonds"),
  "6d": ("diamond", "6", 6, "6 of Diamonds"),
  "7d": ("diamond", "7", 7, "7 of Diamonds"),
  "8d": ("diamond", "8", 8, "8 of Diamonds"),
  "9d": ("diamond", "9", 9, "9 of Diamonds"),
  "10d": ("diamond", "10", 10, "10 of Diamonds"),
  "jd": ("diamond", "jack", 11, "Jack of Diamonds"),
  "qd": ("diamond", "queen", 12, "Queen of Diamonds"),
  "kd": ("diamond", "king", 13, "King of Diamonds"),
  "ad": ("diamond", "ace", 14, "Ace of Diamonds"),
  "2h": ("heart", "2", 2, "2 of Hearts"),
  "3h": ("heart", "3", 3, "3 of Hearts"),
  "4h": ("heart", "4", 4, "4 of Hearts"),
  "5h": ("heart", "5", 5, "5 of Hearts"),
  "6h": ("heart", "6", 6, "6 of Hearts"),
  "7h": ("heart", "7", 7, "7 of Hearts"),
  "8h": ("heart", "8", 8, "8 of Hearts"),
  "9h": ("heart", "9", 9, "9 of Hearts"),
  "10h": ("heart", "10", 10, "10 of Hearts"),
  "jh": ("heart", "jack", 11, "Jack of Hearts"),
  "qh": ("heart", "queen", 12, "Queen of Hearts"),
  "kh": ("heart", "king", 13, "King of Hearts"),
  "ah": ("heart", "ace", 14, "Ace of Hearts"),
}

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



hand = []

def draw_cards(number):
	cardID = random.randrange(0, 51)
	drawCard = str(cardID)
	cardList = list(cardsIndex[cardID])

	newCard = Card(cardsIndex[drawCard])

def main():
	draw_cards(1)


if __name__ == "__main__":
    main()