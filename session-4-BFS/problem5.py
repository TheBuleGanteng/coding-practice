'''
Session 4, Problem 5: Count the islands (timed)

Time limit: 30 minutes, including writing your own tests. Aim for working code by about minute 24. Hard stop at 45 minutes. Start with the design block: what you scan, what bfs does each time, and what’s shared across bfs calls.

Function name: count_islands

Argument:

grid: a list of lists of strings, where each string is "L" (land) or "W" (water). Every row has the same length, and there’s at least one row.

An island is a group of land cells that are all connected to each other by moving up, down, left, or right through land cells, and not connected to any other land cell. Returns the number of islands, as an int. Returns 0 if there’s no land.
'''
from collections import deque


def count_islands(grid: list):
    height = len(grid)
    width = len(grid[0])
    
    def in_bounds(y, x):
        if y < 0 or y > height -1 or x < 0 or x > width - 1:
            return False
        return True
    
    def not_water(y, x):
        if grid[y][x] == "W":
            return False
        return True
    
    def bfs(y, x, visited):
        
        # Declare deque, add curent cell to queue and vistied
        queue = deque()
        queue.append((y, x))
        visited.add((y,x))        
        
        while len(queue) > 0:
            # Pop oldest item from queue
            y_current, x_current = queue.popleft()
            # Start loop
            for dy, dx in [(-1,0), (1,0), (0,-1), (0, 1)]:
                y_new = y_current + dy
                x_new = x_current + dx
                # Check that new cell is in bounds
                if not in_bounds(y_new, x_new):
                    continue
                # If new cell is legit, add to queue and visited
                if (y_new, x_new) not in visited and not_water(y_new, x_new):
                    queue.append((y_new, x_new))
                    visited.add((y_new, x_new))
    
    islands = 0
    visited = set()
    
    # Loop over cells
    for y in range(height):
        for x in range(width):
            if (y, x) not in visited and not_water(y,x):
                islands += 1
                bfs(y, x, visited)
    return islands            
    
        
# Complexity: O(height x width)
# Memory: O(height x width)
    


# Example tests:


grid = [
    ["L", "L", "W", "W"],
    ["W", "L", "W", "L"],
    ["W", "W", "W", "L"],
    ["L", "W", "W", "W"],
]
assert count_islands(grid) == 3

grid = [
    ["W", "W"],
    ["W", "W"],
]
assert count_islands(grid) == 0