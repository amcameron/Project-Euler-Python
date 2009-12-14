def alphabeticalValue(name):
	total = 0
	for char in name:
		total += ord(char) - 96

	return total

if __name__ == '__main__':
	f = open('names.txt')
	names = f.read().replace('"', '').split(',')
	names.sort()

	total = 0
	for i in xrange(1,len(names)+1):
		total += alphabeticalValue(names[i-1].lower()) * i

	print total
