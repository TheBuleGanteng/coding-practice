'''
Session 2, Problem 26: Restaurant waitlist (progressive). Level 1

Time limit: 25 minutes, including writing your own tests. Aim for working code by about minute 20. Hard stop at 37 minutes. Before coding: write __init__ with an example comment, run one example call through it, and check that your dict keys are unique and are what the spec looks things up by.

Write a class that keeps a separate waitlist for each restaurant, in the order parties arrive.

Class name: Waitlist

Creating a Waitlist() takes no arguments, and it starts with no waitlists. Any restaurant name can be used; restaurants don’t need to be created first.

Methods:

join(restaurant, party, size): restaurant and party are strings, size is a positive int. Adds the party, with that many people, to the back of that restaurant’s waitlist. Returns the party’s position in the line, as an int (1 for the front). Returns None, with nothing changed, if that party is already waiting at that restaurant.
seat_next(restaurant): restaurant is a string. Removes the party that has been waiting longest at that restaurant and returns its name. Returns None if that restaurant’s waitlist is empty or doesn’t exist.
leave(restaurant, party): restaurant and party are strings. Removes that party from that restaurant’s waitlist, wherever it is, and returns its size. Returns None if the party isn’t waiting there.

Time limit: 25 minutes, including writing your own tests. Aim for working code by about minute 20. Hard stop at 37 minutes. Start with your one-line variable list and one example call through your structure.

Add two methods to your Waitlist class. Everything from Level 1 must keep working.

New methods:

position(restaurant, party): restaurant and party are strings. Returns the party’s current position in that restaurant’s line, as an int (1 for the front). Returns None if the party isn’t waiting there.
busiest(n): n is a non-negative int. Returns a list of the n restaurants with the most people currently waiting (the total of all waiting parties’ sizes), each as a string in the format "restaurant(people)". The list is sorted by people, largest first; restaurants with equal totals are sorted alphabetically. Only restaurants with at least one party waiting are included. If fewer than n qualify, returns all of them.

'''

import re


class Waitlist():
    def __init__(self):
        self.records: dict[str, dict[str, int]] = {} # k=rest(str), k=party(str), v=size(int)
        
        
    '''1. join(restaurant, party, size): restaurant and party are strings, size is a positive int. 
    Adds the party, with that many people, to the back of that restaurant’s waitlist. 
    Returns the party’s position in the line, as an int (1 for the front). 
    Returns None, with nothing changed, if that party is already waiting at that restaurant.'''
    def join(self, restaurant: str, party: str, size:int):
        data = self.records.get(restaurant, None)
        if data is None:
            self.records[restaurant] = {party:size}
            return 1
        if party in data:
            return None
        self.records[restaurant][party] = size
        return len(self.records[restaurant])
        
    
    
    '''2. seat_next(restaurant): restaurant is a string. 
    Removes the party that has been waiting longest at that restaurant and returns its name. 
    Returns None if that restaurant’s waitlist is empty or doesn’t exist.'''
    def seat_next(self, restaurant: str):
        data = self.records.get(restaurant, None)
        if data is not None and len(data) > 0:
            solution = next(iter(data))
            self.records[restaurant].pop(solution)
            return solution
        return None
    
    '''3. leave(restaurant, party): restaurant and party are strings. 
    Removes that party from that restaurant’s waitlist, wherever it is, and returns its size. 
    Returns None if the party isn’t waiting there.'''
    def leave(self, restaurant: str, party: str):
        data = self.records.get(restaurant, None)
        if data is not None and len(data) > 0:
            return data.pop(party, None)
        return None
    
    
    '''4. position(restaurant, party): restaurant and party are strings. 
    Returns the party’s current position in that restaurant’s line, as an int (1 for the front). 
    Returns None if the party isn’t waiting there.'''
    def position(self, restaurant: str, party: str):
        data = self.records.get(restaurant, None)
        if data is not None and party in data:
            n = 1
            for rest_party, rest_size in data.items():
                if rest_party == party:
                    return n
                else:
                    n += 1
        return None
    
    
    '''5. busiest(n): n is a non-negative int. 
    Returns a list of the n restaurants with the most people currently waiting (the total of all waiting parties’ sizes), 
    each as a string in the format "restaurant(people)". 
    The list is sorted by people, largest first; restaurants with equal totals are sorted alphabetically. 
    Only restaurants with at least one party waiting are included. 
    If fewer than n qualify, returns all of them.'''
    def busiest(self, n: int):
        restos = {}
        for restaurant, data in self.records.items():
            if len(data) > 0:
                restos[restaurant] = sum(data.values())
        solution = [f'{restaurant}({bookings})' for restaurant, bookings in sorted(restos.items(), key=lambda kv:(-kv[1], kv[0]))][:n]
        print(f'solution: {solution}')
        return solution
    
    
    
        
# Complexity:
# r = total restaurants
# b = total bookings
# p = bookings for a given resto
# 1. join --> O(1)
# 2. seat_next --> O(1)
# 3. leave --> O(1)
# 4. position --> loops over bookings for a given resto --> O(p)
# 5. busiest --> Loops over all restos O(r) and loops across the bookings in each resto, so O(b) in total and sorts the results O(r log r)--> O(r + b + r log r)

# Worst case complexity: O(r + b + r log r) --> O(b + r log r)
# Memory: O(r + b)

# Example tests:



waitlist = Waitlist()
assert waitlist.join("noma", "ann", 2) == 1
assert waitlist.join("noma", "bob", 4) == 2
assert waitlist.seat_next("noma") == "ann"
assert waitlist.join("noma", "ann", 2) == 2 # Party rejoins line after being seated
assert waitlist.join("noma", "bob", 4) is None # Duplicate reservation

waitlist = Waitlist()
assert waitlist.seat_next("noma") is None # Waitlist is empty

waitlist = Waitlist()
waitlist.join("noma", "ann", 2)
assert waitlist.leave("noma", "ann") == 2
assert waitlist.seat_next("noma") is None # Waitlist is empty
assert waitlist.leave("bob", "ann") is None # Party isn't waiting there

waitlist = Waitlist()
waitlist.join("noma", "ann", 2)
waitlist.join("noma", "bob", 4)
waitlist.join("noma", "cat", 3)
waitlist.seat_next("noma")
assert waitlist.position("noma", "cat") == 2
assert waitlist.position("noma", "dog") is None # Party isn't waiting there


waitlist = Waitlist()
waitlist.join("noma", "ann", 2)
waitlist.join("noma", "bob", 4)
waitlist.join("geranium", "cat", 8)
assert waitlist.busiest(2) == ["geranium(8)", "noma(6)"]
assert waitlist.busiest(10) == ["geranium(8)", "noma(6)"] # returns all restults
waitlist.join("alpha", "dog", 8) 
assert waitlist.busiest(10) == ["alpha(8)", "geranium(8)", "noma(6)"] # alpha sort

waitlist = Waitlist()
assert waitlist.busiest(10) == [] # No resos

print('all tests pass')