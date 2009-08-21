from math import *
def fib(n):
	if (n < 1): return 0
	if (n == 1 or n == 2): return n
	thisfib = 0
	i = 3
	prevprev = 1
	prev = 2
	while (i <= n):
		thisfib = prevprev + prev
		prevprev = prev
		prev = thisfib
		i = i + 1
	return thisfib

total = 0
n = 1
thisfib = fib(n)
while(thisfib <= 4000000):
	if (thisfib % 2 == 0): total = total + thisfib
	n = n + 1
	thisfib = fib(n)
print total