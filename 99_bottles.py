import time 

def main():
	i = 99
	while i > 0:
		if i != 1:
			print "%d bottles of beer on the wall, %d bottles of beer." % (i, i)
			print "Take one down, pass it around, %d bottles of beer on the wall" % (i -1)
			print "\n"
			i -= 1
		else:
			print "%d bottle of beer on the wall, %d bottle of beer." % (i, i)
			print "Take one down, pass it around, %d bottles of beer on the wall" % (i -1)
			print "\n"
			i -= 1

main()