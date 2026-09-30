'''
Problem 14: Longest fast stretch

Time limit: 25 minutes.

An API logs the latency of each request in milliseconds, in order. 
A request is slow if its latency is strictly greater than threshold. 
The team wants the longest stretch of consecutive requests containing at most max_slow slow requests.

Function name: longest_fast_stretch

Arguments:
latencies: a list of ints, each ≥ 0.
threshold: an int ≥ 0.
max_slow: an int ≥ 0.

Requirements:
1. Return (start, length) for the longest run of consecutive requests with no more than max_slow slow requests.
2. If runs tie for the longest, return the one that starts earliest.
2. If no stretch of at least 1 request qualifies, or latencies is empty, return None.
Target: O(n).
'''

'''
Notes:
 - Bigger value = slower
 - Slow = latench > threshold
 
Example:
lat = [120, 300, 90, 80, 450, 100, 95], 200, 1
middle solution:
    300, 90, 80
    for i, latency in latencies:
        i = 0
        latency = 300
        
        # Convert speeds into a minomial of violations (1) or not (0)
        if latency > threshold: violations_dict[i] = 1
        else: violations_dict[i] = 0
        # Now, violations_dict = [1]
        
        get running cumul total of violations:
        if i == 0
            violations_cumul[i] = violations_dict[i]
        else:
            violations_cumul[i] = violations_dict[i-1] + violations_dict[i]
        
        # Now, violations_cumul = 1
        
        # happy path
        if violations_cumul <= max_slow:
            solutions[start]
        
        Loop 2:
        i = 1
        latency = 90
        violations_dict[i] 
 
 To return:
 - longest strech where the number of items above the threshold is <= max_slow
 - format: (index position of stetch start, length of stretch)
'''

def longest_fast_stretch(latencies: list, threshold: int, max_slow: int):
    violations_dict = {} # key= index position, value=0(no violation) or 1(violation)
    violations_cumul = {} # key = index position, value= cumul violations from list start until that position
    solutions = {} # dict containing stretches with key=start, value = length of run

    
    # guard
    if len(latencies) == 0:
        return None
    
    for i, latency in enumerate(latencies):
        
        # Convert speeds into a dict of violations or not
        if latency > threshold:
            violations_dict[i] = 1
        else:
            violations_dict[i] = 0
        print(f'violations_dict udpated to: {violations_dict}')    
        
        # Create running total violations from start of list
        # If this is the first poisiton in the binomial list, then the total = current value and start of run = start
        if i == 0:
            violations_cumul[i] = violations_dict[i]
            run_start = 0
        # If this isn't the first position in the list, simply take the prior total and add current value
        else:
            violations_cumul[i] = violations_cumul[i-1] + violations_dict[i]
        print(f'violations_cumul updated to: {violations_cumul}')
    
        # Create running total of violations for the current run (run_cumul[i] - run_cumul[start-1])
        # If the run starts at [0] then the total until now is also run total
        if run_start == 0:
            run_cumul = violations_cumul[i] 
        # If run doesn't start at 0, then the total for this run is the current grand total - the grand total before start
        else:
            run_cumul = violations_cumul[i] - violations_cumul[run_start - 1]
        print(f'run_cumul updated to: {run_cumul}')
    
        # Main mechanism
        # Happy path - total for this run is <= max_slow, so update solutions for start, length (i-start+1)
        if run_cumul <= max_slow:
            solutions[run_start] = i - run_start + 1
        # Unhappy path - keep moving start later (shrinking window) until total of window's violations fit within budget
        else:
            while run_cumul > max_slow:
                run_start += 1
                run_cumul = violations_cumul[i] - violations_cumul[run_start - 1]
            solutions[run_start] = i - run_start + 1
        print(f'solutions updated to: {solutions}')
              
    print(f'solutions: {solutions}')
    solution = max(solutions.items(), key=lambda kv:(kv[1], -kv[0]))
    print(f'solution: {solution}')
    if solution[1] == 0:
        return None
    else:
        return solution

# Complexity:
# 1. Outer loop --> O(n)
# 2. While --> Inside loop, but only runs forward with max n steps, so additive, not mult --> O(n)
# 3. Max --> O(n)
# Total: O(3n) --> O(n) with storage of O(n) items 


# Test cases
lat = [120, 300, 90, 80, 450, 100, 95]
assert longest_fast_stretch(lat, 200, 1) == (2, 5)
assert longest_fast_stretch(lat, 200, 0) == (2, 2)
assert longest_fast_stretch(lat, 200, 2) == (0, 7)
assert longest_fast_stretch([], 100, 1) is None
assert longest_fast_stretch([500, 600], 100, 0) is None
assert longest_fast_stretch([500, 600], 100, 1) == (0, 1)
assert longest_fast_stretch([200, 200, 201], 200, 0) == (0, 2)
assert longest_fast_stretch([50], 100, 0) == (0, 1)
assert longest_fast_stretch([300, 50, 50, 300, 50], 100, 1) == (1, 4)
print("all tests passed")