import random
from pprint import pprint

board = ['GO', 'A1', 'CC1', 'A2', 'T1', 'R1', 'B1', 'CH1', 'B2', 'B3',
		'JAIL', 'C1', 'U1', 'C2', 'C3', 'R2', 'D1', 'CC2', 'D2', 'D3',
		'FP', 'E1', 'CH2', 'E2', 'E3', 'R3', 'F1', 'F2', 'U2', 'F3',
		'G2J', 'G1', 'G2', 'CC3', 'G3', 'R4', 'CH3', 'H1', 'T2', 'H2']
community_chest = ["GO", "JAIL"] + [""] * 14
chance = ["GO", "JAIL", "C1", "E3", "H2", "R1", "R*", "R*", "U*", "-3"] + \
		[""] * 6

def roll(die_sides):
	"""Return the result of rolling two fair dice with die_sides sides."""
	return random.randint(1, die_sides) + random.randint(1, die_sides)

def position_manager_factory(die_sides):
	"""Create a game position manager function which uses dice with the given
	number of sides."""

	def fun(pos):
		"""Given the player's current position, roll the dice, follow the game
		rules, and determine the player's final position."""

		# First implementation: don't follow any rules; just wrap around.
		# Check that the spaces all have about the same frequency.
		new_pos = (pos + roll(die_sides)) % len(board)

		return new_pos
		
	return fun

def play(num_turns):
	"""Initialize a new game and simulate it for the specified number of turns,
	returning the most frequently landed-on squares as (name, freq) tuples."""

	# Perform setup.
	pos = 0
	die_sides = 6
	occurrences = [0] * len(board)
	advance = position_manager_factory(die_sides)

	for i in xrange(num_turns):
		pos = advance(pos)
		occurrences[pos] += 1

	return [occ / float(num_turns) for occ in occurrences]

if __name__ == '__main__':
	freqs = play(100000)
	pprint(zip(board, freqs))
