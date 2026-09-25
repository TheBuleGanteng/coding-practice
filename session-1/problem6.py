'''
Problem 6: Match a payment pair

A reconciliation system has a list of payment amounts in cents, in the order they arrived. It needs to find two payments that add up exactly to a target amount.

Function name: find_pair

Arguments:

amounts: a list of ints, where each int is a payment in cents.
target: an int, the total to match.

Requirements:

Return a tuple (i, j) of the two positions (indices) of payments whose amounts add up to target, with i < j.
A payment can't be paired with itself, but two different payments can have the same amount.
If more than one pair works, return the pair whose second position j is smallest. If several is work with that j, return the smallest i.
If no pair works, return None.

Test cases
assert find_pair([500, 1200, 300, 700], 1000) == (2, 3)
assert find_pair([250, 750, 400, 600], 1000) == (0, 1)
assert find_pair([500, 500], 1000) == (0, 1)
assert find_pair([500], 1000) is None
assert find_pair([100, 200, 300], 1000) is None
assert find_pair([], 0) is None
assert find_pair([400, 100, 600, 900], 1000) == (0, 2)
assert find_pair([300, 300, 700], 1000) == (0, 2)
print("all tests passed")

Once it passes: state the complexity with the mechanism behind it. 
If your solution checks every possible pair, say what that costs, and whether you think it can be done in one pass. 
Getting it working is the first goal; the second question is where this problem gets interesting.
'''