# type: ignore
'''
Problem 21: Longest frugal streak

Time limit: 25 minutes, including writing your own tests. 
Aim for working code by about minute 20.

A budgeting app records how much a user spent each day, in order. 
The first entry is day 1, the second is day 2, and so on. 
The app wants to highlight the user's longest streak of consecutive days whose combined spending is ≤ allowance.

Function name: longest_frugal_streak

Arguments:
spend: a list of ints, each ≥ 0. The list can contain up to 1,000,000 entries.
allowance: an int ≥ 0.

Requirements:
1. Return (first_day, last_day): the day numbers of the first and last day of the longest qualifying streak.
2. If streaks tie for the longest, return the one that starts earliest.
3. If no streak of at least one day qualifies, return None.
'''
'''
solutions --> k= start, v=length
best_solution = max(solutions.items(), key=lambda kv:[kv[1], -kv[0]])

# Guard: Best solution has len(0)
if best_solution[1] == 0:
    return None

# Find first, last day
first_day = best_solution[0]
last_day = first_day + best_solution[1] - 1
solution = (first_day, last_day) 
'''

def longest_frugal_streak(spend: list, allowance: int):
    cumul_tot = [] 
    solutions = {} # k=start, v=length
    
    # Guard
    if len(spend) == 0 or min(spend) > allowance:
        return None
    
    # loop
    for i, day in enumerate(spend):
        
        if i == 0:
            start = 0
            cumul_tot.append(day)
        else:
            cumul_tot.append(cumul_tot[i-1]+day)
        
        if start == 0:
            run_tot = cumul_tot[i]
        else:
            run_tot = cumul_tot[i] - cumul_tot[start - 1]
            
        if run_tot <= allowance:
            solutions[start] = i - start + 1
        else:
            while run_tot > allowance:
                start +=1
                run_tot = cumul_tot[i] - cumul_tot[start - 1]
            solutions[start] = i - start + 1

    # Get longest run w/ earliest start
    best_solution = max(solutions.items(), key=lambda kv:[kv[1], -kv[0]])
    print(f'best_solution: {best_solution}')

    # Guard: Best solution has len(0)
    if best_solution[1] == 0:
        print(f'best_solution[0]: {best_solution[0]}, returning None')
        return None

    # Find first, last day
    first_day = best_solution[0]
    last_day = first_day + best_solution[1] - 1
    solution = (first_day+1, last_day+1) 
    print(f'first_day: {first_day}, last_day: {last_day}, solution: {solution}')
    return solution

#Complexity:
#1. Loop --> O(n)
#2. While (moves forward only, so additive) --> O(n)
#3. Max --> O(n)
# Total = O(n) w/ memory O(n)

#Examples
assert longest_frugal_streak([12, 4, 6, 20, 3, 3, 4, 9], 13) == (5, 7)
assert longest_frugal_streak([25], 20) is None
assert longest_frugal_streak([], 20) is None
assert longest_frugal_streak([1,2,3,4], 200) == (1,4)
assert longest_frugal_streak([1,2,3,4], 6) == (1,3)
assert longest_frugal_streak([1,2,3,4], 9) == (1,3)
assert longest_frugal_streak([8,2,3,4], 9) == (2,4)
