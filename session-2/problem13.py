'''
Session 2, Problem 13: Lending library (progressive). Level 1

This problem has 3 levels. Each adds to the same class, and earlier levels must keep working.

Time limit: 25 minutes, including writing your own tests. Aim for working code by about minute 20. Hard stop at 37 minutes. Start with the design block: variable list, data structures, one line per method.

Write a class that tracks books and which members have borrowed them.

Class name: LendingLibrary

Creating a LendingLibrary() takes no arguments, and a new library starts with no books.

Methods:

add_copies(book_id, copies): book_id is a string, copies is a positive int. Adds copies copies of the book to the library; the book may or may not already be in the library. Returns the total number of copies of that book the library now owns, as an int. Copies currently borrowed still count as owned.
borrow(member, book_id): member and book_id are strings. The member borrows one copy of the book. Returns True if the loan was made. Returns False, with nothing changed, if the book isn't in the library, if every copy is already borrowed, or if the member already has a copy of that book.
return_book(member, book_id): member and book_id are strings. The member returns their copy of the book. Returns True if the member had borrowed that book and has now returned it, or False otherwise.
------------------------------------------------------------------------------------
Session 2, Problem 13: Lending library. Level 2

Time limit: 25 minutes, including writing your own tests. Aim for working code by about minute 20. Hard stop at 37 minutes. Start by running one example call through your structures.

Add two methods to your LendingLibrary class. Everything from Level 1 must keep working. 

New methods:

books_on_loan(member): member is a string. Returns a list of the ids of all books the member currently has on loan, sorted alphabetically. Returns an empty list if the member has no books on loan or has never borrowed.
available_titles(): no arguments. Returns a list of all books that have at least one copy not currently borrowed, each as a string in the format "book_id(available)", where available is the number of copies not currently borrowed. The list is sorted by available, largest first; books with equal available are sorted alphabetically by id. Returns an empty list if no copies are available.

------------------------------------------------------------------------------------

'''


class LendingLibrary:
    
    def __init__(self):
        self.records_owned: dict[str, int] = {} # k=book_id (str), v=copies (int), memory = t (titles)
        self.records_borrower: dict[str, set] = {} # k= member(str), v=set of book_id (str) user[copies lent out] --> u + L
        self.records_total_borrowed: dict[str, int] = {} # k= book_id (str) v= copies borrowed (int) t (titles) 

    '''1. add_copies(book_id, copies): book_id is a string, copies is a positive int. 
    Adds copies copies of the book to the library; the book may or may not already be in the library. 
    Returns the total number of copies of that book the library now owns, as an int. 
    Copies currently borrowed still count as owned.'''
    def add_copies(self, book_id: str, copies: int):
        # Get the # of books the library owns
        books_owned = self.records_owned.get(book_id, None)
        # If the library doesn't already own the book, total stock = copies
        if books_owned is None:
            books_owned = copies
            self.records_owned[book_id] = copies
            self.records_total_borrowed[book_id] = 0
        # If the library already owns the book, increment the stock
        else:
            books_owned += copies
            self.records_owned[book_id] = books_owned
        # return the updated stock
        return books_owned
    
    '''2. borrow(member, book_id): member and book_id are strings. 
    The member borrows one copy of the book. Returns True if the loan was made. 
    Returns False, with nothing changed, if the book isn't in the library, if every copy is already borrowed, or if the member already has a copy of that book.'''
    def borrow(self, member: str, book_id: str):
        books_owned = self.records_owned.get(book_id, None)
        books_total_borrowed = self.records_total_borrowed.get(book_id, None)
        books_borrowed_member = self.records_borrower.get(member, None)
        
        # Return false if the book isn't in the library, if every copy is already borrowed, or if the member already has a copy of that book
        if books_owned is None or books_total_borrowed is None or (books_owned-books_total_borrowed) < 1 or (books_borrowed_member is not None and book_id in books_borrowed_member):
            return False
        # Increment the total borrowings for this book and add it to this member's set of borrowed books
        self.records_total_borrowed[book_id] += 1
        if books_borrowed_member is None:
            self.records_borrower[member] = {book_id}
        else:
            self.records_borrower[member].add(book_id)
        return True

    '''3. return_book(member, book_id): member and book_id are strings. 
    The member returns their copy of the book. 
    Returns True if the member had borrowed that book and has now returned it, or False otherwise.'''
    def return_book(self, member: str, book_id: str):
        books_owned = self.records_owned.get(book_id, None)
        books_total_borrowed = self.records_total_borrowed.get(book_id, None)
        books_borrowed_member = self.records_borrower.get(member, None)
        print(f'books_owned: {books_owned}, books_total_borrowed: {books_total_borrowed}, books_borrowed_member: {books_borrowed_member}')
        
        # Return false if the book isn't in the library, if every copy is already borrowed, or if the member already has a copy of that book
        if books_owned is not None and books_borrowed_member is not None and book_id in books_borrowed_member:
            self.records_total_borrowed[book_id] -= 1
            self.records_borrower[member].remove(book_id)
            print(f'self.records_total_borrowed[book_id]: {self.records_total_borrowed[book_id]},  self.records_borrower[member]: { self.records_borrower[member]}')
            return True
        return False
    
    '''4. books_on_loan(member): member is a string. 
    Returns a list of the ids of all books the member currently has on loan, sorted alphabetically. 
    Returns an empty list if the member has no books on loan or has never borrowed.'''
    def books_on_loan(self, member: str):
        solution = sorted(self.records_borrower.get(member, [])) 
        return solution
    
    '''5. available_titles(): no arguments. 
    Returns a list of all books that have at least one copy not currently borrowed, 
    each as a string in the format "book_id(available)", where available is the number of copies not currently borrowed. 
    The list is sorted by available, largest first; books with equal available are sorted alphabetically by id. 
    Returns an empty list if no copies are available.'''
    def available_titles(self):
        pairs = {}
        # Loop over copies owned and subtract total checked out
        for book_id, copies in self.records_owned.items():
            checked_out = self.records_total_borrowed.get(book_id, 0)
            pairs[book_id] = copies-checked_out
        print(f'pairs: {pairs}')
        # Sort and format
        solution_formatted = [f'{book_id}({copies})' for book_id, copies in sorted(pairs.items(), key=lambda kv: (-kv[1], kv[0])) if copies > 0]
        print(f'solution_formatted: {solution_formatted}') 
        return solution_formatted
            
        

    
# Complexity:
# 1. add_copies: O(1)
# 2. borrow: all lookups are dicts or sets O(1) --> O(1)
# 3. return_book: ditto above --> O(1)
# 4. books_on_loan: sort the books borrowed by a given user O(b log b), worst case since b<=t, O(t log t)
# 5. available_titles: loop over records owned O(t) + sort pairs with 1 pair per title O(t log t) + loop over those sorted pairs O(t) --> O(t + t + t log t) --> O(t log t)
    
# Worst case complexity: O(b log b + t log t) --> since b <= t --> O(t log t)
# Memory: O(t + u + L) w/ t=titles, u=users, L=books loaned out, a = available books, b= the books borrowed by a given user

#Example tests:


library = LendingLibrary()
assert library.add_copies("dune", 1) == 1
assert library.borrow("ann", "dune") is True
assert library.borrow("bob", "dune") is False
assert library.borrow("ann", "no title") is False # book not in library
assert library.borrow("ann", "dune") is False # user already rented book
assert library.add_copies("dune", 1) == 2


library = LendingLibrary()
assert library.return_book("ann", "dune") is False
assert library.add_copies("dune", 1) == 1
assert library.borrow("ann", "dune") is True
assert library.return_book("ann", "dune") is True



library = LendingLibrary()
library.add_copies("dune", 2)
library.add_copies("emma", 1)

library.borrow("ann", "emma")
library.borrow("ann", "dune")
assert library.books_on_loan("ann") == ["dune", "emma"]
assert library.books_on_loan("bill") == [] # Empty list if user not registered
library.add_copies("emma", 1)
library.add_copies("all", 2)
library.borrow("ann", "all")
assert library.books_on_loan("ann") == ["all", "dune", "emma"] # alph sorting if avail is equal

assert library.return_book("ann", "dune") is True
assert library.return_book("ann", "emma") is True
assert library.return_book("ann", "all") is True
assert library.books_on_loan("ann") == [] # Empty list if nothing borrowed



library = LendingLibrary()
library.add_copies("dune", 3)
library.add_copies("emma", 1)
library.borrow("ann", "dune")
library.borrow("bob", "emma")
assert library.available_titles() == ["dune(2)"]

library = LendingLibrary()
library.add_copies("dune", 3)
library.add_copies("emma", 1)
library.add_copies("all", 3)
library.add_copies("zebra", 3)
library.borrow("ann", "emma")
library.borrow("ann", "all")
library.borrow("ann", "dune")
assert library.available_titles() == ["zebra(3)", "all(2)", "dune(2)"] # qty, then alph sorting


print(f'tests pass')