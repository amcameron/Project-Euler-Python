from math import sqrt

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
