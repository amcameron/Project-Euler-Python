"""Find the side length of the square spiral for which the ratio of primes
along both diagonals first falls below 10%."""
from utils import is_prime, memoize

def get_diagonals(side_length):
	"""Return the diagonals of a square spiral.
	
	int -> array of ints
	For a square spiral of the given side length, return an array containing
	all the elements along both diagonals."""

	if side_length < 1:
		raise ValueError

	diags = [1]
	i = 1
	for i in xrange(3, side_length + 1, 2):
		# 1, 3, 5, 7, 9, 13, 17, 21, 25, 31, 37, 43, 49, ...
		isquared = i**2
		diags.extend([isquared - 3*i + 3, isquared - 2*i + 2, isquared - i + 1,
			isquared])

	return diags

if __name__ == '__main__':
	i = 3
	side_length = 2
	diags = get_diagonals(i)
	num_elems = len(diags)
	num_primes = sum(1 for i in diags if is_prime(i))

	while float(num_primes)/num_elems > 0.10:
		i += 2
		new_diags = [i*i - i + 1, i*i - 2*i + 2, i*i - 3*i + 3]
		num_elems += 4
		num_primes += sum(1 for i in new_diags if is_prime(i))

	print "i: ", i
	print "proportion of primes: ", float(num_primes)/num_elems
	print "number of primes found: ", len(is_prime.primes)
	print "max prime: ", is_prime.primes[-1]
