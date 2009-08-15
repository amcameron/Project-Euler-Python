def ispalindrome(n):
	if str(n)==str(n)[::-1] : return 1
	else: return 0

curbest = 0
for i in range(1000,0,-1):
	for j in range(1000,i,-1):
		if (ispalindrome(i*j) == 1 and i*j > curbest): curbest = i*j
print curbest	
