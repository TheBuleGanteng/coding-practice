# type: ignore
'''
Problem 11c: Longest quiet stretch, efficient version

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

def longest_quiet_stretch(counts: list, budget: int):
    running_tot = {} # Dict w/ key=position, value=cumulative total from [0] until that position
    stretches = {} # Dict w/ key =start, value= length of that run
    
    # Inital guards
    if len(counts) == 0 or min(counts) > budget:
        return None
    
    for i, count in enumerate(counts):
        
        # If first entry, no look-back. Go ahead and add count and set start to [0]
        if i == 0:
            running_tot[i] = count
            start = 0
            
            
        # If not first entry, running total = prior running total + current value
        else:
            running_tot[i] = running_tot[i-1] + count
        
        # Guard against start = [0] --> start-1 = [-1] 
        if start == 0:
            stretch_tot = running_tot[i] - 0
        else:
            stretch_tot = running_tot[i] - running_tot[start-1]
        
        # Happy path: Update stretches dict
        if stretch_tot <= budget:
            print(f'happy path: stretch_tot: {stretch_tot} <= budget: {budget}')
            stretches[start] = i-start+1
        
        # Unhappy path: move start forward until meets budget 
        else:
            print(f'starting unhappy path: stretch_tot: {stretch_tot} > budget: {budget}')
            while stretch_tot > budget:
                start += 1
                stretch_tot = running_tot[i] - running_tot[start-1]
            stretches[start] = i-start+1
            
    # Find best solution w max
    print(f'stretches: {stretches}')
    solution = max(stretches.items(), key=lambda kv:(kv[1], -kv[0]))
    print(f'solution: {solution}')
    return solution

# Complexity:
# 1. Loop loops n times -->  O(n)
# 2. While: start only moves forward, so at most n steps in TOTAL across the whole run --> O(n)
# 3. Max (outside loop) is always O(m) w/ m <= n --> O(n)
# Total: O(n+n+n) --> O(3n) --> O(n)
# Memory: O(n) for n items


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