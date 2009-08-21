class IsPrime():
	primes = []
	def __init__(self):
		self.primes = [2,3]
	def __call__(self, n):
		if self.primes.count(n) != 0: return True
		while self.primes[-1]**2 < n:
			newprimes = range(0,self.primes[-1]**2)
			for prime in self.primes:
				newprimes[prime::prime] = [0 for i in newprimes[prime::prime]]
			l = len(self.primes)
			self.primes[l:l] = [i for i in newprimes[self.primes[-1]+1:] if i != 0]
		if self.primes[-1]**2 >= n:
			for prime in self.primes:
				if n%prime == 0: return False
				if prime**2 > n: break
			return True
