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


def busiest_window(counts: list, k: int):
    num_counts = len(counts)
    running_totals = {}

    # return none for bogus windows
    if num_counts <= 0 or k <= 0 or k > num_counts:
        print(f'returning None')
        return None
    
    # loop across each count
    for i, count in enumerate(counts):
        
        # gard against overruns
        if i + k <= num_counts:
            
            # Calculate the first total
            if len(running_totals) == 0:
                total = sum(counts[i:i+k])
                running_totals[i] = total  
                print(f'initial total done - running_totals: {running_totals}')
            else:
                running_totals[i] = running_totals[i-1] - counts[i-1] + counts[i+k-1]
                print(f'updated running totals - running_totals: {running_totals}')

    print(f'final running_totals: {running_totals}')
    best_start = max(running_totals, key=running_totals.get)
    solution = best_start, running_totals[best_start] 
    print(f'solution: {solution}')
    return solution


# Complexity:
# 1. First loop: O(n)
# 2. Fist addition of k numbers O(k)
# 3. After that, nothing varies with k (e.g. we subtract 1 number and add 1 number each time)
# 4. The final max step O(n)
# Result: O(n) + O(k) + O(n) --> Since k <= n --> O(n) + O(n) + O(n) --> O(3n) --> drop the constant --> O(n)
    
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