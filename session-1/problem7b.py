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


def find_pair(amounts: list, target: int):
    print(f'amounts: {amounts}')
    new_dict = {}
    
    for i in range(len(amounts)): 
        
        # Get position (i) value at that position (value_i), and the remainder (remainder)
        value_i = amounts[i]
        remainder = target - value_i
        print(f'i:{i}, value_i: {value_i}, reminder: {remainder}')

        # Look in the dict to see if the remainder is already in there as a key. If so, retrieve the corresponding position.
        remainder_position = new_dict.get(remainder, None)

        # Add to new_dict w/ key=value_i and value=i
        new_dict[value_i] = new_dict.get(value_i, i)
        print(f'new_dict updated to: {new_dict}')
        
        # If there is a remainder position already registered, rearrange i and j to ensure i < j (per requirements)
        if remainder_position is not None:
            solution = (min(i, remainder_position), max(i, remainder_position))
            print(f'solution: {solution}')
            return (solution)
    
    # Return None if no pairs identified
    return None


'''
Complexity:
Steps:
1. 1 loop through each of the values in the list O(n)
2. In each loop, 1 dict lookup O(1)

Result = O(n)
'''

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