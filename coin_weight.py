from time import sleep

def pennies(weight):
	count = (weight/(126/50)) 
	return count

def nickels(weight):
	count = (weight/(199/40)) 
	return count

def dimes(weight):
	count = (weight/(113/50)) 
	return count

def quarters(weight):
	count = (weight/(226/40)) 
	return count

def calcuation():
	print "Welcome to the coin calculator!"
	print "What is the weight of the pennies you have?"
	numpennies = pennies(float(raw_input("> ")))
	print "What is the weight of the nickels you have?"
	numnickels = float(raw_input("> "))
	print "What is the weight of the dimes you have?"
	numdimes = float(raw_input("> "))
	print "What is the weight of the quarters you have?"
	numquarters = float(raw_input("> "))
	sleep(1)
	print "\nThinking...\n"
	sleep(1)
	number_of_coins = numpennies + numnickels + numdimes + numquarters
	print "You have %d total coins" % number_of_coins
	print "You have %d pennies and would need %d penny holders" % (numpennies, numpennies/50)
	print "You have %d nickels and would need %d nickel holders" % (numnickels, numnickels/40)
	print "You have %d dimes and would need %d dime holders" % (numdimes, numdimes/50)
	print "You have %d quarters and would need %d quarter holders" % (numquarters, numquarters/40)
	print "You have $%d total" % ((numpennies * .01) + (numnickels * .05) + (numdimes *.1) + (numquarters*.25))


if __name__ == "__main__":
    calcuation()