'''
Problem 15: Longest upload burst

Time limit: 25 minutes.

A storage service logs each upload as a (user, size_mb) tuple, in order. 
The team wants the longest stretch of consecutive uploads whose total size is ≤ quota.

Function name: longest_upload_burst

Arguments:
uploads: a list of (user, size_mb) tuples. user is a string, and size_mb is an int ≥ 0.
quota: an int ≥ 0.

Requirements:
1. Return (start, length) for the longest run of consecutive uploads whose total size_mb is ≤ quota.
2. If runs tie for the longest, return the one that starts earliest.
3. If no stretch of at least 1 upload qualifies, or uploads is empty, return None.
Target: O(n).
'''

'''
Thoughts:
1. The user item in each tuple is a red herring- it isn't used anywhere. 
Thus when cycling through items in the list, be sure to access item[1]
2. Otherwise, classic moving window + window total problem 
3. Return the following:
solution = max(solutions.items(), key=lambda kv:(kv[1], -kv[0]))
if solution[1] == 0:
return None
else:
return solution
'''

def longest_upload_burst(uploads: list, quota: int):
    cumul_tot = {} # key= index position at a given point, val = list cumul tot until that position
    solutions = {} # key = start of run, val= length of run
    
    # Guard: uploads not empty
    if len(uploads) == 0:
        return None
    
    # Start loop 
    # Be sure to get the size value
    for i, (user, size) in enumerate(uploads):
        
        # Guard: What if this is the fist iteration
        # If first iteration, set start to zero and running total to current value
        if i == 0:
            start = 0 # Start of run starts w o
            cumul_tot[i] = size
        # Otherwise, set running total to prior running total + current value
        else:
            cumul_tot[i] = cumul_tot[i-1] + size
            
        # Guard: What if start == 0
        if start == 0:
            run_tot = cumul_tot[i]
        else:
            run_tot = cumul_tot[i] - cumul_tot[start-1]
            
        # Start checking against budget
        # Happy path - append length of current run to solutions
        if run_tot <= quota:
            solutions[start] = i - start + 1
        # Unhappy path - while loop
        else:
            while run_tot > quota:
                start += 1
                run_tot = cumul_tot[i] - cumul_tot[start-1]
            solutions[start] = i - start +1
            
    print(f'solutions: {solutions}')
    solution = max(solutions.items(), key=lambda kv:(kv[1], -kv[0]))
    print(f'solutions: {solution}')
    if solution[1] == 0:
        return None
    else:
        return solution

# Complexity:
# 1. Outer loop -> O(n)
# 2. While --> only moves forward max n times, not multiplicative --> O(n)
# 3. Max --> O(n)
# Total= O(3n) --> O(n) with memory of O(n)

# Test cases
u = [("ann", 40), ("bob", 10), ("cy", 30), ("ann", 10), ("dee", 10), ("bob", 50)]
assert longest_upload_burst(u, 50) == (1, 3)
assert longest_upload_burst(u, 100) == (0, 5)
assert longest_upload_burst(u, 9) is None
assert longest_upload_burst([], 10) is None
assert longest_upload_burst([("a", 0), ("b", 0)], 0) == (0, 2)
assert longest_upload_burst([("a", 60), ("b", 5), ("c", 5)], 50) == (1, 2)
assert longest_upload_burst([("a", 10)], 10) == (0, 1)
assert longest_upload_burst([("a", 20), ("b", 20), ("c", 20), ("d", 20)], 40) == (0, 2)
print("all tests passed")