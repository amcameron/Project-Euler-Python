import utils
upperbound = 2000000
isPrime = utils.IsPrime()
isPrime(upperbound**2) #guarantees isPrime.primes has all primes <= upperbound
print sum([i for i in isPrime.primes if i < upperbound])
