from utils import is_prime

n = 600851475143
i = 2
nisprime = is_prime(n)
while (not nisprime):
	if (n % i == 0):
		n = n/i
		i = 2
		nisprime = is_prime(n)
	else:
		i = i + 1
print n
