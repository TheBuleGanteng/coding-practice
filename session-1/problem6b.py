'''
Problem 6: Match a payment pair

A reconciliation system has a list of payment amounts in cents, in the order they arrived. 
It needs to find two payments that add up exactly to a target amount.

Function name: find_pair

Arguments:

amounts: a list of ints, where each int is a payment in cents.
target: an int, the total to match.

Requirements:

1. Return a tuple (i, j) of the two positions (indices) of payments whose amounts add up to target, with i < j.
2. A payment can't be paired with itself, but two different payments can have the same amount.
3. If more than one pair works, return the pair whose second position j is smallest. If several is work with that j, return the smallest i.
3. If no pair works, return None.

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

def find_pair(amounts: list, target: int):
    print(f'running find_pair...')
    print(f'amounts: {amounts}')
    
    solutions = []
    
    for i in range(len(amounts)):
        num_first = int(amounts[i])
        for j in range(i+1, len(amounts)): # The idea here is to start a second loop with i+1 - I forget how to do that
            num_second = int(amounts[j])
            if num_first + num_second == target:
                # Pair found! Add to list of solutions
                solutions.append((i, j))
                
    if len(solutions) == 1:
        return solutions[0]
    elif len(solutions) > 1:
        solutions = [min(solutions, key=lambda kv:(kv[1], kv[0]))] # Note that this version uses min instead of sort (used in problem6.py)
        return solutions[0]
    else:
        return None
    
# Complexity: 
# Steps: 
#   Loop complexity:
#       The outer loop runs n-1 times (e.g. we will check 9 of the total 10 values as the first item in the pair)
#       Each time that outer loop runs, we add that value to the following items. When n=10 and i=0, then we perform 9 checks, when i=1, we perform 8 checks, etc. The average number of checks per pass is n/2
#       In summary, (n-1)(n/2) --> (n^2 - n)/2 --> O(n^2) 
#   Sort complexity: 
#       m (just need to find the min)
#   Total complexity:
#       loop complexity + sort complexity : n^2 + m --> O(n^2) Note how this is smaller than n^2 log n when using sorting (as done in problem6.py)
#   
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
print("all tests passed")