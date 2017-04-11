from time import sleep
import random
#from deck import deck 

class Character(object):

	def __init__(self):
		self.hand = []

	def draw_card(self, face):
		raise NotImplementedError

class Player(Character):

	def __init__(self):
		super(Player, self).__init__()

	#def draw_card(self):		
	#	card = random.choice(deck.keys())
	#	value = deck[card]
	#	self.hand[card] = value
	#	del deck[card]
	def draw_card(self):		
		card = deck1.deck.pop()
		self.hand.append(card) 
		print self.hand

class Dealer(Character):

	def __init__(self):
		super(Dealer, self).__init__()

	def draw_card(self, face):
		if face == 'up':
			card = deck1.deck.pop()
			self.hand.append(card) 
			print self.hand
			print card
		elif face == 'down':
			card = deck1.deck.pop()
			self.hand.append(card) 

class CardDeck(object):

	def __init__(self):
		self.deck = []

	def new_deck(self):
		suits = ['Heart','Club','Spade','Diamond']
		cards = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
		for i in suits:
			for x in cards:
				self.deck.append("[" + i + "] " + x)
		random.shuffle(self.deck)
		print self.deck

	def calculate_value(self, card):
		print card
		if "2" in card:
			return 2
		elif "3" in card:
			return 3
		elif "4" in card:
			return 4
		elif "5" in card:
			return 5
		elif "6" in card:
			return 6
		elif "7" in card:
			return 7
		elif "8" in card:
			return 8
		elif "9" in card:
			return 9
		elif "10" in card:
			return 10
		elif "Jack" in card:
			return 10
		elif "Queen" in card:
			return 10
		elif "King" in card:
			return 10
		elif "Ace" in card:
			return 11

	def hand_value(self, hand):
		value = 0
		for i in hand:
			value += self.calculate_value(i)
		print value



def game(deck1, dealer, player):
	deck1.new_deck()
	deck1.hand_value(player.hand)
	deck1.calculate_value('[Diamond] 9')
	player.draw_card()
	dealer.draw_card("up")
	deck1.hand_value(player.hand)
	print player.hand
	print deck1.deck

if __name__ == '__main__':
	deck1 = CardDeck()
	dealer = Dealer()
	player = Player()
	game(deck1, dealer, player)