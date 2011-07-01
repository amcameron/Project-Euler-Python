"""Find the least number for which the proportion of bouncy numbers is exactly
99%."""

def isIncreasing(num):
	last = 0
	for d in str(num):
		if int(d) < last:
			return False
		else:
			last = int(d)

	return True

def isDecreasing(num):
	last = 9
	for d in str(num):
		if int(d) > last:
			return False
		else:
			last = int(d)

	return True

def isBouncy(num):
	return not isIncreasing(num) and not isDecreasing(num)

if __name__ == '__main__':
	numBouncy = 0
	i = 1
	while (numBouncy*100 != i*99):
		i += 1
		if (isBouncy(i)):
			numBouncy += 1
	
	print i
