from random import randint
from time import sleep

def response():

	responses = [
			'It is certain',
			'It is decidedly so',
			'Without a doubt',
			'Yes definitely',
			'You may rely on it',
			'As I see it, yes',
			'Most likely',
			'Outlook good',
			'Yes',
			'Signs point to yes',
			'Reply hazy try again',
			'Ask again later',
			'Better not tell you now',
			'Cannot predict now',
			'Concentrate and ask again',
			'Don\'t count on it',
			'My reply is... no',
			'My sources say... no',
			'Outlook not so good',
			'... Very doubtful'
		]

	print "8-Ball: " + responses[randint(0, len(responses)-1)]

def user_input():
	print "What is your question?"
	question = raw_input("> ")
	sleep(1)
	print "\n8-ball: thinking...\n"
	sleep(1)
	response()
	print "\n"
	print "Would you like to ask another question? Y/N"
	another_question = raw_input("> ")
	if another_question.lower() == "y":
		print "\n"
		user_input()
	else:
		print "\nThanks for playing!\n"
		exit()

user_input()

