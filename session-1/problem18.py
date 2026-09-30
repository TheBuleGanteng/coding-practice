'''
Problem 18: Longest playlist within a limit

Time limit: 25 minutes.

A music app has a list of song durations in minutes, in play order. 
The team wants the longest run of consecutive songs whose total duration is ≤ max_minutes, 
returned as the list of durations themselves.

Function name: longest_playlist

Arguments:
durations: a list of ints, each ≥ 0.
max_minutes: an int ≥ 0.

Requirements:
1. Return a list: the durations in the longest qualifying run, in their original order. For example, if the best run covers positions 2, 3 and 4, return [durations[2], durations[3], durations[4]].
2. If runs tie for the longest, return the one that starts earliest.
3. If no run of at least 1 song qualifies, or durations is empty, return None.
4. Target: O(n).
'''
'''
1. Initial guard
2. Calculate cumul total from bgn, store in cumul_tot = {key=starting position, value= cumulative total from start}
3. Calculate run_total from start
4. Typical check
5. At end, index back into durations to get a list of items

Return
solutions = dict w/ key= starting index, value = list (song1, song2, etc)
solution = max(solutions.items(), key=lambda kv:(kv[len[1]], -kv[0]))
return solution
'''
def longest_playlist(durations: list, max_minutes: int):
    
    cumul_tot = []  
    solutions = {} # key = index pos of run start, value = list of durations in run 
    
    # Guard: empty durations
    if len(durations) == 0 or min(durations) > max_minutes:
        return None
    
    # Loop
    for i, duration in enumerate(durations):
        
        # Guard against i-1 out of range
        if i == 0:
            start = 0
            cumul_tot.append(duration)
        else:
            cumul_tot.append(cumul_tot[i-1] + duration)
        print(f'cumul_tot: {cumul_tot}')
        
        # Guard against start-1 out of range
        if start == 0:
            run_tot = cumul_tot[i]
        else:
            run_tot = cumul_tot[i] - cumul_tot[start-1]
            
        # Check against budget
        # Happy path
        if run_tot <= max_minutes:
            solutions[start] = i - start + 1
        # Unhappy path
        else:
            while run_tot > max_minutes:
                start += 1
                run_tot = cumul_tot[i] - cumul_tot[start-1]
            solutions[start] = i - start +1
    

    print(f'solutions: {solutions}')
    best_solution = max(solutions.items(), key=lambda kv:(kv[1], -kv[0]))
    print(f'best_solution: {best_solution}')
    start_pos = best_solution[0]
    end_pos = start_pos + best_solution[1]
    solution = durations[start_pos:end_pos]
    print(f'start_pos: {start_pos}, end_pos: {end_pos}, solution: {solution}')
    return solution

# Complexity: 
# 1. loop --> O(n)
# 2. While (only moves fwd, additive) --> O(n)
# 3. Max --> O(n)
# Tot = O(3n) --> O(n) w/ memory O(n)    

# Test cases
d = [3, 5, 2, 2, 4, 1, 6]
assert longest_playlist(d, 8) == [2, 2, 4]
assert longest_playlist(d, 20) == [3, 5, 2, 2, 4, 1]
assert longest_playlist(d, 1) == [1]
assert longest_playlist(d, 0) is None
assert longest_playlist([], 5) is None
assert longest_playlist([0, 0], 0) == [0, 0]
assert longest_playlist([10], 10) == [10]
assert longest_playlist([4, 4, 4], 8) == [4, 4]
print("all tests passed")