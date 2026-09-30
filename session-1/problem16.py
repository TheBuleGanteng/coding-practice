'''
Time limit: 25 minutes.

A service writes one log line per minute, in the format "HH:MM LEVEL", where LEVEL is INFO, WARN or ERROR. 
The team wants the longest stretch of consecutive lines containing at most max_errors ERROR lines. WARN doesn't count as an error.

Function name: longest_calm_period

Arguments:
lines: a list of strings, each formatted "HH:MM LEVEL".
max_errors: an int ≥ 0.

Requirements:
1. Return (start_time, length). start_time is the "HH:MM" part of the first line in the longest qualifying stretch, 
and length is the number of lines in that stretch.
2. If stretches tie for the longest, return the one that starts earliest.
3. If no stretch of at least 1 line qualifies, or lines is empty, return None.
Target: O(n).
'''

'''
Thoughts: 
1. Will potentially need to parse text to start time (HH:MM format) and msg type from initial format: HH:MM LEVEL, turning those into tuples
2. Can turn list into a bool where 0 != error and 1 = error. From there, it's a typical sliding window with budget

Return:
solution = (start_time, length)

solution = max(solutions.items(), key=lambda kv:(kv[1], -kv[0]))
if solution(1) == 0:
    return None
else:
    return solution

'''

def longest_calm_period(lines: list, max_errors: int):
    # lines format: HH:MM LEVEL
    cumul_tot = [] # values = total until that pointsolution
    solutions = {} # key= index position of each run's start, value= length of run
    
    # Guard: lines is empty
    if len(lines) == 0:
        return None
    
    for i, line in enumerate(lines):
        
        # Splice each line
        index = (line.index(" "))
        timestamp = line[:index]
        msg = line[index+1:]
        if msg == "ERROR":
            msg_val = 1
        else:
            msg_val = 0
        print(f'index: {index}, msg: {msg}')
        
        
        # Generate cumul totals for errors
        # Handle first iteration to avoid [i-1]
        if i == 0:
            start = 0
            cumul_tot.append(msg_val)
        else:
            prior_total = cumul_tot[i-1]
            cumul_tot.append(prior_total + msg_val)
        print(f'updated cumul_tot: {cumul_tot}')
        
        # Generate cumul tot for current run
        # Handle if start is 0 to avoid [start-1]
        if start == 0:
            cumul_run = cumul_tot[i]
        else:
            cumul_run = cumul_tot[i] - cumul_tot[start-1] 
        
        # Start checking against budget
        # Happy path: update solutions
        if cumul_run <= max_errors:
            solutions[start] = i - start + 1
        # Unhappy path: while loop
        else:
            while cumul_run > max_errors:
                start += 1
                cumul_run = cumul_tot[i] - cumul_tot[start-1] 
            solutions[start] = i - start + 1

    solution_notime = max(solutions.items(), key=lambda kv:(kv[1], -kv[0]))
    print(f'solution_notime: {solution_notime}')
    if solution_notime[1] == 0:
        print(f'solution_notime: {solution_notime}, returning None')
        return None
    else:
        line_num = solution_notime[0]
        solution = (lines[line_num].split(" ")[0], solution_notime[1])
        return solution

# Complexity:
# 1. Outer loop --> O(n)
# 2. While only moves forward --> not multiplicative --> O(n)
# 3. Max --> O(n)
# Total = O(3n) --> O(n) w/ memory O(n)

# Test cases
logs = ["09:00 INFO", "09:01 ERROR", "09:02 WARN", "09:03 INFO", "09:04 ERROR", "09:05 INFO"]
assert longest_calm_period(logs, 1) == ("09:00", 4)
assert longest_calm_period(logs, 0) == ("09:02", 2)
assert longest_calm_period(logs, 2) == ("09:00", 6)
assert longest_calm_period([], 1) is None
assert longest_calm_period(["10:00 ERROR"], 0) is None
assert longest_calm_period(["10:00 ERROR"], 1) == ("10:00", 1)
assert longest_calm_period(["10:00 WARN", "10:01 WARN"], 0) == ("10:00", 2)
assert longest_calm_period(["10:00 ERROR", "10:01 INFO", "10:02 ERROR", "10:03 INFO", "10:04 INFO"], 1) == ("10:01", 4)
print("all tests passed")