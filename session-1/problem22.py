
'''
Problem 22: Longest pick batch

Time limit: 25 minutes, including writing your own tests. Aim for working code by about minute 20.

A warehouse picker's cart holds at most capacity units. 
Orders arrive as strings in the format "SKU:QTY", for example "A1:3": the SKU is A1, and the quantity is 3 units. 
SKUs never contain a colon, and quantities are non-negative ints that can have several digits. 
The picker wants the longest run of consecutive orders whose total quantity is ≤ capacity.

Function name: longest_pick_batch

Arguments:
orders: a list of strings in the format "SKU:QTY". The list can contain up to 1,000,000 entries.
capacity: an int ≥ 0.

Requirements:
1. Return a list of the SKUs in the longest qualifying run, in their original order.
2. If runs tie for the longest, return the one that starts earliest.
3. If no run of at least one order qualifies, return None.
'''
'''
THOUGHTS
1. Need to parse the text in each order, based on ":"
2. 
RETURN
solutions = {} k=stat, v=len
best_solution = max(solutions.items(), key=lambda kv:(kv[1], -kv[0]))
print(f'best_solution: {best_solution})

start = best_solution[0]
if best_soluton[0] + best_solution[1] == 0:
    end = best_solution[1]
else:
    end = best_soluton[0] + best_solution[1] - 1

windowed = orders[start:end]

'''

def longest_pick_batch(orders: list, capacity: int):
    cumul_tot = []
    sku_list = []
    solutions = {} # k=stat, v=len
    
    if len(orders) == 0:
        return None

    for i, order in enumerate(orders):
        split = order.split(":")
        sku = split[0]
        quantity = int(split[1])
        sku_list.append(sku)
        print(f'sku: {sku}, quantity: {quantity}')

        if i == 0:
            start = 0
            cumul_tot.append(quantity)
        else:
            cumul_tot.append(cumul_tot[i-1]+quantity)
        
        if start == 0:
            run_tot = cumul_tot[i]
        else:
            run_tot = cumul_tot[i] - cumul_tot[start - 1]
        
        if run_tot <= capacity:
            solutions[start] = i - start + 1
        else:
            while run_tot > capacity:
                start += 1
                run_tot = cumul_tot[i] - cumul_tot[start - 1]
            solutions[start] = i - start + 1
    
    best_solution = max(solutions.items(), key=lambda kv:(kv[1], -kv[0]))
    print(f'best_solution: {best_solution}')

    # Eliminate solutions with len == 0
    if best_solution[1] == 0:
        return None

    start = best_solution[0]
    end = best_solution[0] + best_solution[1] - 1

    solution = sku_list[start:end+1]
    print(f'solution: {solution}')
    return solution
        
# Complexity: O(n) w/ memory O(n)


#Examples
orders = ["A1:3", "B2:9", "C3:2", "D4:2", "E5:4", "F6:8", "G7:1"]
assert longest_pick_batch(orders, 8) == ["C3", "D4", "E5"]
assert longest_pick_batch(["Z9:10"], 5) is None
assert longest_pick_batch([], 5) is None
assert longest_pick_batch(["A1:3", "B2:9", "C3:2"], 500) == ["A1", "B2", "C3"]
assert longest_pick_batch(["A1:5", "B2:9", "C3:2"], 11) == ["B2", "C3"]
