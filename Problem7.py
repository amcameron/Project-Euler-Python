def nextprime(n):
	if n%2 == 0: i = n + 1
	else: i = n + 2

	while not isprime(i): i += 2
	return i


def isprime(n):
	i = 2
	while (i <= sqrt(n)):
		if (n % i == 0): return 0
		else: i = i + 1
	return 1


