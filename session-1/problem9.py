'''
A web service logs how many requests it received each minute, in order. 
The on-call team wants to find the busiest stretch of k consecutive minutes.

Function name: busiest_window

Arguments:
counts: a list of ints, one per minute, each ≥ 0.
k: an int, the length of the window in minutes.

Requirements:

1. Return a tuple (start, total). start is the index of the first minute in the busiest window, and total is the sum of the requests in that window.
2. If several windows tie for the highest total, return the one that starts earliest.
3. If no window of length k is possible (empty list, k ≤ 0, or k longer than the list), return None.
4. Target: O(n) time. A first version that re-adds every window from scratch is acceptable. 
If you write that version, state its complexity, then improve it.
'''

# Find the length of counts
# Disqualify if k doesn't make sense, relative to length of counts
# Running total, e.g. n, n+1, etc. 
# Need to keep both position and value

def busiest_window(counts: list, k: int):
    obserations = len(counts)
    results = {} # Dict with keys = position and values = calls
    
    # Req 3
    if obserations <= 0 or k <= 0 or k > obserations:
        return None

    # Loop across each observation to store key=position, value=observations
    for i, count in enumerate(counts):
        if i+k <= obserations:
            slice_total = sum(counts[i:i+k])
            results[i] = slice_total
    
    best_window_start_pos = max(results, key=results.get)
    print(f'best_window_start_pos: {best_window_start_pos}')
    return best_window_start_pos, results[best_window_start_pos]
    
# Complexity:
# 1. Initial check: O(1)
# 2. First loop: O(n)
# 3. Inside that loop, k work is done

# Test cases
assert busiest_window([1, 3, 2, 5, 1, 1], 2) == (2, 7)
assert busiest_window([5, 1, 1, 5], 2) == (0, 6)
assert busiest_window([4], 1) == (0, 4)
assert busiest_window([1, 2, 3], 3) == (0, 6)
assert busiest_window([1, 2, 3], 4) is None
assert busiest_window([], 1) is None
assert busiest_window([1, 2, 3], 0) is None
assert busiest_window([0, 0, 0], 2) == (0, 0)
assert busiest_window([3, 1, 4, 1, 5, 9, 2, 6], 3) == (5, 17)
print("all tests passed")