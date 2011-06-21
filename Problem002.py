from utils import fib

total = 0
n = 1
thisfib = fib(n)
while(thisfib <= 4000000):
	if (thisfib % 2 == 0): total = total + thisfib
	n = n + 1
	thisfib = fib(n)
print total
