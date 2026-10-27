Session 3, Problem 6: Recent files (progressive). Level 1

Time limit: 25 minutes, including writing your own tests. Before coding, read all three methods, note what data each needs, then write __init__ with an example comment and run one example call through it. Aim for working code by about minute 20. Hard stop at 37 minutes. Before running your tests, point at the line that handles each “Returns…” sentence.

Write a class that keeps, for each user, a limited list of the files they opened most recently.

Class name: RecentFiles

Creating a RecentFiles(limit) takes one argument: limit, a positive int, the most files kept for any one user. It starts with no users.

Methods:

open_file(user, file): user and file are strings. Records that the user opened the file, making it their most recently opened. If this makes the user’s list hold more than limit files, removes the one they opened least recently. Returns the removed file, or None if nothing was removed.
open_count(user, file): user and file are strings. Returns how many times the user has opened the file while it has been in their list, as an int. If a file is removed and later opened again, its count starts over from 1. Returns 0 if the file isn’t in the user’s list.
oldest(user): user is a string. Returns the file in the user’s list that they opened least recently, or None if their list is empty.

Example tests:

python
files = RecentFiles(2)
files.open_file("ann", "a.py")
files.open_file("ann", "b.py")
files.open_file("ann", "a.py")
assert files.oldest("ann") == "b.py"
assert files.open_count("ann", "a.py") == 2
python
files = RecentFiles(2)
files.open_file("ann", "a.py")
files.open_file("ann", "b.py")
assert files.open_file("ann", "c.py") == "a.py"

Paste your code, your tests, and your time when you’re done.