from math import *
def isprime(n):
	i = 2
	while (i <= sqrt(n)):
		if (n % i == 0): return 0
		else: i = i + 1
	return 1

n = 600851475143
i = 2
nisprime = isprime(n)
while (nisprime == 0):
	if (n % i == 0):
		n = n/i
		i = 2
		nisprime = isprime(n)
	else:
		i = i + 1
print n