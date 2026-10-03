# type: ignore
'''
Problem 17: Longest affordable span

Time limit: 25 minutes.

A procurement tool has a list of daily prices, in order. 
The team wants the longest span of consecutive days whose total price is ≤ budget.

Function name: longest_affordable_span

Arguments:
prices: a list of ints, each ≥ 0.
budget: an int ≥ 0.

Requirements:
1. Return (start, end): the positions of the first and last day of the longest qualifying span, both included. 
For example, a span covering positions 4, 5 and 6 is returned as (4, 6).
2. If spans tie for the longest, return the one that starts earliest.
3. If no span of at least 1 day qualifies, or prices is empty, return None.
4. Target: O(n).
'''
'''
Thoughts:
1. Need span wherein TOTAL price <= budget
2. Do typical sliding window w/ budget
3. At end, take starting point + length to get ending point
4. Return starting point, ending point

Return
solution = (start, end) <-- index positions

solutions = {} key = start
solutions = 
'''
def longest_affordable_span(prices: list, budget: int):
    cumul_tot = []
    solutions = {} # key = start pos, value = total
    
    # Guard: Prices not empty
    if len(prices) == 0:
        return None
    
    # Start loop
    for i, price in enumerate(prices):
        
        # Guard against i-1
        if i == 0:
            start = 0
            cumul_tot.append(price)
        else:
            cumul_tot.append(cumul_tot[i-1]+price)
        
        # Guard against start -1
        if start == 0:
            cumul_run = cumul_tot[i]
        else:
            cumul_run = cumul_tot[i] - cumul_tot[start-1]
        
        # Happy path
        if cumul_run <= budget:
            solutions[start] = i - start + 1
        # Unhappy path
        else:
            while cumul_run > budget:
                start += 1
                cumul_run = cumul_tot[i] - cumul_tot[start-1]
            solutions[start] = i - start + 1
    
    print(f'solutions: {solutions}')
    solution_wo_end = max(solutions.items(), key=lambda kv:(kv[1], -kv[0]))
    print(f'solution_wo_end: {solution_wo_end}')
    if solution_wo_end[1] == 0:
        return None
    
    # Find position in orig list corresponding to solution[1]
    end = solution_wo_end[0] + solution_wo_end[1] - 1
    solution = (solution_wo_end[0], end)
    print(f'solution: {solution}')
    return solution

# Complexity: 
#1. Loop --> O(n)
#2. While only moves forward, so additive --> O(n)
#3. max --> O(n)
# Total --> O(3n) --> O(n) w/ memory O(n)

# Test cases
p = [4, 2, 1, 7, 1, 1, 3]
assert longest_affordable_span(p, 6) == (4, 6)
assert longest_affordable_span(p, 10) == (2, 5)
assert longest_affordable_span(p, 3) == (1, 2)
assert longest_affordable_span([], 5) is None
assert longest_affordable_span([9, 8], 5) is None
assert longest_affordable_span([5], 5) == (0, 0)
assert longest_affordable_span([0, 0, 0], 0) == (0, 2)
assert longest_affordable_span([3, 3, 3, 3], 6) == (0, 1)
print("all tests passed")