'''
Problem 19: Longest charging session

Time limit: 25 minutes, including writing your own test cases.

An EV charging station logs the energy delivered in each 15-minute interval, in kWh, in order. 
To stay within its agreement with the grid, the station is allowed at most cap kWh across any run of 
consecutive intervals it reports as a single session. The operator wants to find the longest such session in the log.

Function name: longest_session

Arguments:
kwh: a list of ints, each ≥ 0. The list can contain up to 1,000,000 entries.
cap: an int ≥ 0.

Requirements:
1. Return (start, length, total): 
- the position of the first interval in the longest run of consecutive intervals whose total is ≤ cap, 
- the number of intervals in it, 
- and its total kWh.
2. If runs tie for the longest, return the one that starts earliest.
3. If no run of at least one interval qualifies, return None.
'''
'''
Return
solution --> triple

solutions --> k= starting pos, v= length of session
best_solution = max(solutions.items(), key=lambda kv:(kv[1], -kv[0]))
sp = best_solution[0]
end = sp + best_solution[1] 
session_total = cumul_tot[end] - cumul_tot[sp-1]
solition = best_solution.append(session_total)
'''

def longest_session(kwh: list, cap: int):
    cumul_tot = []
    solutions = {} # k= starting pos, v= length of session
    
    # Guard if orig list is empty or each interval is over cap
    if len(kwh) == 0 or min(kwh) > cap:
        return None
    
    # Loop
    for i, obs in enumerate(kwh):
        
        if i == 0:
            start = 0
            cumul_tot.append(obs)
        else:
            cumul_tot.append(cumul_tot[i-1] + obs)
        print(f'cumul_tot: {cumul_tot}')
        
        if start == 0:
            run_tot = cumul_tot[i]
        else:
            run_tot = cumul_tot[i] - cumul_tot[start - 1]
        print(f'run_tot: {run_tot}')
            
        # happy path
        if run_tot <= cap:
            solutions[start] = i - start + 1
        # unhappy path
        else:
            while run_tot > cap:
                start += 1
                run_tot = cumul_tot[i] - cumul_tot[start - 1]
            solutions[start] = i - start + 1
    
    print(f'solutions: {solutions}')
    
    # First, get the best run (e.g. longest run w/ earliest start)
    best_solution = max(solutions.items(), key=lambda kv:(kv[1], -kv[0]))
    print(f'best_solution: {best_solution}')
    
    # Second, get the total for that run
    # If best_solution[0] == 0 (i.e. the best run starts at [0]), need to avoid [-1] 
    start = best_solution[0]
    end = start + best_solution[1] - 1
    
    if start == 0:
        session_total = cumul_tot[end]
    else:
        session_total = cumul_tot[end] - cumul_tot[start - 1]
    print(f'start: {start}, end: {end}, session_total: {session_total}')
    
    # Add the total to the existing best_soluton (run start and run length) items
    solution = (best_solution[0], best_solution[1], session_total)
    print(f'solution: {solution}')
    return solution

# Complexity: O(n) w/ memory O(n)

# Examples
k = [5, 3, 8, 2, 2, 7, 1]
assert longest_session(k, 12) == (3, 4, 12)
assert longest_session([15, 20], 10) is None
assert longest_session([], 5) is None
assert longest_session(k, 30) == (0, 7, 28)
assert longest_session(k, 1) == (6, 1, 1)
assert longest_session([0, 0, 0], 0) == (0, 3, 0)
assert longest_session([10], 10) == (0, 1, 10)
assert longest_session([6, 6, 6], 12) == (0, 2, 12)
assert longest_session([4, 4, 1, 1, 4, 4], 8) == (1, 3, 6)
print("all tests passed")