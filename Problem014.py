def collatz(n):
	if n%2 == 0:
		return n/2
	else:
		return 3*n+1

curbestlen = curbeststart = 0
for i in xrange(500001,1000000):
	n = i
	l = 1
	while n != 1:
		n = collatz(n)
		l += 1
	if l > curbestlen:
		curbestlen = l
		curbeststart = i

print curbeststart, "produces a sequence of length", curbestlen
