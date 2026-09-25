'''
Problem 5: Merge monitoring windows

A monitoring system logs time windows when an alert was active. Each window has a start and an end time.
Write a function that merges any windows that overlap or touch, and returns the merged windows.

Function name: merge_windows

Argument:

windows: a list of (start, end) tuples, where both values are ints and start <= end.

Requirements:

1. The input may be in any order.
2. Two windows overlap if they share any time. For example, (1, 5) and (3, 8) overlap.
3. Two windows touch if one starts exactly where the other ends. For example, (1, 4) and (4, 6) touch. Touching windows also merge.
4. Return a list of (start, end) tuples, sorted by start time, with no two windows overlapping or touching.
4. An empty input returns an empty list.

Test cases
assert merge_windows([(1, 3), (2, 6), (8, 10), (15, 18)]) == [(1, 6), (8, 10), (15, 18)]
assert merge_windows([(1, 4), (4, 5)]) == [(1, 5)]
assert merge_windows([(8, 10), (1, 3), (2, 6)]) == [(1, 6), (8, 10)]
assert merge_windows([(1, 10), (2, 3)]) == [(1, 10)]
assert merge_windows([(1, 3), (3, 5), (5, 7)]) == [(1, 7)]
assert merge_windows([(1, 2), (3, 4)]) == [(1, 2), (3, 4)]
assert merge_windows([(5, 7)]) == [(5, 7)]
assert merge_windows([]) == []
print("all tests passed")
'''

# Overall thinking: I think I need to do the following:
# 1. Order each of the pairs by the first item in that pair
# 2. Check each 2 sequential pairs (n, n+1) to see if the second item in the first pair (n1b) equals the first item in the second pair (n2a).
#   If yes, merge the pair, reorder, and restart
# Notes: 
# - I think this would work best with a wile or until loop, but not sure

def merge_windows(windows: list):
    print(f'starting merge_windows...')
    print(f'windows is: {windows}')
    results= [] # Final list of merged pairs
    
    # Step 1: Order the list by the fist number
    windows_sorted = sorted(windows, key=lambda kv:(kv[0])) # I know that for a list of dicts, we were able to deal with each dict using the .items() method. This seems to error with using a list. Not sure what is the correct equivilent of .items() for a list.
    print(f'windows_sorted: {windows_sorted}')
   
    # Step 2: Compare the start and end times of each pair
    for start_1, end_1 in windows_sorted:    
        
        # If this is the first pass, append the first pair and increment the loop
        if len(results) == 0:
            results.append(windows_sorted[0])
            continue
        
        # Assuming this is not the first pass, parse the starting and ending time for the current pair
        start_0, end_0 = results[-1]

        if start_1 <= end_0: # We have some kind of overlap.  
            merged_start = start_0 # Use start_0 as the starting point for the new pair.
            
            if end_1 >= end_0: # pair_1 ends after pair_0
                merged_end = end_1 
            else:
                merged_end = end_0 # Pair 0 ends after pair 1 (e.g. pair 1 is completely within pair 0)
            results[-1] = merged_start, merged_end
            print(f'new merged pair: {merged_start, merged_end}')
            
        else:
            unchanged_pair = start_1, end_1
            results.append((start_1, end_1)) # Here, there is no overlap, so just append the new pair to results as-is 
        print(f'updated results: {results}')    



    return results

'''
    # Complexity:
    print(f'Complexity consists of the following:
        1. n log n : One pass for each item in the list to sort them (always n log n)
        2. n : Another pass that compares the most recent pair in results to the current pair in windows, merging if needed
        Result: O(n log n + n) = O(n log n)
'''



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

