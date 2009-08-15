from math import *
def ispalindrome(n):
	nstr = str(n)
	for i in range(int(len(nstr)/2)):
		if (nstr[i] != nstr[len(nstr) - i - 1]): return 0
	return 1

curbest = 0
for i in range(1000,0,-1):
	for j in range(1000,i,-1):
		if (ispalindrome(i*j) == 1 and i*j > curbest): curbest = i*j
print curbest	
