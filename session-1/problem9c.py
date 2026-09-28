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
4. Target: O(n) time. 
If you write that version, state its complexity, then improve it.
'''

# High-level: 
# - List slicing with a running total most efficient solution. Will need some initial checks

def busiest_window(counts: list, k: int):
    counts_len = len(counts)
    running_total = {}
    print(f'counts_len: {len(counts)}, k: {k}')
    
    # Initial checks
    if counts_len <= 0 or k <= 0 or counts_len < k:
        return None
    
    # Loop through each char in window
    for i, count in enumerate(counts):
        print(f'i: {i}')
        
        # Scope the addition to ensure it doesn't overrun the end of counts
        if i + k <= counts_len:
            
            # If the first loop, go ahead and add the first 3 chars
            if i == 0:
                running_total[i] = sum(counts[i:i+k])
                print(f'i: {i}, summing positions i: {i} to i+k:{i+k-1}, running_total updated to: {running_total}')
            else:    
                # If not the first loop, then each time, drop the first item from the last time and add the new item k places out front
                running_total[i] = running_total[i-1] - counts[i-1] + counts[i+k-1] 
                print(f'running total updated... dropped counts[i-1]: {counts[i-1]} and added counts[i+k-1]:{counts[i+k-1]}, running_total updated to: {running_total}')
        
    # Find the one with the highest total (value)
    best_window = max(running_total.items(), key=lambda kv:(kv[1], -kv[0]))
    print(f'best_window: {best_window}')
    return best_window

# Complexity:
# 1. Intial check: O(1)
# 2. Loop: O(n)
# 3. First totaling inside loop O(k)
# 4. Rest of totaling inside loop is fixed (e.g. drop 1 char, add 1 char): O(1)
# 5. Final scan by highest value, lowest key: O(n-k+1)
# Total: O(n) + O(k) + ~O (n) -->  O(2n+k) --> O(n+k) --> since k <= n --> O(n)

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