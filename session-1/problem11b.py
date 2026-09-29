'''
Problem 11b: Longest quiet stretch, efficient version

Time limit: 30 minutes.

Function name: longest_quiet_stretch

Arguments:
counts: a list of ints, one per minute, each ≥ 0.
budget: an int ≥ 0.

Target: O(n). No restarting from every start.

Recap of the requirements:
1. Return (start, length) for the longest run of consecutive minutes whose total is ≤ budget.
2. If runs tie for the longest, return the one that starts earliest.
3. If no single minute fits within the budget, or counts is empty, return None.
''' 

# High level ideas:
# 1. Check to if len(counts) == 0 or min(counts) > budget
# 2. I think I want a running total, wherein I use a dict to record each position and the total until that position --> can use prior total + new number to avoid re-totaling multiple numbers
# 3. Use a max across the solutions, as usual

def longest_quiet_stretch(counts: list, budget: int):
    counts_dict = {} # Dict with key=position, value=total until that point
    solutions = {} # Dict with key= position, value = length of stetch
    
    # Initial guard
    if len(counts) == 0 or min(counts) > budget:
        return None
    
    # Create dict that holds the position and the total (until that point) for each item in counts
    for i, count in enumerate(counts):
        
        # Get running total (counts_dict) and stretch total (total)
        if i == 0: 
            start = 0 
            counts_dict[i] = count # Don't add to prior value (there are none)
        else:
            counts_dict[i] = counts_dict[i-1] + count # Increment the overall running total
        print(f'completed counts_dict: {counts_dict}')    
                
        # Get the total of the current window
        if start == 0:
            stretch_total = counts_dict[i]
        else:
            stretch_total = counts_dict[i] - counts_dict[start-1]
            
        # Check stretch_total against budget
        # Happy path
        if stretch_total <= budget:
            solutions[start] = i - start + 1 # Solution dict is (starting_position, length of run)

        # Unhappy path    
        else:    
            # If the updated total is greater than the budget, then keep removing items while the total remains above the budget
            while stretch_total > budget:
                start += 1
                stretch_total = counts_dict[i] - counts_dict[start-1]
            solutions[start] = i - start + 1 # Save the new solution thus derived 
            print(f'readjusted window to starting position:{start}, with length: {i-start + 1} and stretch_total: {stretch_total}')
        
    print(f'solutions: {solutions}')
    solution = max(solutions.items(), key=lambda kv:(kv[1], -kv[0]))
    print(f'solution: {solution}')
    return solution
        
# Complexity:
# 1. One loop: O(n)        
# 2. The stuff inside that loop is arethmetic --> O(1)
# 3. The while effecively represents a second, independent loop, since it performs at most n steps across the whole run --> O(n)
# 4. The max --> O(n)
# Total = O(n+n+n) --> O(3n) --> O(n)
# Space: O(n) for counts_dict and solutions

# Test cases
assert longest_quiet_stretch([2, 1, 3, 1, 1, 4], 5) == (1, 3)
assert longest_quiet_stretch([5, 5, 5], 4) is None
assert longest_quiet_stretch([], 10) is None
assert longest_quiet_stretch([1, 1, 1, 1], 10) == (0, 4)
assert longest_quiet_stretch([3, 3, 3], 3) == (0, 1)
assert longest_quiet_stretch([0, 0, 7, 0], 0) == (0, 2)
assert longest_quiet_stretch([4, 1, 1, 4, 1, 1, 1], 3) == (4, 3)
assert longest_quiet_stretch([6, 2], 5) == (1, 1)
assert longest_quiet_stretch([2, 1, 3, 0], 4) == (1, 3)
assert longest_quiet_stretch([2, 2, 1, 4, 0, 0], 5) == (2, 4)
print("all tests passed")