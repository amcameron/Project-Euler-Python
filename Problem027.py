from utils import IsPrime

is_prime = IsPrime()

quad = lambda n, a, b: n**2 + a*n + b

def prime_series_length(a, b):
	"""Find the number of primes for consecutive n, starting with n=0,
	for quad(n, a, b)."""
	n = 0
	while is_prime(quad(n, a, b)):
		n += 1
	return n

longest_series = 40
best_a = 1
best_b = 41

for a in xrange(-999, 1000):
	for b in xrange(-999, 1000):
		length = prime_series_length(a, b)
		if length > longest_series:
			print "New longest series:"
			print length, a, b
			longest_series, best_a, best_b = length, a, b

print "Longest series: ", longest_series
print "a, b: ", best_a, best_b
print "a*b: ", best_a*best_b
