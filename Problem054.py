"""Rank and compare hands of poker."""

SUITS = ('H', 'S', 'D', 'C')
VALUES = {"2": 2,
		"3": 3,
		"4": 4,
		"5": 5,
		"6": 6,
		"7": 7,
		"8": 8,
		"9": 9,
		"T": 10,
		"J": 11,
		"Q": 12,
		"K": 13,
		"A": 14}
RANKS = ('-', '1P', '2P', '3', 'St', 'Fl', 'FH', '4', 'SF')

def parse_card(card):
	"""Evaluate a len-2 string to determine its value and suit.

	'TD' -> (10, 'D'); 'AS' -> (14, 'S'); etc."""
	if card[1] not in SUITS:
		raise ValueError("Invalid card suit: " + str(card[1]))
	return VALUES[card[0]], card[1]

def rank_hand(hand):
	"""Rank a hand; return its rank, and (if appropriate) value and tiebreakers.

	>>> print rank_hand(['2C', '3S', '8S', '8D', 'TD'])
	('1P', 8, [10, 3, 2])

	>>> print rank_hand(['3C', '3D', '3S', '9S', '9D'])
	('FH', [3, 9], None)

	>>> print rank_hand(['3D', '6D', '7D', 'TD', 'QD'])
	('Fl', None, [12, 10, 7, 6, 3])
	"""
	# Parse the hand and do some preprocessing.
	parsedHand = [parse_card(i) for i in hand]
	vals = list(i[0] for i in parsedHand)
	multiples = set([(i, vals.count(i)) for i in vals])
	maxMult = max(multiples, key=lambda x: x[1])
	hasFlush = len(set(i[1] for i in parsedHand)) == 1

	# Evaluate hands which involve multiple copies of the same value.
	if maxMult[1] == 4:
		# Four of a Kind.
		rank = '4'
		value = maxMult[0]
		tiebreakers = _sortHoles(vals, usedValues=value)
	elif maxMult[1] == 3:
		# Full House or Three of a Kind.
		extraPair = _hasPair(multiples - set([maxMult]))
		if extraPair:
			rank = 'FH'
			value = maxMult[0], extraPair[0]
			tiebreakers = None
		else:
			rank = '3'
			value = maxMult[0]
			tiebreakers = _sortHoles(vals, usedValues=value)
	elif maxMult[1] == 2:
		# One Pair or Two Pair.
		extraPair = _hasPair(multiples - set([maxMult]))
		if extraPair:
			rank = '2P'
			value = sorted([maxMult[0], extraPair[0]], reverse=True)
			tiebreakers = _sortHoles(vals, usedValues=value)
		else:
			rank = '1P'
			value = maxMult[0]
			tiebreakers = _sortHoles(vals, usedValues=value)
	elif maxMult[1] == 1:
		# Straights, Flushes, or High Card.
		hasStraight = max(vals) - min(vals) == 4
		if hasStraight and hasFlush:
			rank = 'SF'
			value = max(vals)
			tiebreakers = None
		elif hasStraight:
			rank = 'St'
			value = max(vals)
			tiebreakers = None
		elif hasFlush:
			rank = 'Fl'
			value = None
			tiebreakers = _sortHoles(vals)
		else:
			rank = '-'
			value = None
			tiebreakers = _sortHoles(vals)
	else:
		raise ValueError("Impossible hand: " + ''.join(hand))

	return rank, value, tiebreakers

def cmp_hands(h1, h2):
	"""cmp_hands(h1, h2) -> integer

	Return negative if h1<h2, zero if h1==h2, positive if h1>h2."""
	rank1, values1, tiebreakers1 = h1
	rank2, values2, tiebreakers2 = h2
	rank1 = RANKS.index(rank1)
	rank2 = RANKS.index(rank2)

	# Check if one hand outranks the other.
	if rank1 > rank2:
		return 1
	elif rank2 > rank1:
		return -1
	# Same rank, so check the values (e.g. 33399 loses to 33999) and then the
	# tiebreakers.
	else:
		# If values1 and values2 are lists, iterate them.
		try:
			for val1, val2 in zip(values1, values2):
				if val1 > val2:
					return 1
				elif val2 > val1:
					return -1
		# Otherwise, just compare them.
		except TypeError:
			if values1 > values2:
				return 1
			elif values2 > values1:
				return -1
		# Finally, check the tiebreakers.
		for tb1, tb2 in zip(tiebreakers1, tiebreakers2):
			if tb1 > tb2:
				return 1
			elif tb2 > tb1:
				return -1

	# Even the tiebreakers were tied, so the hands are equal.
	return 0

def _hasPair(multiples):
	"""Find a pair if it exists in the given (value, count) tuples."""
	try:
		return max((i for i in multiples if i[1] > 1),
				key=lambda x: x[1])
	except ValueError:
		return False

def _sortHoles(allValues, usedValues=None):
	"""Eliminate the used values and sort the remainder."""
	if usedValues is None:
		usedValues = []
	try:
		return sorted(list(set(allValues) - set(usedValues)), reverse=True)
	except TypeError:
		return sorted(list(set(allValues) - set([usedValues])), reverse=True)

if __name__ == '__main__':
	p1wins = 0
	with open('poker.txt', 'r') as f:
		for line in f:
			cards = line.split()
			try:
				hand1 = rank_hand(cards[:5])
				hand2 = rank_hand(cards[5:])
			except Exception as e:
				print "cards: ", line
				raise
			if cmp_hands(hand1, hand2) > 0:
				p1wins += 1

	print p1wins
