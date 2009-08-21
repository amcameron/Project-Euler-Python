upperbound = 2000000
mylist = range(0,upperbound)
mylist[1] = 0
for i in mylist:
	if i != 0:
		for j in xrange(2*i, upperbound, i):
			mylist[j] = 0

print sum(mylist)
