factors = []

def factor(number):
	for i in range(1,number+1):
		if number % i == 0:
			factors.append(i)
		else:
			pass


def game():
	print "Welcome - please enter a number"
	number = int(raw_input("> "))
	factor(number)
	print factors

game()