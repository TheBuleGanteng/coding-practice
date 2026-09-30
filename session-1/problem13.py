'''
Problem 13: Longest tolerant stretch

Time limit: 25 minutes.

A health checker logs one status per minute, either "OK" or "ERR". 
The team wants the longest stretch of consecutive minutes that contains at most max_errors "ERR" minutes.

Function name: longest_tolerant_stretch

Arguments:
statuses: a list of strings, each "OK" or "ERR".
max_errors: an int ≥ 0.

Requirements:
1. Return (start, length) for the longest run of consecutive minutes with no more than max_errors "ERR" entries.
2. If runs tie for the longest, return the one that starts earliest.
3. If no stretch of at least 1 minute qualifies, or statuses is empty, return None.
Target: O(n).
'''

def longest_tolerant_stretch(statuses: list, max_errors: int):
    running_tot = {} # key current index, value is running total from beginning
    solutions = {} # key= start, value= len
    
    # Guard: Req 3
    if len(statuses) == 0:
        print(f'erroring out, returning None')
        return None
    
    # Start loop
    for i, status in enumerate(statuses):
        print(f'status: {status}, i: {i}')
        
        # Convert readings to 0 for OK and 1 for ERR (easier)
        if status == "ERR":
            num_status = 1
        else:
            num_status = 0
        
        # Guard against running_tot[i-1] = [-1]
        # If this IS the first time loop runs
        if i == 0:
            start = 0
            running_tot[i] = num_status
        # If this IS NOT the first time loop runs
        else:
            running_tot[i] = running_tot[i-1] + num_status
        
        # Guard against start-1 = [-1], since normally a stretch_tot = running_tot[i] - running_tot[i-start-1]
        if start == 0:
            stretch_tot = running_tot[i] - 0
        else:
            stretch_tot = running_tot[i] - running_tot[start-1]

        # Happy path: Update soluton for stetch's length
        if stretch_tot <= max_errors:
            solutions[start] = i - start + 1
        # Unhappy path: keep inrementing start until stretch_tot fits budget
        else:
            while stretch_tot > max_errors:
                start += 1
                stretch_tot = running_tot[i] - running_tot[start-1]
            solutions[start] = i-start+1
            

    print(f'solutions: {solutions}')
    solution = max(solutions.items(), key=lambda kv:(kv[1], -kv[0]))
    print(f'solution: {solution}')
    
    if solution[1] == 0:
        return None
    else:
        return solution


# Test cases
s = ["OK", "ERR", "OK", "OK", "ERR", "OK"]
assert longest_tolerant_stretch(s, 1) == (0, 4)
assert longest_tolerant_stretch(s, 0) == (2, 2)
assert longest_tolerant_stretch(s, 2) == (0, 6)
assert longest_tolerant_stretch([], 1) is None
assert longest_tolerant_stretch(["ERR", "ERR"], 0) is None
assert longest_tolerant_stretch(["ERR", "ERR"], 1) == (0, 1)
assert longest_tolerant_stretch(["OK", "OK", "OK"], 0) == (0, 3)
assert longest_tolerant_stretch(["ERR", "OK", "ERR", "OK", "OK", "ERR"], 1) == (1, 4)
assert longest_tolerant_stretch(["OK", "ERR", "ERR", "OK"], 1) == (0, 2)
print("all tests passed")