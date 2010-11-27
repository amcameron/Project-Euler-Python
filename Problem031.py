"""Find the number of combinations of coins to produce a given sum.

Requires Python >= 2.7 for combinations_with_replacement."""

from itertools import combinations_with_replacement, ifilter

coin_values = [0, 1, 2, 5, 10, 20, 50, 100, 200]

unfiltered_combinations = combinations_with_replacement(coin_values, 200)
two_pounds = ifilter(lambda comb: sum(comb) == 200, unfiltered_combinations)

print len(list(two_pounds))
