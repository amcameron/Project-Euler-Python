from datetime import date

total = 0
for year in xrange(1901, 2001):
	for month in xrange(1, 13):
		if date(year, month, 1).weekday() == 6:
			total += 1

print total

# Fun with listcomps:
#print len([date(y,m,1) for y in xrange(1901, 2001)
#		for m in xrange(1, 13) if date(y,m,1).weekday()==6])
