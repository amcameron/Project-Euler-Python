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
		self.primeList = [2, 3]
		self.primes = set(self.primeList)

	def __call__(self, n):
		"""Return True if n is prime; False otherwise."""

		# check if the input is a natural number
		if n <= 1:
			return False
		if int(n) != n:
			return False

		self.extend(n)
		if n in self.primes:
			return True
		else:
			return False

	def extend(self, n):
		"""Extend the list of known primes to at least n."""
		# TODO: This is broken for big numbers (cf. Problem010.py) - fix it.

		# Depending on what the last currently-known prime is, we may get bonus
		# primes AT NO EXTRA COST!!1!one
		while self.primeList[-1] < n:
			# index all integers up until and including the largest we
			# can currently check definitively.
			newprimes = range(0, self.primeList[-1] ** 2)

			# turn off all numbers that are multiples of known primes.
			for prime in self.primeList:
				newprimes[prime::prime] = [False for i in newprimes[prime::prime]]

			# and, lastly, append the remaining (prime) numbers to self.primes
			l = len(self.primeList)
			self.primeList.extend([i for i in newprimes[self.primeList[-1]+1:] if i])
			self.primes |= set(self.primeList)

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
