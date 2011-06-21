"""Find the last ten digits of the non-Mersenne prime: 28433 * 2^7830457 + 1"""

digits = 1
for i in xrange(7830457):
	digits *= 2
	digits = int(str(digits)[-10:])

digits *= 28433
digits += 1
digits = int(str(digits)[-10:])
print digits
