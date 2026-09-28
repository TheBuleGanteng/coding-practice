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

def range_totals(counts: list, queries: list):
    results = [] # List to hold results
    
    
    # inital loop looks at each query
    for query in queries:
        query_start = query[0]
        query_end = query[1]
        
        
        # find the position of query_start in counts
        total = sum(counts[query_start:query_end+1])
        print(f'query: {query}, query_start: {query_start}, query_end: {query_end}, total: {total}')
        results.append(total)
        print(f'results: {results}')

    return results

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
