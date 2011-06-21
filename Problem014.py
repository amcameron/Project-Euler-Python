def collatz(n):
	if n%2 == 0:
		return n/2
	else:
		return 3*n+1

curbestlen = curbeststart = 0
cache = dict()
for i in xrange(1, 1000000):
	n = i
	l = 1
	while n != 1:
		if cache.get(n) is not None:
			l += cache[n]
			n = 1
		else:
			n = collatz(n)
			l += 1
	cache[i] = l
	if l > curbestlen:
		curbestlen = l
		curbeststart = i

print curbeststart, "produces a sequence of length", curbestlen
