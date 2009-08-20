print [(a,b,(1000-a-b)) for b in xrange(1,500) for a in xrange(1,b) if a**2 + b**2 == (1000-a-b)**2]
