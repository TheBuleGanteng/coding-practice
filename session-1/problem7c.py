'''
Problem 7: Match a payment pair, in one pass

Same task as Problem 6, with a performance constraint: the solution must run in O(n) time.

Function name: find_pair

Arguments:

amounts: a list of ints, where each int is a payment in cents.
target: an int, the total to match.

Requirements:

Return a tuple (i, j) of the positions of two payments whose amounts add up to target, with i < j.
A payment can't be paired with itself, but two different payments can have the same amount.
If more than one pair works, return the pair whose j is smallest. If several is work with that j, return the smallest i.
If no pair works, return None.
New: walk through amounts exactly once. No nested loops, and nothing that hides a loop inside a loop. The total work must be O(n).
'''

# Loop through each item in the list
# Find the remainder of total / list[n]
# Check the dict to see if that remainder is there and if so, retrieve the position (stored as the value w/ remainder as the key)


def find_pair(amounts: list, target: int):
    dict = {}
    solutions = []
    
    for n in range(len(amounts)):
        print(f'n: {n}')
        
        remainder = target - amounts[n]
        position_match = dict.get(remainder, None)
        print(f'remainder: {remainder}, position_match: {position_match}')
        
        if position_match is not None:
            solution = ((min(position_match, n), max(position_match, n)))
            print(f'returning solution: {solution}')
            return solution
        elif dict.get(amounts[n], None) is not None:
            print(f'remainder not yet in dict, however, current value is. Do not add current value')
            continue
        else:
            print(f'remainder not yet in dict, adding amounts[n]: {amounts[n]} and n: {n} to dict')
            dict[amounts[n]] = n
            continue
    
    print(f'returning None')
    return None
        
# Complexity: 
# There is only one loop and inside that loop, a fixed amount of work is done --> O(n)
        
# Test cases
assert find_pair([500, 1200, 300, 700], 1000) == (2, 3)
assert find_pair([250, 750, 400, 600], 1000) == (0, 1)
assert find_pair([500, 500], 1000) == (0, 1)
assert find_pair([500], 1000) is None
assert find_pair([100, 200, 300], 1000) is None
assert find_pair([], 0) is None
assert find_pair([400, 100, 600, 900], 1000) == (0, 2)
assert find_pair([300, 300, 700], 1000) == (0, 2)
assert find_pair([100, 500, 500, 900], 1000) == (1, 2)
assert find_pair([300, 700, 700], 1000) == (0, 1)
print("all tests passed")