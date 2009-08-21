class IsPrime():
	primes = []
	def __init__(self):
		self.primes = [2]
	def __call__(self, n):
		i = 0
		while (self.primes[i]**2 <= n):
			if (n % self.primes[i] == 0): return False
			else:
				i += 1
				if len(self.primes) == i:
					self.primes[i:i] = [j for j in xrange(self.primes[-1]+1,self.primes[-1]**2) if [j%prime for prime in self.primes].count(0)==0]
		return True
