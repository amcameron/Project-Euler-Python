import random
from pprint import pprint

board = ['GO', 'A1', 'CC1', 'A2', 'T1', 'R1', 'B1', 'CH1', 'B2', 'B3',
		'JAIL', 'C1', 'U1', 'C2', 'C3', 'R2', 'D1', 'CC2', 'D2', 'D3',
		'FP', 'E1', 'CH2', 'E2', 'E3', 'R3', 'F1', 'F2', 'U2', 'F3',
		'G2J', 'G1', 'G2', 'CC3', 'G3', 'R4', 'CH3', 'H1', 'T2', 'H2']
community_chest = ['GO', 'JAIL'] + [''] * 14
chance = ['GO', 'JAIL', 'C1', 'E3', 'H2', 'R1', 'R*', 'R*', 'U*', '-3'] + \
		[''] * 6
railways = (5, 15, 25, 35)
utilities = (12, 28)
doubles = [False] * 3

def roll(die_sides):
	"""Return the result of rolling two fair dice with die_sides sides, and
	whether the roll was a double, as a (sum, boolean) tuple."""
	a = random.randint(1, die_sides)
	b = random.randint(1, die_sides)
	return a + b, a == b

def position_manager_factory(die_sides):
	"""Create a game position manager function which uses dice with the given
	number of sides."""

	def fun(pos):
		"""Given the player's current position, roll the dice, follow the game
		rules, and determine the player's final position."""

		total, isDouble = roll(die_sides)
		doubles.append(isDouble)
		doubles.pop(0)
		new_pos = (pos + total) % len(board)
		pos_name = board[new_pos]

		if (pos_name == 'G2J' or all(doubles)):
			new_pos = board.index('JAIL')
		elif (pos_name.startswith('CH')):
			card = chance.pop(0)
			if (card == 'R*'):
				# Move to the next railway.
				if (new_pos > railways[-1]):
					new_pos = 0
				new_pos = min(rr for rr in railways if rr > new_pos)
			elif (card == 'U*'):
				# Move to the next utility.
				if (new_pos > utilities[-1]):
					new_pos = 0
				new_pos = min(ut for ut in utilities if ut > new_pos)
			elif (card == '-3'):
				new_pos = new_pos - 3
				pos_name = board[new_pos]
			elif card:
				new_pos = board.index(card)
			chance.append(card)

		# We can arrive at Community Chest either by rolling and landing there,
		# or by getting dropped there by a Chance card on this same turn.
		# Therefore, don't use "elif" - let the Chance case fall through.
		if (pos_name.startswith('CC')):
			card = community_chest.pop(0)
			if card:
				new_pos = board.index(card)
			community_chest.append(card)

		return new_pos
		
	return fun

def play(num_turns, die_sides):
	"""Initialize a new game and simulate it for the specified number of turns,
	returning the most frequently landed-on squares as (name, freq) tuples."""

	# Perform setup.
	pos = 0
	occurrences = [0] * len(board)
	advance = position_manager_factory(die_sides)

	for i in xrange(num_turns):
		pos = advance(pos)
		occurrences[pos] += 1

	freqs = [occ / float(num_turns) for occ in occurrences]
	retval = zip(freqs, board)
	retval.sort(key=lambda x: x[0], reverse=True)
	return retval

if __name__ == '__main__':
	board_sorted_by_freq = play(1000000, 4)
	pprint(board_sorted_by_freq[:5])
