
'''
Session 3, Problem 6: Recent files (progressive). Level 1

Time limit: 25 minutes, including writing your own tests. Before coding, read all three methods, note what data each needs, then write __init__ with an example comment and run one example call through it. Aim for working code by about minute 20. Hard stop at 37 minutes. Before running your tests, point at the line that handles each “Returns…” sentence.

Write a class that keeps, for each user, a limited list of the files they opened most recently.

Class name: RecentFiles

Creating a RecentFiles(limit) takes one argument: limit, a positive int, the most files kept for any one user. It starts with no users.

Methods:

open_file(user, file): user and file are strings. Records that the user opened the file, making it their most recently opened. If this makes the user’s list hold more than limit files, removes the one they opened least recently. Returns the removed file, or None if nothing was removed.
open_count(user, file): user and file are strings. Returns how many times the user has opened the file while it has been in their list, as an int. If a file is removed and later opened again, its count starts over from 1. Returns 0 if the file isn’t in the user’s list.
oldest(user): user is a string. Returns the file in the user’s list that they opened least recently, or None if their list is empty.
'''
class RecentFiles:
    
    def __init__(self, limit):
        self.limit = limit
        self.records: dict[str, dict[str, int]] = {} # k=user, k=file, v=opens
    
    
    '''1. open_file(user, file): user and file are strings. 
    Records that the user opened the file, making it their most recently opened. 
    If this makes the user’s list hold more than limit files, removes the one they opened least recently. 
    Returns the removed file, or None if nothing was removed.'''
    def open_file(self, user:str, file: str):
        user_data = self.records.get(user, None)
        # If new user, set up dict
        if user_data is None:
            self.records[user] = {file:1}
        # If user exists, pop prior record, if any, and reinput, with total incremented
        else:
            opens = self.records[user].pop(file, 0)
            self.records[user][file] = opens + 1
        # Check for length
        if len(self.records[user]) > self.limit:
            removed = next(iter(self.records[user]))
            self.records[user].pop(removed, None)
            return removed
        # Return None if nth removed
        return None     
        
    '''2. open_count(user, file): user and file are strings. 
    Returns how many times the user has opened the file while it has been in their list, as an int. 
    If a file is removed and later opened again, its count starts over from 1. 
    Returns 0 if the file isn’t in the user’s list.'''
    def open_count(self, user: str, file: str):
        return self.records.get(user, {}).get(file, 0)


    '''3. oldest(user): user is a string. 
    Returns the file in the user’s list that they opened least recently, or None if their list is empty.'''
    def oldest(self, user:str):
        return next(iter(self.records.get(user, {})), None)

# Complexity:
# u = total users
# f = total files across all users
# 1. open_file: O(1)
# 2. open_count --> O(1)
# 3. oldest --> O(1)

# Worst-case complexity: O(1)
# Memory: O(u + f)

# Example tests:


files = RecentFiles(2)
assert files.oldest("ann") is None # List is empty, return None
files.open_file("ann", "a.py")
files.open_file("ann", "b.py")
files.open_file("ann", "a.py")
assert files.oldest("ann") == "b.py"
assert files.open_count("ann", "a.py") == 2
assert files.open_count("ann", "z.py") == 0 # File not in list, returns 0


files = RecentFiles(2)
files.open_file("ann", "a.py")
files.open_file("ann", "b.py")
assert files.open_file("ann", "b.py") is None # At limit, return None
assert files.open_file("ann", "c.py") == "a.py" # Above limit, remove file

files = RecentFiles(2)
files.open_file("ann", "a.py")
assert files.open_file("ann", "c.py") is None # under limit, nth removed


print(f'all tests pass')