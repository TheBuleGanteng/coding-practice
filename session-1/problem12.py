'''
Problem 12: Longest stable stretch

Time limit: 25 minutes.

A sensor reports one reading per minute. 
The team wants the longest stretch of consecutive minutes where the readings stayed stable, 
meaning the highest and lowest readings in the stretch differ by no more than a tolerance.

Function name: longest_stable_stretch

Arguments:
readings: a list of ints, one per minute.
tolerance: an int ≥ 0.

Requirements:

1. Return a tuple (start, length) for the longest run of consecutive readings where (largest reading − smallest reading) ≤ tolerance.
2. If several runs tie for the longest, return the one that starts earliest.
3. If readings is empty, return None.
4. Brute force is fine. State its complexity.
'''


def longest_stable_stretch(readings: list, tolerance: int):
    values = []
    solutions = {}
    
    # Req 3
    if len(readings) == 0:
        return None

    # Start outer loop
    for i, readingi in enumerate(readings):
        values =[]
        values.append(readingi)
        counter = 1
        solutions[i] = counter
        print(f'i: {i}, counter: {counter}, solutions: {solutions}')
        
        # Start inner loop
        for j, readingj in enumerate(readings[i+1:]):
            
            # Ensure that next item is within tolerance
            if abs(readingj - max(values)) > tolerance or abs(readingj - min(values)) > tolerance:
                print(f'readingj:{readingj}, max(values): {max(values)}, min(values): {min(values)}')
                print(f'tol exceeded, breaking out')
                break
            else:
                values.append(readingj)
                counter = counter + 1
                solutions[i] = counter
                print(f'i:{i}, j:{j}, values:{values}, counter:{counter}, solutions[i]: {solutions[i]}')
        
        # If we reach end of string w/o tolerance violation
        #solutons[i] = counter
        
    # Find best solution
    print(f'solutions: {solutions}')
    answer = max(solutions.items(), key=lambda kv:[kv[1], -kv[0]])
    print(f'answer: {answer}')
    return answer

# Complexity:
# 1. One outer loop (i) --> O(n)
# 2. One inner loop (k) --> ~O(n)
# 3. Inside inner loop, I run min and max at most 1 time each O(2n)  
# 3. Finding best solution via max --> O(n)
# Total: O(n + n * n * 2n) --> O(n^3)

# Test cases
assert longest_stable_stretch([5, 6, 5, 9, 9, 10, 2], 1) == (0, 3)
assert longest_stable_stretch([], 3) is None
assert longest_stable_stretch([7], 0) == (0, 1)
assert longest_stable_stretch([4, 4, 4, 4], 0) == (0, 4)
assert longest_stable_stretch([1, 3, 5, 7], 1) == (0, 1)
assert longest_stable_stretch([1, 3, 5, 7], 2) == (0, 2)
assert longest_stable_stretch([10, 1, 2, 3, 2, 10], 2) == (1, 4)
assert longest_stable_stretch([3, 8, 3, 8], 4) == (0, 1)
assert longest_stable_stretch([2, 1, 2, 1, 5, 6, 5, 6], 1) == (0, 4)
print("all tests passed")