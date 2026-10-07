'''
Session 2, Problem 18: Job title history (progressive). Level 1

Time limit: 25 minutes, including writing your own tests. Aim for working code by about minute 20. Hard stop at 37 minutes. Before coding: write __init__ with an example comment, and run one example call through it.

Write a class that records each employee's job title over time, keeping every change.

Class name: TitleHistory

Creating a TitleHistory() takes no arguments, and a new history starts empty.

For any one employee, the timestamps in successive set_title calls always strictly increase.

Methods:

set_title(employee, title, timestamp): employee and title are strings, timestamp is a non-negative int. Records that the employee's title became title at time timestamp, keeping all earlier titles. Returns nothing.
title_at(employee, timestamp): employee is a string, timestamp is a non-negative int. Returns the employee's title at that time: the title recorded at the largest timestamp less than or equal to timestamp. Returns None if the employee doesn't exist or has no title recorded at or before timestamp.
title_count(employee): employee is a string. Returns the number of title changes recorded for the employee, as an int, or 0 if the employee doesn't exist.
---------------------------------------------------------------------------------
Session 2, Problem 18: Job title history. Level 2

Time limit: 25 minutes, including writing your own tests. Aim for working code by about minute 20. Hard stop at 37 minutes. Start with your one-line variable list and one example call through your structure.

Add two methods to your TitleHistory class. Everything from Level 1 must keep working.

New methods:

changes_between(employee, start, end): employee is a string; start and end are non-negative ints with start ≤ end. Returns a list of the titles recorded for the employee at timestamps from start to end, inclusive, in time order (earliest first). Returns an empty list if the employee doesn't exist or has no changes in that range.
employees_with_title(title, timestamp): title is a string, timestamp is a non-negative int. Returns a list of all employees whose title at time timestamp is title, sorted alphabetically. Returns an empty list if there are none.


'''

class TitleHistory:
    
    def __init__(self):
        self.records: dict[str, dict] = {} # k=employee (str), dict w/ inner k=timestamp (int), v=title (str)

    '''1. set_title(employee, title, timestamp): employee and title are strings, timestamp is a non-negative int. 
    Records that the employee's title became title at time timestamp, keeping all earlier titles. 
    Returns nothing.'''
    def set_title(self, employee: str, title: str, timestamp: int):
        employee_data = self.records.get(employee, None)
        # If employee isn't in records, add him
        if employee_data is None:
            self.records[employee] = {timestamp:title}
        # If employee is in records, add timestamp:title to inner dict
        else:
            employee_data[timestamp] = title
            self.records[employee] = employee_data


    '''2. title_at(employee, timestamp): employee is a string, timestamp is a non-negative int. 
    Returns the employee's title at that time: the title recorded at the largest timestamp less than or equal to timestamp. 
    Returns None if the employee doesn't exist or has no title recorded at or before timestamp.'''
    def title_at(self, employee: str, timestamp: int):
        employee_data = self.records.get(employee, None)
        # If employee is in records, check timestamps+titles
        if employee_data is not None:
            result = None
            # Loop across the employee's ts+titles
            for employee_timestamp, employee_title in employee_data.items():
                # If we've passed the timestamp, we've gone too far
                if employee_timestamp > timestamp:
                    break
                # Update result with the last title before we hit the threshold 
                result = employee_title
                print(f'result: {result}')
            # Return that title (None if no titles earlier than threshold)
            return result
        # None if employee doesn't exist
        return None
    
    '''3. title_count(employee): employee is a string. 
    Returns the number of title changes recorded for the employee, as an int, or 0 if the employee doesn't exist.'''
    def title_count(self, employee: str):
        # Each record in the inner dict = a change, so just return len of dict
        return len(self.records.get(employee, []))
    
    '''4. changes_between(employee, start, end): employee is a string; start and end are non-negative ints with start ≤ end. 
    Returns a list of the titles recorded for the employee at timestamps from start to end, inclusive, in time order (earliest first). 
    Returns an empty list if the employee doesn't exist or has no changes in that range.'''
    def changes_between(self, employee: str, start: int, end: int):
        employee_data = self.records.get(employee, None)
        print(f'employee_data: {employee_data}, start: {start}, end:{end}')
        # We return an empty list if nth qualifies
        positions = []
        # If employee is in records, check timestamps+titles
        if employee_data is not None:
            # List comp, filtering for timestamps
            positions = [position for timestamp, position in employee_data.items() if (timestamp >= start and timestamp <= end)]
        print(f'positions: {positions}')
        # Return populated or empty list
        return positions
    
    '''5. employees_with_title(title, timestamp): title is a string, timestamp is a non-negative int. 
    Returns a list of all employees whose title at time timestamp is title, sorted alphabetically. 
    Returns an empty list if there are none.'''
    def employees_with_title(self, title: str, timestamp: int):
        employees = []
        if len(self.records.items()) > 0:
            for employee, employee_data in self.records.items():
                if self.title_at(employee=employee, timestamp=timestamp) == title:
                    employees.append(employee)
        return sorted(employees)
                
# Complexity:
# j = jobs for 1 employee
# e = # of employees total
# h = # of titles held, total, across all employees
# l = # employees with a specified title, at a specified time
# 1. set_title --> O(1)
# 2. title_at --> loops over jobs for given employee --> O(j)
# 3. title_count --> O(1)
# 4. changes_between --> loops over jobs for a given employee O(j) 
# 5. employees_with_title --> loops over each employee O(e) and inside, loops over each employee's jobs, which in total is h, so O(h) + sorts O(l log l) --> O(e + h + l log l)

# Worst case: employees_with_title, O(h + l log l)
# Memory: O(j) since j < e
    
# Example tests:

history = TitleHistory()
history.set_title("ann", "engineer", 10)
history.set_title("ann", "manager", 20)
assert history.title_at("ann", 15) == "engineer"
assert history.title_at("ann", 25) == "manager"
assert history.title_at("bob", 15) is None # No such employee
assert history.title_at("ann", 1) is None # Employee exists but no title at or before date
assert history.title_at("bob", 1) is None # No position at this date


history = TitleHistory()
assert history.title_count("ann") == 0
history.set_title("ann", "engineer", 10)
history.set_title("ann", "manager", 20)
assert history.title_count("ann") == 2 # Increments title count
assert history.title_count("bob") == 0 # No such employee

history = TitleHistory()
history.set_title("ann", "engineer", 10)
history.set_title("ann", "lead", 20)
history.set_title("ann", "manager", 30)

assert history.changes_between("ann", 15, 30) == ["lead", "manager"]
assert history.changes_between("ann", 10, 10) == ["engineer"] # One specific date
assert history.changes_between("ann", 1, 2) == [] # No changes in date range (too low)
assert history.changes_between("ann", 100, 200) == [] # No changes in date range (too high)
assert history.changes_between("bob", 15, 30) == [] # No such employee


history = TitleHistory()
assert history.employees_with_title("engineer", 15) == [] # No employees
history.set_title("bob", "engineer", 5)
history.set_title("ann", "engineer", 10)
history.set_title("ann", "manager", 20)
assert history.employees_with_title("engineer", 15) == ["ann", "bob"]
assert history.employees_with_title("banker", 15) == [] # No employees w/ this title
assert history.employees_with_title("engineer", 1) == [] # No employees w/ this title at specified time


print(f'all tests pass')