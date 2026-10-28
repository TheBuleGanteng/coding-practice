'''
Session 4, Problem 7: Color regions (timed)

Time limit: 30 minutes, including writing your own tests. Aim for working code by about minute 24. Hard stop at 45 minutes. Start with the design block: what you scan, what bfs does each time, and what’s shared across bfs calls.

Function name: count_regions

Argument:

grid: a list of lists of strings, where each string is a single uppercase letter, such as "R", "G", or "B", representing a color. Every row has the same length, and there’s at least one row.

A region is a group of cells that all have the same color and are connected to each other by moving up, down, left, or right through cells of that color, and not connected to any other cell of that color. Every cell belongs to exactly one region. Returns the number of regions, as an int.
'''
from collections import deque

def count_regions(grid: list):
    height = len(grid)
    width = len(grid[0])
    
    def in_bounds(y, x):
        if y < 0 or y > height - 1 or x < 0 or x > width - 1:
            return False
        return True
    
    def same_color(y_current, x_current, y_new, x_new):
        if grid[y_current][x_current] != grid[y_new][x_new]:
            return False
        return True
    
    def bfs(y: int, x: int, visited: set):
        # Declare and populate deque, visited
        queue = deque() 
        queue.append((y, x))
        visited.add((y, x))
        
        # Start loop
        while len(queue) > 0:
            # Pop oldest item
            y_current, x_current = queue.popleft()
            for dy, dx in [(-1,0), (1,0), (0,-1), (0,1)]:
                y_new = y_current + dy
                x_new = x_current + dx
                if (y_new, x_new) not in visited and in_bounds(y_new, x_new) and same_color(x_current=x_current, y_current=y_current, x_new=x_new, y_new=y_new):
                    queue.append((y_new, x_new))
                    visited.add((y_new, x_new))
        return regions
                    
    # Initialize visited
    visited = set()
    regions = 0
    
    for y in range(height):
        for x in range(width):
            if (y,x) not in visited:
                regions += 1
                bfs(y, x, visited)
    print(f'regions: {regions}')
    return regions
    
# Complexity: O(height x width)
# Memory: O(height x width)
    
    
# Example tests:


grid = [
    ["R", "R", "G"],
    ["G", "R", "G"],
    ["G", "B", "B"],
]
assert count_regions(grid) == 4

grid = [
    ["R"],
]
assert count_regions(grid) == 1

