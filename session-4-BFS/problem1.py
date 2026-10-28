'''
Session 3, Problem 7: Reachable cells (untimed walkthrough)

This time it’s a function, not a class.

Function name: count_reachable

Arguments:

grid: a list of lists of strings, where each string is "." (open) or "#" (wall). Every row has the same length, and there’s at least one row.
start: a tuple of two ints, (row, col), the starting cell.

Returns the number of open cells reachable from start by moving up, down, left, or right through open cells, as an int, counting start itself. Returns 0 if start is a wall.
'''
from collections import deque

def count_reachable(grid: list, start: tuple):
    height = len(grid) # Number of rows
    width = len(grid[0]) # Number of cols
    
    # Helper for telling a wall
    def is_wall(y, x):
        if grid[y][x] == "#":
            return True
        return False
    
    # Helper for telling if a cell is on the grid
    def off_grid(y, x):
        if y > height - 1 or y < 0 or x > width - 1 or x < 0:
            return True
        return False
    
    # Set up deque to store valid, but not-yet-visited cells
    to_visit = deque() 
    # Set up set to store the running total of cells known to be reachable
    possible = set()
    
    # First, check if start is a wall and if so, return 0, per spec
    start_y, start_x = start
    if is_wall(start_y, start_x) is True:
        return 0
    
    # The start gets appended to both visited and to possible (the latter so the while loop works)
    to_visit.append((start_y, start_x))
    possible.add((start_y, start_x))
    while len(to_visit) > 0:
        # Fist, remove the current cell (the oldest one) from to_visit
        current_y, current_x = to_visit.popleft()
        # Next, explore y+1, y-1, x+1, x-1
        for dy, dx in [(1,0), (-1,0), (0, 1), (0, -1)]:
            next_y = current_y + dy
            next_x = current_x + dx
            # Here, we check if that cell is truly new (e.g. not already in the possible set) and that it's not off-grid or is a wall
            if (next_y, next_x) not in possible and not off_grid(next_y, next_x) and not is_wall(next_y, next_x):
                # If this truly is a new option, add it to the deque and the set
                to_visit.append((next_y, next_x))
                possible.add((next_y, next_x))
    # Return the number of cells that are reachable, per the spec
    return len(possible)


# Complexity: Loop runs for len(possible), which in the worst case, is all cells, so O(height x width)
# Memory: O(height x width)

# Example tests:

grid = [
    [".", ".", "#"],
    [".", "#", "."],
    [".", ".", "."],
]
assert count_reachable(grid, (0, 0)) == 6

grid = [["#"]]
assert count_reachable(grid, (0, 0)) == 0