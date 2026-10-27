'''
Session 3, Problem 5: Recent orders (progressive). Level 1

Time limit: 25 minutes, including writing your own tests. Before coding, read all three methods, note what data each needs, then write __init__ with an example comment and run one example call through it. Aim for working code by about minute 20. Hard stop at 37 minutes. Before running your tests, point at the line that handles each “Returns…” sentence.

Write a class that keeps, for each customer, a limited list of the drinks they ordered most recently.

Class name: OrderHistory

Creating an OrderHistory(limit) takes one argument: limit, a positive int, the most drinks kept for any one customer. It starts with no customers.

Methods:

order(customer, drink): customer and drink are strings. Records that the customer ordered the drink, making it their most recent order. If this makes the customer’s list hold more than limit drinks, removes the one they ordered least recently. Returns the removed drink, or None if nothing was removed.
times_ordered(customer, drink): customer and drink are strings. Returns how many times the customer has ordered the drink while it has been in their list, as an int. If a drink is removed and later ordered again, its count starts over from 1. Returns 0 if the drink isn’t in the customer’s list.
last_order(customer): customer is a string. Returns the drink the customer ordered most recently, or None if their list is empty.
'''

class OrderHistory:
    
    def __init__(self, limit):
        self.limit = limit
        self.records: dict[str, dict[str, int]] = {} # k customer, k=drink, v=times ordered
    
    '''order(customer, drink): customer and drink are strings. Records that the customer ordered the drink, making it their most recent order. 
    If this makes the customer’s list hold more than limit drinks, removes the one they ordered least recently. 
    Returns the removed drink, or None if nothing was removed.'''
    def order(self, customer: str, drink:str):
        # Pull customer data
        customer_data = self.records.get(customer, None)
        # If no customer data, set up dict
        if customer_data is None:
            self.records[customer] = {drink:1}
        # If customer data, save drink record, if any
        else:
            order_data = self.records[customer].pop(drink, 0)
            self.records[customer][drink] = order_data + 1
        # Check for overrun
        if len(self.records[customer]) > self.limit:
            # Store drink to return it
            removed = next(iter(self.records[customer]))
            # Remove drink
            self.records[customer].pop(removed)
            return removed
        return None

    '''2. times_ordered(customer, drink): customer and drink are strings. 
    Returns how many times the customer has ordered the drink while it has been in their list, as an int. 
    If a drink is removed and later ordered again, its count starts over from 1. 
    Returns 0 if the drink isn’t in the customer’s list.'''
    def times_ordered(self, customer:str, drink: str):
        return self.records.get(customer, {}).get(drink, 0)
   

    '''3. last_order(customer): customer is a string. 
    Returns the drink the customer ordered most recently, or None if their list is empty.'''
    def last_order(self, customer: str):
        customer_data = self.records.get(customer, None)
        if customer_data is not None:
            return next(reversed(customer_data), None)
            print(f'solution: {solution}')
        return None    


# Complexity:
# c = total customers
# d = total drinks, across all customers
# 1. order --> O(1)
# 2. times_ordered --> O(1)
# 3. last_order --> O(1)


# Worst-case complexity: O(1)
# Memory: O(c + d)


# Example tests:

history = OrderHistory(2)
history.order("ann", "latte")
history.order("ann", "mocha")
history.order("ann", "latte")
assert history.last_order("ann") == "latte"
assert history.times_ordered("ann", "latte") == 2
assert history.times_ordered("bob", "latte") == 0 # Customer doesn't exist
assert history.times_ordered("bob", "milk") == 0 # Drink not in customer's order history



history = OrderHistory(2)
history.order("ann", "latte")
history.order("ann", "mocha")
assert history.order("ann", "tea") == "latte"


history = OrderHistory(2)
assert history.last_order("ann") is None # Empty list
