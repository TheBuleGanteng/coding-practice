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
+ 3. If readings is empty, return None.
4. Brute force is fine. State its complexity.
'''


# Ideas
# 1. Initial check per req 3
# 2. Outside loop: loops through each item in readings (i)
# 3. Inner loop: Loops through each item after i, e.g. [readings[i+1:]], (j)
# 4. Checking for variation of current item vs. max, min --> Store max and min in dedicated variables, compare newest number to each to determine if variation > tolerance
# 5. As long as variation < tolerance, increment counter (len) and update solution dict[i]=len
# 6. Return solution with greatest len (max value in dict)

def longest_stable_stretch(readings: list, tolerance: int):
    solutions = {}
    
    # Req 3
    if len(readings) == 0:
        return None
   
    for i, readingi in enumerate(readings): # Outer loop = starting position and char of a given solution
        length = 1
        val_max = readingi
        val_min = readingi
        solutions[i] = length
        
        for j, readingj in enumerate(readings[i+1:]): # Inner loop = checks the numbers subsequent to i
            diff_max = val_max - readingj # Positive if new number is new max
            diff_min = val_min - readingj # Positive if new number is new min
            
            if abs(diff_max) > tolerance or abs(diff_min) > tolerance: # Tolerance exceeded, break out of inner loop and restart w/ next i 
                print(f'breaking out b/c exceeded tolerance')
                break
            else:
                length = length + 1 # Update counter
                val_max = max(val_max, readingj) # Update max
                val_min = min(val_min, readingj) # Update min
                solutions[i] = length
    
    print(f'solutions: {solutions}')
    result = max(solutions.items(), key=lambda kv:(kv[1], -kv[0]))
    print(f'returning result: {result}') 
    return result
                    

# Complexity:
# 1. Outer loop = O(n)
# 2. Inner loop = ~O(n)
# 3. Inside inner loop, fixed work w/r/t n (e.g. comparisons and updates)
# 4. Final max = O(n)
# Total = O(n) * O(n) + O(n) --> O(n^2 + n) --> O(n^2)

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