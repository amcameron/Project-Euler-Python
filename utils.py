class IsPrime():
	primes = []
	def __init__(self):
		self.primes = [2,3]
	def __call__(self, n):
		if self.primes.count(n) != 0: return True
		while self.primes[-1]**2 < n:
			i = len(self.primes)
			self.primes[i:i] = [j for j in xrange(self.primes[-1]+2,self.primes[-1]**2,2) if [j%prime for prime in self.primes].count(0)==0]
		
		if [n%prime for prime in self.primes].count(0) != 0:
			return False
		else: return True
