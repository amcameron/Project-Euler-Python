def propMax(cur, next):
	"""Calculate the maximum route sums for the next
	row in a triangle, given the current one.

	"""

	if len(next) != len(cur) + 1:
		raise IndexError("Next row must have one more"
			"element than current.")

	# Edge case: the only way to reach the first element
	# is from the first element of the previous row.
	next[0] += cur[0]

	# Use the maximum of each of the possible parents of each item.
	# Don't use the first or last elements of next, because they
	# are edge cases.
	for i in range(1, len(next) - 1):
		next[i] += max(cur[i - 1], cur[i])

	# Edge case: the only way to reach the last element
	# is from the last element of the previous row.
	next[-1] += cur[-1]

	return next

if __name__ == "__main__":
	triangle = []
	text = \
"""75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""
	text = text.splitlines()
	for line in text:
		triangle.append(map(int, line.split()))

	cur = triangle[0]
	for row in triangle[1:]:
		cur = propMax(cur, row)

	print max(cur)
