'''
Problem 5: Merge monitoring windows
A monitoring system logs time windows when an alert was active. Each window has a start and an end time.
Write a function that merges any windows that overlap or touch, and returns the merged windows.

Function name: merge_windows
Argument: windows: a list of (start, end) tuples, where both values are ints and start <= end.

Requirements:
1. The input may be in any order.
2. Two windows overlap if they share any time. For example, (1, 5) and (3, 8) overlap.
3. Two windows touch if one starts exactly where the other ends. For example, (1, 4) and (4, 6) touch. Touching windows also merge.
4. Return a list of (start, end) tuples, sorted by start time, with no two windows overlapping or touching.
4. An empty input returns an empty list.
'''

def merge_windows(windows: list):
    print(f'windows: {windows}')
    solution = []
    
    # Sort all existing windows by start time
    windows_sorted = sorted(windows, key=lambda kv:(kv[0]))
    print(f'windows_sorted: {windows_sorted}')        


    # Extract each window's start and end
    for window in windows_sorted:
        print(f'solution: {solution}, len[solution]: {len(solution)}')
        
        # Automatically append the first pair
        if len(solution) == 0:
            solution.append(window)
            print('appended first window to solution')
            continue
        
        # Check each pair against the preceeding pair
        s1, e1 = solution[-1]
        s2, e2 = window
        print(f's1: {s1}, e1: {e1}, s2: {s2}, e2: {e2}')
        
        if s2 <= e1: # Overlap detected
            if e2 <= e1: # Window 2 is entirely witin window 1. Preserve the existing soltion, discarding window 2
                print(f'complete overlap: window 2: {window} entirely within window 1: {solution[-1]}')
                continue
            else:
                print(f'replaced existing solution[-1]: {solution[-1]} with: {s1, e2}')
                solution[-1] = s1, e2 # Replace the existing solution
                continue
        
        solution.append(window)
        print(f'no overlap - appended window to solution')
    
    return solution
                 
        
# Complexity:
# Sort: O(n log n) (n = number of windows)
# Merge: one pass, O(1) work per window (lookup [-1], compare, append/replace) → O(n)
# Total: O(n log n + n) → O(n log n); the sort dominates

        
    
# Test cases
assert merge_windows([(1, 3), (2, 6), (8, 10), (15, 18)]) == [(1, 6), (8, 10), (15, 18)]
assert merge_windows([(1, 4), (4, 5)]) == [(1, 5)]
assert merge_windows([(8, 10), (1, 3), (2, 6)]) == [(1, 6), (8, 10)]
assert merge_windows([(1, 10), (2, 3)]) == [(1, 10)]
assert merge_windows([(1, 3), (3, 5), (5, 7)]) == [(1, 7)]
assert merge_windows([(1, 2), (3, 4)]) == [(1, 2), (3, 4)]
assert merge_windows([(5, 7)]) == [(5, 7)]
assert merge_windows([]) == []
print("all tests passed")

