'''
Problem 23: Longest low-power run

Time limit: 25 minutes, including writing your own tests. 
Aim for working code by about minute 20.

A phone logs its battery use once a minute, as (time_label, mwh) tuples in order. 
The power team wants the longest run of consecutive minutes whose total energy use is ≤ budget mWh.

Function name: longest_low_power_run

Arguments:
readings: a list of (time_label, mwh) tuples. time_label is a string like "08:00", and mwh is an int ≥ 0. 
The list can contain up to 1,000,000 entries.
budget: an int ≥ 0.

Requirements:
1. Return (start_time, length): the time_label of the first minute in the longest qualifying run, and the number of minutes in it.
2. If runs tie for the longest, return the one that starts earliest.
3. If no run of at least one minute qualifies, return None.
'''
'''
THOUGHTS:
1. Initial guard
2. Loop
3. Parse text based on ",". Be sure to remove space after comma
4. 
RETURN:
solutions = {} # k=start, v=length
solution = max(solutions.items(), key=lambda kv:(kv[1], -kv[0]))
if solution[1] == 0:
    return None
else:
    return solution
'''
def longest_low_power_run(readings: list, budget: int):
    times = {}
    cumul_tot = []
    solutions = {} # k=start, v=length

    if len(readings) == 0:
        return None 

    for i, (start_time, mwh) in enumerate(readings):
        times[i] = start_time
        print(f'times: {times}')
        
        if i == 0:
            start = 0
            cumul_tot.append(mwh)
        else:
            cumul_tot.append(cumul_tot[i-1] + mwh)
        print(f'cumul_tot: {cumul_tot}')
        
        if start == 0:
            run_tot = cumul_tot[i]
        else:
            run_tot = cumul_tot[i] - cumul_tot[start-1]
            
        if run_tot <= budget:
            solutions[start] = i - start + 1
        else:
            while run_tot > budget:
                start += 1
                run_tot = cumul_tot[i] - cumul_tot[start-1]
            print(f'finished while with i: {i}, run_tot: {run_tot}')
            solutions[start] = i - start + 1
    
    print(f'solutions: {solutions}')
    best_solution = max(solutions.items(), key=lambda kv:(kv[1], -kv[0]))
    print(f'best_solution: {best_solution}')
    if best_solution[1] == 0:
        return None
    else:
        sol1 = times[best_solution[0]]
        sol2 = best_solution[1]
        solution = (sol1, sol2)
        print(f'solution: {solution}')
        return solution

#  Complexity O(n) w/ memory O(n)

#Examples
r = [("08:00", 30), ("08:01", 50), ("08:02", 10), ("08:03", 20),
     ("08:04", 15), ("08:05", 60), ("08:06", 5)]
s = [("08:00", 30), ("08:01", 50), ("08:02", 90), ("08:03", 120),
     ("08:04", 115), ("08:05", 60), ("08:06", 5)]
assert longest_low_power_run(r, 50) == ("08:02", 3)
assert longest_low_power_run([("09:00", 80)], 50) is None
assert longest_low_power_run([], 50) is None
assert longest_low_power_run(r, 500) == ("08:00", 7)
assert longest_low_power_run(r, 190) == ("08:00", 7)
assert longest_low_power_run(s, 65) == ("08:05", 2)
