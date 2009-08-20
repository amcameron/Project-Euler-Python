import math
a = b = c = 1
while True:
	a += 1
	b = a
	while a + b + c <= 1000:
		b += 1
		c = int(math.sqrt(a*a + b*b))
		if c*c != a*a + b*b: continue
		else:	#i.e. if a*a + b*b == c*c
			if a+b+c == 1000: break
	if c*c != a*a + b*b: continue
	else:
		if a+b+c == 1000: break

print 'a=',a,' b=',b,' c=',c,' a+b+c=',a+b+c,' abc=',a*b*c
