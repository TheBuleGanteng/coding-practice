'''
Problem 20: Longest low-traffic window

Time limit: 25 minutes, including writing your own tests. Aim for working code by about minute 20.

A router logs the packet count for each minute as a (minute_label, packets) tuple, in order. 
The network team wants the longest run of consecutive minutes whose total packet count is ≤ limit, to schedule maintenance.

Function name: longest_quiet_window

Arguments:
logs: a list of (minute_label, packets) tuples. minute_label is a string, and packets is an int ≥ 0. 
The list can contain up to 1,000,000 entries.
limit: an int ≥ 0.

Requirements:
Return (first_label, last_label): the labels of the first and last minute of the longest qualifying run.
If runs tie for the longest, return the one that starts earliest.
If no run of at least one minute qualifies, return None.
'''
'''
Thoughts
1. Initial guard
2. Unpack tuple in loop (minute_label, packets)
3. 
Return
sols --> k= start, v=length
best_sol = max(sols.items(), key=lambda kv:(kv[1], -kv[0])) --> best(start, length)
first_label = logs[best([0])[0]]
last_label = logs[best(best[1][0])]
sol = first_label, last_label

'''
def longest_quiet_window(logs: list, limit: int):
    cumul_tot = []
    sols = {} # k=start, v=len
    
    # Guard: logs is empty
    if len(logs) == 0:
        return None
    
    # loop 
    for i, (minute_label, packets) in enumerate(logs):
        
        # Guard for first loop
        if i == 0:
            start = 0
            cumul_tot.append(packets)
        else:
            cumul_tot.append(cumul_tot[i-1] + packets)
            
        # Guard
        if start == 0:
            run_cumul = cumul_tot[i]
        else:
            run_cumul = cumul_tot[i] - cumul_tot[start-1]
            
        # Testing v. budget
        if run_cumul <= limit:
            sols[start] = i - start + 1
        else:
            while run_cumul > limit:
                start += 1
                run_cumul = cumul_tot[i] - cumul_tot[start-1]
            sols[start] = i - start + 1

    best_sol = max(sols.items(), key=lambda kv:(kv[1], -kv[0]))
    print(f'best_sol:{best_sol}')
    
    if best_sol[1] == 0:
        return None
    
    start_pos = best_sol[0]
    end_pos = start_pos + best_sol[1] - 1
    print(f'start_pos:{start_pos}, end_pos:{end_pos}')
    first_label = logs[start_pos]
    last_label = logs[end_pos]
    sol = first_label[0], last_label[0]
    print(f'sol: {sol}')
    return sol

# Complexity:
# Loop --> O(n)
# While (forward, additive) --> O(n)
# Max --> O(n)
# Total = O(3n) --> O(n) w/ memory O(n)

# Testing
logs = [("00:00", 40), ("00:01", 70), ("00:02", 10), ("00:03", 20),
        ("00:04", 30), ("00:05", 90), ("00:06", 5)]
assert longest_quiet_window(logs, 60) == ("00:02", "00:04")
assert longest_quiet_window([("09:00", 100)], 50) is None
assert longest_quiet_window([], 60) is None
assert longest_quiet_window([("00:00", 40), ("00:01", 70), ("00:02", 10)], 600) == ("00:00", "00:02")