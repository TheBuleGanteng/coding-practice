'''
Session 3, Problem 8: Shortest path (timed)

Time limit: 30 minutes, including writing your own tests. This is the second BFS problem, so it gets a little extra time. Aim for working code by about minute 24. Hard stop at 45 minutes. Start with the design block: what goes in the queue, what goes in the set, and what else you need to keep track of.

Function name: shortest_steps

Arguments:

grid: a list of lists of strings, where each string is "." (open) or "#" (wall). Every row has the same length, and there’s at least one row.
start: a tuple of two ints, (row, col), the starting cell.
target: a tuple of two ints, (row, col), the cell to reach.

Returns the smallest number of moves needed to get from start to target, moving up, down, left, or right through open cells, as an int. 
Returns 0 if start and target are the same open cell. 
Returns None if target can’t be reached, or if start or target is a wall.
'''

from collections import deque


def shortest_steps(grid: list, start: tuple, target: tuple):
    # Unpack the arguments
    y_start, x_start = start
    height = len(grid)
    width = len(grid[0])
    y_target, x_target = target
    
    def not_wall(y, x):
        if grid[y][x] == "#":
            return False
        return True
    
    def in_bounds(y, x):
        if x < 0 or x > width -1 or y <0 or y > height -1:
            return False
        return True
    def is_target(y, x):
        if y == y_target and x == x_target:
            return True
        return False
    
    # Fist, check if we're starting on a wall or if the target is a wall. If so, return None, per the spec.
    if not not_wall(y=y_start, x=x_start) or not not_wall(y_target, x_target):
        return None
    
    # Check if we're starting on the target. If so, return 0
    if is_target(y=y_start, x=x_start):
        return 0
    
    # Set up deque
    to_explore = deque()
    possible = {} # k = (y, x) v = steps
    
    # Append start point to both lists
    to_explore.append(start)
    possible[(y_start, x_start)] = 0 # Possible is a dict with k=a given possible cell v=the steps from start to that cell
    
    # Set up loop
    while len(to_explore) > 0:
        # Pop the oldest item from to_expore and extract the current position
        y_current, x_current = to_explore.popleft()
        # Loop that explores +/- y and +/- x
        for dy, dx in [(-1,0), (1,0), (0,-1), (0,1)]:
            y_next = y_current + dy
            x_next = x_current + dx
            # If one of the cells thus discovered is the target, return the steps, which is the steps to the current cell plus 1
            if is_target(y_next, x_next):
                return possible[(y_current, x_current)] + 1
            elif (y_next, x_next) not in possible and in_bounds(y_next, x_next) and not_wall(y_next, x_next):
                to_explore.append((y_next, x_next))
                possible[(y_next, x_next)] = possible[(y_current, x_current)] + 1
    # Return None if cannot reach target
    return None


# Complexity: O(r) w/ r = reachable cells, worst case O(height x width)
# Memory: O(height x width)

# Example tests:


grid = [
    [".", ".", "#"],
    [".", "#", "."],
    [".", ".", "."],
]
assert shortest_steps(grid, (0, 0), (1, 2)) == 5

grid = [
    [".", "#", "."],
]
assert shortest_steps(grid, (0, 0), (0, 2)) is None