from utils import IsPrime

def primeFactors(n):
	"""Find the prime factors of an integer n.

	For example, the prime factors of 12 are
	2, 2, and 3.
	"""

	# initialize list of prime factors and IsPrime object
	facts = []
	isPrime = IsPrime()

	# ensure list of known primes is long enough to state whether
	# n is prime or compound
	isPrime.extend(n)

	# divide by factors until none remain
	for prime in isPrime.primes:
		while n % prime == 0:
			facts.append(prime)
			n /= prime

		if n == 1:
			break

	return facts


def properFactors(n):
	"""Find the proper factors of an integer n.

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
	raise NotImplementedError("properFactors is not yet implemented.")


def isAbundant(n):
	"""A number n is abundant if the sum of its proper factors
	is greater than the number itself.

	For example, 12 is abundant because 1 + 2 + 3 + 4 + 6 = 16,
	and 16 > 12.
	"""

	return properFactors(n) > n


def isPerfect(n):
	"""A number n is perfect if the sum of its proper factors
	is exactly equal to the number itself.

	For example, 6 is perfect because 1 + 2 + 3 = 6.
	"""

	return properFactors(n) == n


def isDeficient(n):
	"""A number n is deficient if the sum of its proper factors
	is less than the number itself.

	For example, 15 is deficient because 1 + 3 + 5 = 8,
	and 8 < 15.
	"""

	return properFactors(n) < n


def abundantSum(n):
	"""Return True if a number n can be expressed as the sum of two
	abundant numbers, False otherwise.

	"""

	raise NotImplementedError("abundantSum is not yet implemented.")


if __name__ == "__main__":
	print sum([i for i in xrange(28124) if not abundantSum(i)])
