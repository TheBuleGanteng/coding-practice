'''
Session 4, Problem 4: Count the rooms (timed)

Time limit: 30 minutes, including writing your own tests. Aim for working code by about minute 24. Hard stop at 45 minutes. Start with the design block: what you scan, what the BFS does each time, and what you keep across BFS runs.

Function name: count_rooms

Argument:

grid: a list of lists of strings, where each string is "." (open) or "#" (wall). Every row has the same length, and there’s at least one row.

A room is a group of open cells that are all connected to each other by moving up, down, left, or right through open cells, and not connected to any other open cell. Returns the number of rooms in the grid, as an int. Returns 0 if there are no open cells.
'''
from collections import deque

def count_rooms(grid: list):
    height = len(grid)
    width = len(grid[0])
    
    
    
    def not_wall(y, x):
        if grid[y][x] == "#":
            return False
        return True
    
    def in_bounds(y, x):
        if y < 0 or y > height -1 or x < 0 or x > width -1:
            return False
        return True
    
    def bfs(y: int, x: int, visited: set):
        # Declare deque and populate with first cell, also add to the visited set
        queue = deque() 
        queue.append((y, x))
        visited.add((y,x))
        
        while len(queue) > 0:
            # Pop current cell
            y_current, x_current = queue.popleft()
            # Set up loop to explore neighboring cells
            for dy, dx in [(-1,0), (1,0), (0,-1), (0,1)]:
                y_new = y_current + dy
                x_new = x_current + dx
                # Check that new cell is in bounds
                if not in_bounds(y_new, x_new):
                    continue
                # Check that new cell is legit
                if (y_new, x_new) not in visited and not_wall(y_new, x_new):
                    # If cell is legit, append to both visited and queue
                    visited.add((y_new, x_new))
                    queue.append((y_new, x_new))
                            
    rooms = 0
    visited = set()
    for y in range(height):
        for x in range(width):
            # We don't want to call BFS if either (a) we have already visited this cell via a prior BFS call or (b) the cell is a wall
            if (y, x) not in visited and not_wall(y, x):
                rooms += 1
                bfs(y, x, visited)
    return rooms


# Complexity: O(height x width)
# Memory: O(height x width)

# Example tests:


grid = [
    [".", ".", "#", "."],
    ["#", "#", "#", "."],
    [".", "#", ".", "."],
]
assert count_rooms(grid) == 3

grid = [
    ["#", "#"],
    ["#", "#"],
]
assert count_rooms(grid) == 0