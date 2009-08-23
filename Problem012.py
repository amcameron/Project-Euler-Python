from array import *
def trianglenum(n):
	return n*(n+1)/2
def factorize(n):
	i=1
	factors = array('L')
	while i*i <= n:
		if n%i == 0:
			factors.append(i)
		i += 1
	if factors[-1]**2 == n:
		for i in factors[-2::-1]:
			factors.append(n/i)
	else:
		for i in factors[-1::-1]:
			factors.append(n/i)
	return factors

i = 1
factors = array('L')
while len(factors) <= 500:
	i += 1
	factors = factorize(trianglenum(i))
print trianglenum(i)
