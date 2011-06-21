from utils import is_prime
upperbound = 2000000
is_prime.extend(upperbound**2)
print sum([i for i in is_prime.primes if i < upperbound])
