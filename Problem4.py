def ispalindrome(n):
	return str(n)==str(n)[::-1]

curbest = 0
for i in range(1000,0,-1):
	for j in range(1000,i,-1):
		if (ispalindrome(i*j) and i*j > curbest): curbest = i*j
print curbest	
