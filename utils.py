from math import sqrt
from array import array

# TODO: refactor class - change name to PrimeUtils; add more convenience funcs.
# TODO: convenience func - next_prime().
class IsPrime():
	"""Determine whether a given number is prime or compound.

	Uses the sieve method of finding primes.
	"""

	primes = []

	def __init__(self):
		self.primes = [2,3]

	def __call__(self, n):
		"""Return True if n is prime; False otherwise."""

		# check if the input is a natural number
		if n <= 1: return False
		if int(n) != n: return False

		# check if the input is a known prime
		if self.primes.count(n) != 0: return True

		# maybe one of the known primes is a factor
		initnumprimes = len(self.primes)
		for prime in self.primes: 
			if n%prime == 0: return False
			if prime**2 > n: return True

		# self.primes is too short to state yet that n is compound;
		# in this case, extend self.primes.  self.primes has to extend to
		# at least the square root of n.
		self.extend(sqrt(n))

		# now we know that we have a large enough prime to check if n is composite
		# but we've already checked some, so check the rest as necessary.
		for prime in self.primes[initnumprimes:]:
			if n%prime == 0: return False
			if prime**2 > n: return True

	def extend(self, n):
		"""Extend the list of known primes to at least n."""
		# TODO: This is broken for big numbers (cf. Problem010.py) - fix it.

		# Depending on what the last currently-known prime is, we may get bonus
		# primes AT NO EXTRA COST!!1!one
		while self.primes[-1] < n:
			# index all integers up until and including the largest we
			# can currently check definitively.
			newprimes = range(0, self.primes[-1] ** 2)

			# turn off all numbers that are multiples of known primes.
			for prime in self.primes:
				newprimes[prime::prime] = [0 for i in newprimes[prime::prime]]

			# and, lastly, append the remaining (prime) numbers to self.primes
			l = len(self.primes)
			self.primes.extend([i for i in newprimes[self.primes[-1]+1:] if i != 0])

# Convenience instance of IsPrime() suitable for importing like a function.
is_prime = IsPrime()

def isPalindrome(obj):
	"""Determine whether a given object is palindromic or not."""
	return str(obj) == str(obj)[::-1]

def toBase10(num):
	"""Represent an integer in base ten, as a string."""
	return str(int(num))

def toBase2(num):
	"""Represent an integer in base two, as a string."""
	return "{0:b}".format(int(num))

def fib(n):
	"""Find the nth Fibonacci number."""
	if (n < 1): return 0
	if (n == 1 or n == 2): return n
	thisfib = 0
	i = 3
	prevprev = 1
	prev = 2
	while (i <= n):
		thisfib = prevprev + prev
		prevprev = prev
		prev = thisfib
		i = i + 1
	return thisfib

def factorize(n):
	i=1
	factors = array('L')
	while i*i <= n:
		if n%i == 0:
			factors.append(i)
		i += 1
	if factors[-1]**2 == n:
		for i in factors[-2::-1]:
			factors.append(n/i)
	else:
		for i in factors[-1::-1]:
			factors.append(n/i)
	return factors

def memoize(fn):
	cache = dict()

	def newfn(*args):
		try:
			return cache[args]
		except KeyError:
			cache[args] = fn(*args)
			return cache[args]
		except TypeError:
			# args is unhashable.
			return fn(*args)

	return newfn
