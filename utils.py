from bisect import bisect_left
from math import sqrt
from array import array

def find_gt(a, x):
	"""Find whether an item greater than or equal to x occurs in a."""
	i = bisect_left(a, x)
	if i != len(a):
		return True
	return False

# TODO: refactor class - change name to PrimeUtils; add more convenience funcs.
# TODO: convenience func - next_prime().
class IsPrime():
	"""Determine whether a given number is prime or compound.

	Uses a fairly naive method for finding primes.
	"""

	primes = []

	def __init__(self):
		self.primes = [2, 3]

	def __call__(self, n):
		"""Return True if n is prime; False otherwise."""

		# check if the input is a natural number
		if n <= 1:
			return False
		if int(n) != n:
			return False

		if not find_gt(self.primes, sqrt(n)):
			self.extend(sqrt(n))

		for prime in self.primes:
			if prime == n:
				return True
			elif n % prime == 0:
				return False
			if prime > sqrt(n):
				return True

	def extend(self, n):
		"""Extend the list of known primes to at least n."""

		lastPrime = self.primes[-1]
		i = lastPrime - (lastPrime % 6) - 6

		while self.primes[-1] <= n:
			i += 6
			if self.__call__(i - 1):
				self.primes.append(i - 1)
			if self.__call__(i + 1):
				self.primes.append(i + 1)

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
