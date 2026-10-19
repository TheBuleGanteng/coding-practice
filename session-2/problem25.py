'''
Session 2, Problem 25: Support ticket queue (progressive). Level 1

Time limit: 25 minutes, including writing your own tests. Aim for working code by about minute 20. Hard stop at 37 minutes. Before coding: write __init__ with an example comment, run one example call through it, and check that your dict keys are unique and are what the spec looks things up by.

Write a class that keeps support tickets in the order they arrive.

Class name: TicketQueue

Creating a TicketQueue() takes no arguments, and a new queue starts empty.

Methods:

add(ticket, description): ticket and description are strings. Adds the ticket to the back of the queue. Returns True if it was added, or False, with nothing changed, if a ticket with that id is already in the queue.
serve(): no arguments. Removes the ticket that has been in the queue the longest and returns its id. Returns None if the queue is empty.
close(ticket): ticket is a string. Removes that ticket from the queue, wherever it is, and returns its description. Returns None if it isn’t in the queue.
'''

class TicketQueue:
    def __init__(self):
       self.records: dict[str, str] = {}   # ticket -> description, e.g. {"t1": "login broken"}
        
    '''1. add(ticket, description): ticket and description are strings. 
    Adds the ticket to the back of the queue. 
    Returns True if it was added, or False, with nothing changed, if a ticket with that id is already in the queue.'''
    def add(self, ticket: str, description: str):
        ticket_data = self.records.get(ticket, None)
        if ticket_data is None:
            self.records[ticket] = description
            return True
        return False
    
    '''2. serve(): no arguments. 
    Removes the ticket that has been in the queue the longest and returns its id. 
    Returns None if the queue is empty.'''
    def serve(self):
        # Return none if no records:
        if len(self.records) == 0:
            return None
        # Retrieve the first key (the timestamp, "ticket")
        first_item = next(iter(self.records))
        # Pop the record with that first key
        solution = self.records.pop(first_item, None)
        print(f'solution: {solution}')
        # Return that first key
        return first_item
    
    '''3. close(ticket): ticket is a string. 
    Removes that ticket from the queue, wherever it is, and returns its description. 
    Returns None if it isn’t in the queue.'''
    def close(self, ticket):
        # Inner parens= get first key --> Outer parens= Pop based on that key, falling back to None
        return self.records.pop(ticket, None)
    
# Complexity: 
# t = total number of tickets
# 1. add --> O(1)
# 2. serve --> O(1)
# 3. close --> O(1)


# Worst-case complexity: O(1)
# Memory: O(t)


# Example tests:


queue = TicketQueue()
queue.add("t1", "login broken")
queue.add("t2", "billing question")
assert queue.serve() == "t1"
assert queue.serve() == "t2"

queue = TicketQueue()
queue.add("t1", "login broken")
assert queue.close("t1") == "login broken"
