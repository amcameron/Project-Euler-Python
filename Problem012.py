from utils import factorize
from array import array

def trianglenum(n):
	return n*(n+1)/2

i = 1
factors = array('L')
while len(factors) <= 500:
	i += 1
	factors = factorize(trianglenum(i))
print trianglenum(i)
