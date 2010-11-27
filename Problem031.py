"""Find the number of combinations of coins to produce a given sum.

Requires Python >= 2.7 for combinations_with_replacement."""

from itertools import combinations, ifilter, repeat

coin_values = [1, 2, 5, 10, 20, 50, 100, 200]
num_coins = [200/val for val in coin_values]
vals_and_nums = zip(coin_values, num_coins)
all_coins = []
for val, num in vals_and_nums:
	all_coins.extend(repeat(val, num))

# TODO: this implementation is fine for small problems, but far too slow
# for the whole problem.  Try Dynamic Programming?
two_pounds = set()
for num in xrange(1, 11):
	candidate_vals = [i for val, amt in vals_and_nums for i in repeat(val, amt)
			if amt <= num]
	for n in xrange(1, num+1):
		two_pounds.update(tuple(comb) for comb in
				combinations(candidate_vals, n) if
				sum(comb) == 200)

#unfiltered_combinations = combinations(all_coins, 200)
#two_pounds = ifilter(lambda comb: sum(comb) == 200, unfiltered_combinations)

print len(list(two_pounds))
