'''
Session 4, Problem 3: Escape the maze (timed)

Time limit: 30 minutes, including writing your own tests. Aim for working code by about minute 24. Hard stop at 45 minutes. Start with the design block: what goes in the queue, what you track for each cell, and how you’ll find the starting point.

Function name: escape_steps

Argument:

grid: a list of lists of strings. 
Each string is "." (open), "#" (wall), "S" (the start), or "E" (an exit). 
There is exactly one "S", and there may be any number of "E" cells, including none. 
Every row has the same length, and there’s at least one row.

Returns the smallest number of moves needed to get from "S" to the nearest "E", moving up, down, left, or right through non-wall cells, as an int. 
"S" and "E" cells can be moved through like open cells. 
Returns None if no exit can be reached.
'''

from collections import deque


def escape_steps(grid: list):
    height = len(grid)
    width = len(grid[0])
    
    def in_bounds(y, x):
        if y < 0 or y > height -1 or x < 0 or x > width - 1:
            return False
        return True
    
    def not_wall(y, x):
         if grid[y][x] == "#":
             return False
         return True
     
    def is_escape(y, x):
        if grid[y][x] == "E":
            return True
        return False
    
    def is_start(y, x):
        if grid[y][x] == "S":
            return True
        return False
    
    # Step 1: Find starting point S
    start = (0,0)
    for y in range(height):
        for x in range(width):
            if is_start(y, x):
                start = (y, x)
    
    # unpak the start
    y_start, x_start = start
    
    # Set up deque and dict
    to_explore = deque()
    possible = {} # k = a given possible cell, v= steps from start to that cell
    
    # Add start to both deque and dict
    to_explore.append((y_start, x_start))
    possible[(y_start, x_start)] = 0
    
    # Start BFS loop
    while len(to_explore) > 0:
        # Pop the current cell from to_expore and get the y, x coordinates
        y_current, x_current = to_explore.popleft()
        # Use a loop to explore the cells surrounding the current cell
        for dy, dx in [(-1,0), (1,0), (0,-1), (0,1)]:
            y_next = y_current + dy
            x_next = x_current + dx
            # First, check that the next cell is in bounds. If not, skip to the next loop via continiue
            if not in_bounds(y_next, x_next):
                continue
            # If the next cell is the exit, return the number of moves (current cell's moves + 1)
            if is_escape(y_next, x_next):
                return possible[(y_current, x_current)] + 1
            # If the next cell isn't the exit, test if it's legit and if so, add to to_expore
            if (y_next, x_next) not in possible and not_wall(y_next, x_next):
                to_explore.append((y_next, x_next))
                possible[(y_next, x_next)] = possible[(y_current, x_current)] + 1
    # Return None if cannot reach exit
    return None

# Complexity: O(height x width) + O(r) w/ r = reachable cells --> since r <= height x width --> O(height x width)
# Worst case complexity: O(height x width)
# Memory: O(height x width)


# Example tests:

grid = [
    ["S", ".", "#"],
    [".", "#", "E"],
    [".", ".", "."],
]
assert escape_steps(grid) == 5

grid = [
    ["S", "#", "E"],
]
assert escape_steps(grid) is None
