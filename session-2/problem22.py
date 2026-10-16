'''
Session 2, Problem 22: Step tracker (progressive). Level 1

Time limit: 25 minutes, including writing your own tests. Aim for working code by about minute 20. Hard stop at 37 minutes. Before coding: write __init__ with an example comment, run one example call through it, and check which row of your structures table this is.

Write a class that records how many steps users walk each day.

Class name: StepTracker

Creating a StepTracker() takes no arguments, and a new tracker starts empty.

For any one user, the day values in successive log calls always strictly increase.

Methods:

log(user, steps, day): user is a string; steps and day are non-negative ints. Records that the user walked steps steps on that day. Returns the user’s total steps across all logged days, as an int.
steps_on(user, day): user is a string, day is a non-negative int. Returns the number of steps the user logged on exactly that day, as an int. Returns 0 if the user doesn’t exist or logged nothing that day.
best_day(user): user is a string. Returns the day on which the user logged the most steps, as an int. If several days tie for the most, returns the earliest of them. Returns None if the user doesn’t exist.


Session 2, Problem 22: Step tracker. Level 2

Time limit: 25 minutes, including writing your own tests. Aim for working code by about minute 20. Hard stop at 37 minutes. Start with your one-line variable list and one example call through your structure.

Add two methods to your StepTracker class. Everything from Level 1 must keep working.

New methods:

steps_between(user, start, end): user is a string; start and end are non-negative ints with start ≤ end. Returns the total steps the user logged on days from start to end, inclusive, as an int. Returns 0 if the user doesn’t exist or logged nothing in that range.
longest_streak(user, goal): user is a string, goal is a non-negative int. Returns the length of the user’s longest run of consecutive days on which they logged at least goal steps, as an int. Days are consecutive only if their numbers differ by exactly 1; a day with nothing logged breaks a run. Returns 0 if the user doesn’t exist or never met the goal.

'''
class StepTracker:
    
    def __init__(self):
        self.records: dict[str, dict[int, int]] = {} # k = user (str), k=day(int), v=steps(int)
        self.records_steps: dict[str, int] = {} # k = user (str), v=steps (int)

    '''1. log(user, steps, day): user is a string; steps and day are non-negative ints. 
    Records that the user walked steps steps on that day. 
    Returns the user’s total steps across all logged days, as an int.'''
    def log(self, user: str, steps: int, day: int):
        user_data = self.records.get(user, None)
        if user_data is None:
            self.records[user] = {day:steps}
            self.records_steps[user] = steps
        else:
            self.records[user][day] = steps
            self.records_steps[user] += steps
        return self.records_steps[user]
        


    '''2. steps_on(user, day): user is a string, day is a non-negative int. 
    Returns the number of steps the user logged on exactly that day, as an int. 
    Returns 0 if the user doesn’t exist or logged nothing that day.'''
    def steps_on(self, user: str, day: int):
        user_data = self.records.get(user, None)
        if user_data is not None:
            day_steps = user_data.get(day, None)
            if day_steps is not None:
                return day_steps
        return 0



    '''3. best_day(user): user is a string. 
    Returns the day on which the user logged the most steps, as an int. 
    If several days tie for the most, returns the earliest of them. 
    Returns None if the user doesn’t exist.'''
    def best_day(self, user: str):
        user_data = self.records.get(user, None)
        if user_data is None:
            return None
        solution = min(user_data.items(), key=lambda kv:(-kv[1], kv[0]))
        print(f'solution: {solution}')
        return solution[0]
    
    '''4. steps_between(user, start, end): user is a string; start and end are non-negative ints with start ≤ end. 
    Returns the total steps the user logged on days from start to end, inclusive, as an int. 
    Returns 0 if the user doesn’t exist or logged nothing in that range.'''
    def steps_between(self, user: str, start: int, end: int):
        user_data = self.records.get(user, None)
        if user_data is None:
            return 0
        summed = sum(user_steps for user_timestamps, user_steps in user_data.items() if (user_timestamps >= start and user_timestamps <= end) )
        return summed 
    
    '''5. longest_streak(user, goal): user is a string, goal is a non-negative int. 
    Returns the length of the user’s longest run of consecutive days on which they logged at least goal steps, as an int. 
    Days are consecutive only if their numbers differ by exactly 1; a day with nothing logged breaks a run. 
    Returns 0 if the user doesn’t exist or never met the goal.'''
    def longest_streak(self, user: str, goal: int):
        user_data = self.records.get(user, None)
        # Return 0 if no user
        if user_data is None:
            return 0
        # Initialize list to hold the days where goal is at least met
        best = 0
        current = 0
        last_day = None
        # Loop through days and populate list
        for day, steps in user_data.items():
            # Check if we meet the goal on this day
            if steps >= goal:
                # If (a) there is an ongoing streak and (b) today is not the last day in current streak + 1, reset current streak
                if current > 0 and last_day is not None and day != last_day + 1:
                    current = 0
                # Increment the length of the current streak
                current += 1
                # Reset last_day to be used in the next iteation of the loop
                last_day = day
                # Check if the newly-updated current_streak beats the best streak thus far
                best = max(best, current)
            else:
                current = 0
        return best
            

# Complexity:
# u = users
# a = all days
# d = days recorded for a given user
# t = days recorded for a user that is tied for most steps
# 1. log --> O(1)
# 2. steps_on --> O(1)
# 3. best_day --> min in days for a given user O(d)
# 4. steps_between --> sum if O(d)
# 5. longest_streak --> loop through days for a user O(d)

# Worst case complexity: O (d)
# Memory: u + a

# Example tests:

tracker = StepTracker()
assert tracker.log("ann", 5000, 1) == 5000
assert tracker.log("ann", 8000, 2) == 13000
assert tracker.steps_on("ann", 2) == 8000
assert tracker.steps_on("ann", 3) == 0 # Nothing logged that day
assert tracker.steps_on("bob", 2) == 0 # No such user

 

tracker = StepTracker()
tracker.log("ann", 8000, 1)
tracker.log("ann", 8000, 3)
assert tracker.best_day("ann") == 1
assert tracker.best_day("bob") is None # No such user
tracker.log("ann", 10000, 4)
assert tracker.best_day("ann") == 4 # Ranks by highest steps
tracker.log("bob", 0, 1)
tracker.log("bob", 0, 2)
assert tracker.best_day("bob") == 1 # Works with 0 steps logged


tracker = StepTracker()
tracker.log("ann", 5000, 1)
tracker.log("ann", 8000, 2)
tracker.log("ann", 3000, 5)
assert tracker.steps_between("ann", 2, 5) == 11000
assert tracker.steps_between("bob", 2, 5) == 0 # User doesn't exist
assert tracker.steps_between("ann", 1, 1) == 5000 # Only 1 day
assert tracker.steps_between("ann", 3, 4) == 0 # No steps in specified period


tracker = StepTracker()
tracker.log("ann", 9000, 1)
tracker.log("ann", 9000, 2)
tracker.log("ann", 2000, 3)
tracker.log("ann", 9000, 4)
tracker.log("ann", 9000, 6)
assert tracker.longest_streak("ann", 8000) == 2
assert tracker.longest_streak("ann", 10000) == 0 # Never met goal
assert tracker.longest_streak("bob", 10000) == 0 # User doesn't exist


tracker = StepTracker()
tracker.log("ann", 9000, 1)
tracker.log("ann", 9000, 2)
tracker.log("ann", 2000, 3)
tracker.log("ann", 9000, 4)
tracker.log("ann", 9000, 6)
assert tracker.longest_streak("ann", 9000) == 2 # Tie for longest streak


print('all tests pass')
