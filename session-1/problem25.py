'''
Problem 25: Longest dry spell

Time limit: 25 minutes, including writing your own tests. Aim for working code by about minute 20.

A weather station logs daily rainfall as strings in the format "YYYY-MM-DD:MM". 
The part before the colon is the date, and the part after it is the rainfall in millimetres, 
a non-negative int that can have several digits. For example, "2026-07-01:12" means 12 mm on 1 July 2026. 
The entries are in date order, one per day. 
A farmer wants the longest run of consecutive days whose total rainfall is ≤ max_mm.

Function name: longest_dry_spell

Arguments:
log: a list of strings in the format "YYYY-MM-DD:MM". The list can contain up to 1,000,000 entries.
max_mm: an int ≥ 0.

Requirements:
1. Return (first_date, last_date): the date strings of the first and last day in the longest qualifying run.
2. If runs tie for the longest, return the one that starts earliest.
3. If no run of at least one day qualifies, return None.
'''
'''
THOUGHTS
1. Initial guard
2. loop
3. split string on ":" --> item.split(":")
4. List of dates = []

RETURN
solutions = {} # k=start, v=length
best_solution = max(solutions.items(), key=lambda kv:(kv[1], -kv[0]))
if best_solution[1] == 0:
    return None
else:
    start_index = best_solution[0]
    end_index = start_index + best_solution[1] - 1 
    print(f'start_index: {start_index}, end_index: {end_index}')
    start= dates[start_index]
    end = dates[end_index]
    solution = start, end
    return solution
'''

def longest_dry_spell(log: list, max_mm: int):
    dates = []
    cumul_tot = []
    solutions = {} # k=start, v=length
    
    if len(log) == 0:
        return None
    
    for i, item in enumerate(log):
        date, meas = item.split(":")
        meas = int(meas)
        dates.append(date)
        print(f'date: {date}, i: {i}, meas: {meas}, dates: {dates}')
        
        if i == 0:
            start = 0
            cumul_tot.append(meas)
        else:
            cumul_tot.append(cumul_tot[i-1] + meas)
        print()
        
        if start == 0:
            run_tot = cumul_tot[i]
        else:
            run_tot = cumul_tot[i] - cumul_tot[start - 1]
            
        if run_tot <= max_mm:
            solutions[start] = i - start + 1
        else:
            while run_tot > max_mm:
                start += 1
                run_tot = cumul_tot[i] - cumul_tot[start - 1]
            solutions[start] = i - start + 1
    
    best_solution = max(solutions.items(), key=lambda kv:(kv[1], -kv[0]))
    if best_solution[1] == 0:
        return None
    else:
        start_index = best_solution[0]
        end_index = start_index + best_solution[1] - 1 
        print(f'start_index: {start_index}, end_index: {end_index}')
        start= dates[start_index]
        end = dates[end_index]
        solution = start, end
        return solution
# Complexity: 
# 1. Loop: O(n)
# 2. While (additive): O(n)
# 3. Max: O(n)
# Total: O(3n)->O(n) w/ memory O(n)

#Examples
log = ["2026-07-01:12", "2026-07-02:0", "2026-07-03:3", "2026-07-04:20",
       "2026-07-05:1", "2026-07-06:2", "2026-07-07:4", "2026-07-08:9"]
q = ["2026-07-01:12", "2026-07-02:0", "2026-07-03:3"]
r = ["2026-07-01:12", "2026-07-02:15", "2026-07-03:100"]
s = ["2026-07-01:12", "2026-07-02:3", "2026-07-03:2"]

assert longest_dry_spell(log, 8) == ("2026-07-05", "2026-07-07")
assert longest_dry_spell(["2026-08-01:30"], 10) is None
assert longest_dry_spell([], 10) is None
assert longest_dry_spell(s, 5) == ("2026-07-02", "2026-07-03")
assert longest_dry_spell(log, 200) == ("2026-07-01", "2026-07-08")