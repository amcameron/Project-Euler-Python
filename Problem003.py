import utils
isprime = utils.IsPrime()
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
