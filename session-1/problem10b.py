'''
Dashboard range totals

Time limit: 30 minutes total. Aim for about 10 minutes on Part A and 20 on Part B.

A monitoring dashboard stores request counts per minute. 
Users run many queries of the form "how many requests between minute X and minute Y?" 
You need to answer a batch of these queries.

Function name: range_totals

Arguments:
counts: a list of ints, one per minute, each ≥ 0.
queries: a list of (start, end) tuples of ints.

Requirements:

1. Return a list of totals, one per query, in the same order as the queries.
2. Each total is the sum of counts from index start to index end, including both ends. So (2, 4) means indices 2, 3 and 4.
3. Every query is valid: 0 ≤ start ≤ end < len(counts). You don't need to check.
4. An empty queries list returns [].

Part A: brute force. Answer each query directly. State the complexity in terms of n (the length of counts) and q (the number of queries).

Part B: efficient version. Same function, same tests. Target O(n + q): some setup work proportional to n, done once, and then each query answered in O(1). 
The guiding question: what could you compute once, up front, so that any range's total becomes a subtraction of two numbers?
'''

# High-level
# Brute force
# 1. Find the position of the first char in the query
# 2. Find the position of the second char in the query
# 3. Total between them, append to a list

# Efficient version (target O(n+q))
# 1. Compute a running total of counts[0] to counts[i] and store that in a dict O(n) times with either 1 or 2 things added each time
# 2. Then, when we have a query (starting index, ending index) we can simply say that dict[ending_index] - dict[starting_index] is the total between them O(q)
# Total: O(n + q). Extra space: O(n) for the totals dict.

def range_totals(counts: list, queries: list):
    totals = {}
    results = []
    
    # Populate the totals dict: for each position in counts, add that new position, plus the prior running total
    for i, count in enumerate(counts):
        # Handle case of first position (no lookback possible)
        if i == 0:
            totals[i] = counts[i]
        # if not first position, add value at [i] + dict value at [i-1]
        else:
            totals[i] = totals[i-1] + counts[i]
    print(f'totals: {totals}')
    
    # Subtract ending running total minus bgn running total: Done for each query (q)
    for query in queries:
        sum_ending = totals[query[1]]
        if query[0] == 0:
            sum_beginning = 0
        else:
            sum_beginning = totals[query[0]-1]
        print(f'sum_ending: {sum_ending}, sum_beginning: {sum_beginning}')
        
        results.append(sum_ending-sum_beginning)
        print(f'for query: {query}, results updated to: {results}')
        
    return results

# Complexity:
# 1. Running sums: O(n)
# 2. Queries: O(q)

# Test cases
counts = [3, 1, 4, 1, 5, 9, 2, 6]

assert range_totals(counts, [(0, 0)]) == [3]
assert range_totals(counts, [(0, 7)]) == [31]
assert range_totals(counts, [(2, 4)]) == [10]
assert range_totals(counts, [(5, 5)]) == [9]
assert range_totals(counts, [(1, 3), (4, 6)]) == [6, 16]
assert range_totals(counts, []) == []
assert range_totals([0, 0, 0], [(0, 2)]) == [0]
assert range_totals([10], [(0, 0), (0, 0)]) == [10, 10]
print("all tests passed")
