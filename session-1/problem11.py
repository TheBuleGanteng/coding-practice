'''
Problem 11: Longest quiet stretch

Time limit: 15 minutes.

An on-call engineer wants to find the longest stretch of consecutive minutes when the service was quiet: 
when the total number of requests across the stretch stayed within a budget.

Function name: longest_quiet_stretch

Arguments:
counts: a list of ints, one per minute, each ≥ 0.
budget: an int ≥ 0.

Requirements:

1. Return a tuple (start, length) for the longest run of consecutive minutes whose total is ≤ budget.
2. If several runs tie for the longest, return the one that starts earliest.
3. If no single minute fits within the budget, or counts is empty, return None.
4. This version can be brute force. State its complexity.
''' 

# High level ideas:
# 1. Iterate over counts, progressively totalling until budget or end of counts is reached. Add start point and and total to list
# 2. Sort by (a) total (highest to lowest) and (b) start point (lowest to highest)

def longest_quiet_stretch(counts: list, budget: int):
    solutions = {}
    
    # Guards
    if len(counts) == 0 or min(counts) > budget:
        return None
    
    for i, counti in enumerate(counts):
        
        # Immediately advance to the next number if the current one is over budget
        if counti > budget:
            continue
        
        total = counti
        length = 1
        
        # Start looping over the subseqent numbers
        for j, countj in enumerate(counts[i+1:]):
            print(f'j:{j}, countj: {countj}')
            
            # If adding the next number puts us over budget stop and append the solution
            if total + countj > budget:
                solutions[i] = length        
                break
            
            # If adding the next number doesn't exceed budget, keep going
            else:
                total = total + countj
                length = length + 1
        
        # If we reached the end of counts w/o exceeding budget, append what we have an iterate i
        solutions[i] = length
        print(f'solutions: {solutions}')
        
    # Find the (a) max length and (b) soonest start
    solution = max(solutions.items(), key=lambda kv:[kv[1], -kv[0]])
    print(f'solution: {solution}')
    return solution

# Test cases
assert longest_quiet_stretch([2, 1, 3, 1, 1, 4], 5) == (1, 3)
assert longest_quiet_stretch([5, 5, 5], 4) is None
assert longest_quiet_stretch([], 10) is None
assert longest_quiet_stretch([1, 1, 1, 1], 10) == (0, 4)
assert longest_quiet_stretch([3, 3, 3], 3) == (0, 1)
assert longest_quiet_stretch([0, 0, 7, 0], 0) == (0, 2)
assert longest_quiet_stretch([4, 1, 1, 4, 1, 1, 1], 3) == (4, 3)
assert longest_quiet_stretch([6, 2], 5) == (1, 1)
print("all tests passed")