'''
Session 4, Problem 6: Largest island (timed)

Time limit: 30 minutes, including writing your own tests. Aim for working code by about minute 24. Hard stop at 45 minutes. Start with the design block: what you scan, what bfs does and returns, and what’s shared across bfs calls.

Function name: largest_island

Argument:

grid: a list of lists of strings, where each string is "L" (land) or "W" (water). Every row has the same length, and there’s at least one row.

An island is a group of land cells that are all connected to each other by moving up, down, left, or right through land cells, and not connected to any other land cell. 
Its size is the number of land cells in it. 
Returns the size of the largest island, as an int. Returns 0 if there’s no land.
'''

from collections import deque


def largest_island(grid: list):
    height = len(grid)
    width = len(grid[0])
    
    def in_bounds(y, x):
        if y < 0 or y > height - 1 or x < 0 or x > width - 1:
            return False
        return True
    
    def is_land(y, x):
        if grid[y][x] == "W":
            return False
        return True
    
    
    def bfs(y: int, x: int, visited: set, record: int):
        # Initialize count variable
        count = 1
        # Declare deque
        queue = deque()
        queue.append((y, x))
        visited.add((y,x))
        # Kick off loop
        while len(queue) > 0:
            y_current, x_current = queue.popleft()
            for dy, dx in [(-1,0), (1,0), (0, -1), (0, 1)]:
                y_new = y_current + dy
                x_new = x_current + dx
                # Ensure not out of bounds
                if (y_new, x_new) not in visited and in_bounds(y_new, x_new) and is_land(y_new, x_new):
                    queue.append((y_new, x_new))
                    visited.add((y_new, x_new))
                    count += 1
        return max(count, record)
    
    # Initialize visited
    visited = set() 
    record = 0
    # start looping
    for y in range(height):
        for x in range(width):
            if (y, x) not in visited and is_land(y, x):
                record = bfs(y, x, visited, record)
    # Return the size 
    print(f'record: {record}')
    return record
                     

# Complexity: O(height x width)
# Memory: O(height x width)
    

# Example tests:

grid = [
    ["L", "L", "W", "W"],
    ["W", "L", "W", "L"],
    ["W", "W", "W", "L"],
    ["L", "W", "W", "W"],
]
assert largest_island(grid) == 3

grid = [
    ["W", "W"],
    ["W", "W"],
]
assert largest_island(grid) == 0


grid = [
    ["L", "L", "W", "W"],
    ["W", "L", "W", "L"],
    ["W", "W", "W", "L"],
    ["L", "W", "W", "L"],
]
assert largest_island(grid) == 3 # Covers tie
