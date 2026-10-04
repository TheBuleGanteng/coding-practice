'''
Session 2, Problem 5: Library

Time limit: 25 minutes, including writing your own tests. Aim for working code by about minute 20. Hard stop at 37 minutes.

Write a class that tracks how many copies of each book a library has on the shelf.

Class name: Library

Creating a Library() takes no arguments, and a new library starts with no books.

Methods:

1. add_copies(title, copies): title is a string, copies is a positive int. 
Adds copies copies of that title to the shelf; the title may or may not already be in the library. 
Returns the number of copies of that title now on the shelf, as an int.
2. checkout(title): title is a string. 
If at least one copy of that title is on the shelf, removes one copy and returns True. 
Otherwise returns False, including when the title isn't in the library.
3. remove_title(title): title is a string. 
Removes the title from the library entirely and returns the number of copies it had on the shelf, as an int. 
Returns None if the title isn't in the library.
4. titles(): no arguments. 
Returns a list of all titles with at least one copy on the shelf, sorted alphabetically.
'''

class Library:
    
    def __init__(self):
        self.records: dict[str, int] = {}
        
    def add_copies(self, title: str, copies: int):
        copies = self.records.get(title, 0) + copies
        self.records[title] = copies
        return self.records[title]
         
    def checkout(self, title):
        copies = self.records.get(title, 0) - 1
        if copies < 0:
            return False
        self.records[title] -= 1
        return True
    
    def remove_title(self, title):
        copies = self.records.get(title, None)
        print(f'title: {title}, copies: {copies}')
        if copies is None:
            return None
        del(self.records[title])
        return copies
    
    def titles(self):
        print(f'self.records.items(): {self.records.items()}')
        print(f'titles() returning: {sorted(names for names, copies in self.records.items() if copies > 0)}')
        return sorted(names for names, copies in self.records.items() if copies > 0)

# Complexity:
# 1. add_copies: O(1)
# 2. checkout: O(1)
# 3. remove_title: O(1)
# 4. titles: loop O(m) + sort a list O(m log m) where m = titles --> O(m + m log m) --> O(m log m)
# Worst case compleixty: O(m) w/ memory O(m)        


# Example tests:

library = Library()

assert library.add_copies("dune", 2) == 2
assert library.add_copies("dune", 2) == 4
assert library.add_copies("all", 2) == 2

assert library.checkout('dune') is True
assert library.checkout('none') is False
assert library.add_copies("none", 2) == 2
assert library.checkout('none') is True
assert library.checkout('none') is True

assert library.remove_title('dune') == 3
assert library.remove_title('none') == 0
assert library.remove_title('not in') is None

assert library.add_copies("dune", 2) == 2
assert library.add_copies("none", 2) == 2
assert library.titles() == ['all', 'dune', 'none']

library2 = Library()
assert library2.titles() == []

print('all tests pass')