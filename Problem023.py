from utils import IsPrime
from itertools import combinations

_isPrime = IsPrime()

def primeFactors(n):
	"""Find the list of prime factors of an integer n.

	For example, the prime factors of 12 are
	2, 2, and 3.

	Factors are returned in a monotonic increasing list.
	For example, primeFactors(12) will never return
	[2, 3, 2] or [3, 2, 2].
	"""

	if int(n) != n:
		raise TypeError("cannot find the factors of a non-integer.")
	if n < 1:
		raise ValueError("cannot find the factors of a non-positive integer.")

	# initialize list of prime factors and IsPrime object
	facts = []

	# ensure list of known primes is long enough to state whether
	# n is prime or compound
	_isPrime.extend(n)

	# divide by factors until none remain
	for prime in _isPrime.primes:
		while n % prime == 0:
			facts.append(prime)
			n /= prime

		if n == 1:
			break

	return facts


def properFactors(n):
	"""Find the set of proper factors of an integer n.

	For example, the proper factors of 12 are
	1, 2, 3, 4, and 6.
	"""

	# The proper factors of a number can be found by taking
	# the product of all unique combinations of its prime factors,
	# except for all of the prime factors (this just yields the number).
	# For example, the prime factorization of 12 yiels [2, 2, 3].
	# The possible combinations are:
	# [2, 2, 3] nCr 0: []
	# [2, 2, 3] nCr 1: [2, 3]
	# [2, 2, 3] nCr 2: [[2, 2], [2, 3]]
	# [2, 2, 3] nCr 3: not included, because prod([2, 2, 3]) = 12.
	# The products of these are [1], [2, 3], and [4, 6], respectively.
	# Therefore, the proper factors of 12 are [1, 2, 3, 4, 6].
	primeFacts = primeFactors(n)
	properFacts = set()

	# Iterate over the number of combinations to take (that is, the
	# r in "nCr"), but don't take the combination of ALL prime
	# factors. (Do take the combination of NONE of them: 1 is
	# always a proper factor.)
	for i in xrange(len(primeFacts)):
		# Find all combinations of i elements, and take the products
		# of each of these combinations.  We might end up with
		# duplicates, so use set() to remove them.  Then add them
		# to the list of proper factors!
		properFacts.update(map(_product, combinations(primeFacts, i)))

	return properFacts


def _product(seq):
	"""Find the product of all elements in a sequence.

	The product of an empty sequence is the multiplicative
	identity: 1.
	"""

	# Make sure the sequence can behave like a list
	# (so that we can pop it)
	seq = list(seq)
	if len(seq) == 0:
		return 1
	else:
		return seq.pop() * _product(seq)


def isAbundant(n):
	"""A number n is abundant if the sum of its proper factors
	is greater than the number itself.

	For example, 12 is abundant because 1 + 2 + 3 + 4 + 6 = 16,
	and 16 > 12.
	"""

	return sum(properFactors(n)) > n


def isPerfect(n):
	"""A number n is perfect if the sum of its proper factors
	is exactly equal to the number itself.

	For example, 6 is perfect because 1 + 2 + 3 = 6.
	"""

	return sum(properFactors(n)) == n


def isDeficient(n):
	"""A number n is deficient if the sum of its proper factors
	is less than the number itself.

	For example, 15 is deficient because 1 + 3 + 5 = 8,
	and 8 < 15.
	"""

	return sum(properFactors(n)) < n


class abundantSum:
	"""Return True if a number n can be expressed as the sum of two
	abundant numbers, False otherwise.

	"""

	def __init__(self):
		self.abundants = [12]
		self.sums = set([24])

	def __call__(self, n):
		if self.abundants[-1] < n:
			self.extend(n)

		return n in self.sums

	def extend(self, n):
		self.abundants.extend(num
			for num in xrange(self.abundants[-1] + 1, n + 1)
			if isAbundant(num))
		self.sums = set(map(sum, combinations(self.abundants, 2)))
		self.sums.update(2*num for num in self.abundants)


if __name__ == "__main__":
	a = abundantSum()
	a.extend(28124)
	print sum(filter(lambda num: not a(num), xrange(1, 28124)))
