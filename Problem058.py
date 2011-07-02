"""Find the side length of the square spiral for which the ratio of primes
along both diagonals first falls below 10%."""
from utils import is_prime

if __name__ == '__main__':
	i = 3
	side_length = 2
	diags = [1, 3, 5, 7, 9]
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
