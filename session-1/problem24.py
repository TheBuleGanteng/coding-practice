'''
Problem 24: Longest truck load

Time limit: 25 minutes, including writing your own tests. Aim for working code by about minute 20.

Packages roll off a conveyor in order. 
Each one is recorded as a dict with an "id" and a weight in "kg". 
A truck can carry at most capacity kg. 
The dispatcher wants the longest run of consecutive packages whose total weight is ≤ capacity.

Function name: longest_load

Arguments:
packages: a list of dicts, each like {"id": "A", "kg": 8}. id is a string, and kg is an int ≥ 0. 
The list can contain up to 1,000,000 entries.
capacity: an int ≥ 0.

Requirements:
1. Return (first_id, last_id): the ids of the first and last package in the longest qualifying run.
2. If runs tie for the longest, return the one that starts earliest.
3. If no run of at least one package qualifies, return None.
'''
'''
THOUGHTS
1. Initial guard
2. Loop
3. Unpack packages --> for i, (id, kg) in packages:
4. List for each package id (strings)
RETURN
solutions = {} # k= start, v=length
best_solution = max(solutions.items(), key=lambda kv:(kv[1], -kv[0]))
if best_solution[1] == 0:
    return None
else:
    start = best_solution[0]
    end = start + best_solution[1] - 1
soluton = (ids[start], ids[end])
return solution
'''

def longest_load(packages: list, capacity: int):
    idens = []
    cumul_tot = []
    solutions = {} # k= start, v=length

    if len(packages) == 0:
        return None
    
    for i, package in enumerate(packages):
        iden = package['id'] 
        kg = package['kg']
        print(f'i: {i}, package: {package}, iden: {iden}, kg: {kg}')
        
        idens.append(iden)
        print(f'idens: {idens}')
        
        if i == 0:
            start = 0
            cumul_tot.append(kg)
        else:
            cumul_tot.append(cumul_tot[i-1] + kg)
        print(f'cumul_tot: {cumul_tot}')
        
        if start == 0:
            run_tot = cumul_tot[i]
        else:
            run_tot = cumul_tot[i] - cumul_tot[start - 1]
        print(f'run_tot: {run_tot}')
        
        if run_tot <= capacity:
            solutions[start] = i - start + 1
        else:
            while run_tot > capacity:
                start += 1
                run_tot = cumul_tot[i] - cumul_tot[start - 1]
            solutions[start] = i - start + 1
        print(f'solutions: {solutions}')
    
    best_solution = max(solutions.items(), key=lambda kv:(kv[1], -kv[0]))
    print(f'best_solution: {best_solution}')
    if best_solution[1] == 0:
        return None
    else:
        start = best_solution[0]
        end = start + best_solution[1] - 1
    solution = (idens[start], idens[end])
    print(f'solution: {solution}')
    return solution
                
# Complexity:
# Loop: O(n)
# While: O(n)
# Max: O(n)
# Total: O(n) w/ memory O(n)

# Examples

p = [{"id": "A", "kg": 8}, {"id": "B", "kg": 3}, {"id": "C", "kg": 4},
     {"id": "D", "kg": 9}, {"id": "E", "kg": 2}, {"id": "F", "kg": 2},
     {"id": "G", "kg": 3}]
q = [{"id": "A", "kg": 8}, {"id": "B", "kg": 1}, {"id": "C", "kg": 1}]
r = [{"id": "A", "kg": 8}, {"id": "B", "kg": 1}, {"id": "C", "kg": 1}]
assert longest_load(p, 10) == ("E", "G")
assert longest_load([{"id": "Z", "kg": 20}], 10) is None
assert longest_load([], 10) is None
assert longest_load(q, 10) == ("A", "C")
assert longest_load(q, 9) == ("A", "B")
assert longest_load(r, 2) == ("B", "C")