"""Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2."""

def isPalindrome(string):
	"""Determine whether a given string is palindromic or not."""
	return string == string[::-1]

def toBase10String(integer):
	"""Represent an integer in base ten, as a string."""
	return str(integer)

def toBase2String(integer):
	"""Represent an integer in base two, as a string."""
	return "{0:b}".format(integer)

def predicate(integer):
	"""Return true if the integer is palindromic in both base 10 and base 2."""
	return isPalindrome(toBase2String(integer)) and \
		isPalindrome(toBase10String(integer))

if __name__ == '__main__':
	print sum(i for i in xrange(1000000) if predicate(i))
