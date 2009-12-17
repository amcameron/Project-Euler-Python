class IsPrime():
	"""Determine whether a given number is prime or compound.

	Uses the sieve method of finding primes.
	"""

	primes = []

	def __init__(self):
		self.primes = [2,3]

	def __call__(self, n):
		"""Return true if n is prime; false otherwise."""

		# if n is already in the list of known primes, it is prime.
		if self.primes.count(n) != 0: return True

		# self.primes may yet be too short to state that n is compound;
		# in this case, extend self.primes.  self.primes has to extend to
		# at least the square root of n.
		while self.primes[-1] ** 2 < n:
			# index all integers up until and including the largest we
			# can currently check definitively.
			newprimes = range(0, self.primes[-1] ** 2)

			# turn off all numbers that are multiples of known primes.
			for prime in self.primes:
				newprimes[prime::prime] = [0 for i in newprimes[prime::prime]]

			# and, lastly, append the remaining (prime) numbers to self.primes
			l = len(self.primes)
			self.primes.extend([i for i in newprimes[self.primes[-1]+1:] if i != 0])

		# this if statement is pretty much implied by the previous while loop.
		# anyway; we now have enough primes to know for sure if n is compound or not.
		if self.primes[-1] ** 2 >= n:
			for prime in self.primes:
				if n%prime == 0: return False
				if prime ** 2 > n: break
			return True

	def extend(self, n):
		"""Extend the list of known primes to at least n."""

		# If n is prime, calling self with n**2 will ensure n is in self.primes.
		# Depending on what the last currently-known prime is, we may get bonus
		# primes AT NO EXTRA COST!!1!one
		self(n**2)

