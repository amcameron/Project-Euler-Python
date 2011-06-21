from utils import is_prime

def nextprime(n):
	if n%2 == 0: i = n + 1
	else: i = n + 2

	while not is_prime(i): i += 2
	return i

curprime = 1
for i in xrange(1,10001):
	curprime = nextprime(curprime)

print curprime
