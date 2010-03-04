total = 1
for i in xrange(2, 502):
	thisSquare = (2*i - 1)**2
	total += thisSquare + thisSquare - 2*(i-1) + thisSquare - 4*(i-1) \
			+ thisSquare - 6*(i-1)

print total
