"""Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2."""

from utils import isPalindrome, toBase10, toBase2

def predicate(integer):
	"""Return true if the integer is palindromic in both base 10 and base 2."""
	return isPalindrome(toBase2String(integer)) and \
		isPalindrome(toBase10String(integer))

if __name__ == '__main__':
	print sum(i for i in xrange(1000000) if predicate(i))
