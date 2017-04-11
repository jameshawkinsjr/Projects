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

	def draw_card(self, deck2, to_print):		
		card = deck2.deck.pop()
		self.hand.append(card) 
		if to_print == 1:
			print "Card Drawn: " + card

	def wallet(self, money):
		self.money = money
		return money

class Dealer(Character):

	def __init__(self):
		super(Dealer, self).__init__()

	def draw_card(self, deck2, face, to_print):
		if face == 'up':
			card = deck2.deck.pop()
			self.hand.append(card) 
			if to_print == 1:
				print "Card Drawn: " + card
		elif face == 'down':
			card = deck2.deck.pop()
			self.hand.append(card)
			if to_print == 1:
				print "Card Drawn: " + card

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

	def calculate_value(self, card):
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
		return value

def print_table(player, dealer, deck1, hidden, money, wager):
	print "=" * 40
	print "\n"
	print "Bank: $%d" % player.wallet(money)
	print "Wager: $%s" % wager
	print "\n"
	print "Dealer's Hand (" + str(deck1.hand_value(dealer.hand)) + "):"
	for i in dealer.hand:
		if i == dealer.hand[0] and hidden is True:
			print "\t> [Face Down]"
		else:
			print "\t> " + i
	print "\n"
	print "Player's Hand (" + str(deck1.hand_value(player.hand)) + "):"
	for i in player.hand:
		print "\t> " + i
	print "\n"
	print "=" * 40
	print "\n"


def game(player, dealer, money):
	deck1 = CardDeck()
	deck1.new_deck()
	print "\n"
	print "*" * 60
	print "\n"
	print "\tStarting a new round"
	print "\n"
	print "\tBank: $%d" % player.wallet(money)
	print "\n"
	print "*" * 60
	print "\n"
	
	while True:
		wager = raw_input("How much would you like to wager? $")
		if (wager.isdigit() is False) or (wager <= 0):
			print "Error. Please try again.\n"
		elif int(wager) > player.wallet(money):
			print "You don't have enough to wager $%s\n" % wager
		else:
			print "You've wagered $%s\n" % wager
			money -= int(wager)
			break


	# Game Loop
	if len(player.hand) < 2 and len(dealer.hand) < 2:
		print "Dealing...\n"
		sleep(1)
		dealer.draw_card(deck1, 'down', 0)
		dealer.draw_card(deck1, 'down', 0)
		player.draw_card(deck1, 0)
		player.draw_card(deck1, 0)
		print_table(player, dealer, deck1, True, money, wager)		
		if deck1.hand_value(player.hand) == 21:
			print "Blackjack! You win!"
			play_again(money, wager, "win")
		
	while True and deck1.hand_value(player.hand) <= 21 and deck1.hand_value(dealer.hand) <= 21:
		action = raw_input("\nHit or Stay? > ")
		print "\n"
		
		if action.lower() == 'hit':
			sleep(1)
			print "Player hits\n"
			player.draw_card(deck1, 1)
			print_table(player, dealer, deck1, True, money, wager)

		elif action.lower() == 'stay':
			print "*" * 40
			print "\n"
			print "\tPlayer Stays"
			print "\n"
			print "*" * 40
			print "\n"
			sleep(1)
			break
		else:
			print "Try Again"
	while True and deck1.hand_value(dealer.hand) <= 21 and deck1.hand_value(player.hand) <= 21:
		if deck1.hand_value(dealer.hand) < 17:
			sleep(1)
			print "*" * 40
			print "\n"
			print "\tThe Dealer Hits"
			print "\n"
			print "*" * 40
			print "\n"
			sleep(1)
			dealer.draw_card(deck1, 'up', 1)
			print "\n"
			print_table(player, dealer, deck1, True, money, wager)
			sleep(1)
		elif deck1.hand_value(dealer.hand) > 21:
			break
		else:
			print "*" * 40
			print "\n"
			print "\tThe Dealer Stays"
			print "\n"
			print "*" * 40
			sleep(1)
			break
	
	print_table(player, dealer, deck1, False, money, wager)

	if deck1.hand_value(player.hand) == deck1.hand_value(dealer.hand) <= 21:
		print "Push!"
		play_again(money, wager, "push")
	elif deck1.hand_value(player.hand) > 21 and deck1.hand_value(dealer.hand) <= 21:
		print "You busted"
		play_again(money, wager, "lose")
	elif deck1.hand_value(dealer.hand) > 21 and deck1.hand_value(player.hand) <= 21:
		print "The dealer busted. You win!"
		play_again(money, wager, "win")
	else:
		if deck1.hand_value(player.hand) > deck1.hand_value(dealer.hand):
			print "You win!"
			play_again(money, wager, "win")
		else:
			print "You lose!"
			play_again(money, wager, "lose")

def play_again(money, wager, state):
	if state == 'win':
		money += (int(wager) * 2)
	elif state == 'lose':
		pass
	else:
		money += (int(wager))
	if money <= 0:
		print "You ran out of money!"
		exit()
	option = raw_input("Play Again? ")
	if option.lower() == 'y':
		main(money)
	else:
		exit()

def main(money):
	dealer = Dealer()
	player = Player()
	player.wallet(money)
	game(player, dealer,money)

if __name__ == '__main__':
	main(500)
	

