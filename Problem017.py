numberNames = {
	1:"one ",
	2:"two ",
	3:"three ",
	4:"four ",
	5:"five ",
	6:"six ",
	7:"seven ",
	8:"eight ",
	9:"nine ",
	10:"ten ",
	11:"eleven ",
	12:"twelve ",
	13:"thirteen ",
	14:"fourteen ",
	15:"fifteen ",
	16:"sixteen ",
	17:"seventeen ",
	18:"eighteen ",
	19:"nineteen ",
	20:"twenty ",
	30:"thirty ",
	40:"forty ",
	50:"fifty ",
	60:"sixty ",
	70:"seventy ",
	80:"eighty ",
	90:"ninety ",
	100:"hundred ",
	1000:"thousand "
}

def spellnum(n):
	if n > 1000 or n < 1:
		raise ValueError("Number out of range.  "
			"Valid range is 1-1000 (inclusive).")

	keys = numberNames.keys()
	keys.sort(reverse=True)
	numname = ""
	if n <= 20:
		numname += numberNames[n]

	elif n < 100:
		for i in keys:
			if n/i:
				numname += numberNames[i]
				if n-i:
					numname += numberNames[n-i]
				break

	else: # i.e. n >= 100
		for i in keys:
			if n/i:
				numname += numberNames[n/i]
				numname += numberNames[i]

				# eliminate the upper digits using rounding
				n -= n/i * i

				print n
				if n:
					numname += "and " + spellnum(n)

				break

	return numname

if __name__ == "__main__":
	names = ""
	for i in xrange(1,1001):
		names += spellnum(i)
	
	# remove spaces
	#print "".join(names.split())
	print len("".join(names.split()))
