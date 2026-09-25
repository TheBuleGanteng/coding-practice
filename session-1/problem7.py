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

# Thinkng: Since the amounts are ints and the target is int, then:
# 1.  if the target is not evenly divisible by a number in amounts, we can eliminate it 
# 2. If the target is evently divisble by a number in amounts, we see if that result is another number in amounts.
def find_pair(amounts: list, target: int):
    print(f'amounts: {amounts}')
    solutions = set()
    
    for n in range(len(amounts)):
        value_n = amounts[n]
        remainder = target - value_n
        print(f'value: {value_n}, reminder: {remainder}')
        
        if remainder in amounts:
            position_remainder = amounts.index(remainder) # Find the position of the remainder in the index (returns the first occurance)
            print(f'for remainder: {remainder}, position_remainder:{position_remainder}')
            
            i, j = min(n, position_remainder), max(n, position_remainder) # Reorders the pair, since the problem states position i < position j 
            print(f'i: {i}, j:{j}')
            
            if i != j:
                solutions.add((i, j)) # I need to return a position for the remainder, not the value, so I need some way to find that position. I suspect there is a method for this, but I don't know it.
                print(f'appended to solutions: {value_n}, {remainder} which are in positions {i} and {j}')
    
    print(f'solutions: {solutions}')    
    if len(solutions) == 0:
        return None
    else:
        solutions = min(solutions, key=lambda kw:(kw[1], kw[0]))
        return solutions


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