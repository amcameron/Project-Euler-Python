"""Find the number of circular primes below one million."""

from utils import is_prime

def isCircularPrime(num):
	"""A prime is circular if all rotations of its digits are also prime
	numbers, e.g. 197, 971, and 719."""
	return all(is_prime(i) for i in rotations(num))

def rotations(num):
	"""Return a list of all possible rotations of the given number."""
	num = str(num)
	l = len(num)
	return [int(num[i:] + num[:i]) for i in xrange(l)]

if __name__ == '__main__':
	print len([i for i in xrange(1000000) if isCircularPrime(i)])
