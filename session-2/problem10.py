'''
Session 2, Problem 10: Warehouse inventory (progressive). Level 1

This problem has 3 levels. Each adds to the same class, and earlier levels must keep working.

Time limit: 25 minutes, including writing your own tests. Aim for working code by about minute 20. Hard stop at 37 minutes. Start with the design block.

Write a class that tracks how many units of each item a warehouse holds.

Class name: Warehouse

Creating a Warehouse() takes no arguments, and a new warehouse starts with no items.

Methods:

add_stock(item, quantity): item is a string, quantity is a positive int. Adds quantity units of that item; the item may or may not already be in the warehouse. Returns the item's new quantity as an int.
remove_stock(item, quantity): item is a string, quantity is a positive int. Removes quantity units of that item and returns its new quantity as an int. Returns None, with the quantity unchanged, if the item isn't in the warehouse or if it has fewer than quantity units. An item whose quantity reaches 0 stays in the warehouse.
get_quantity(item): item is a string. Returns the item's current quantity as an int, or None if the item isn't in the warehouse.

---------------------------------------------------------------------------------------
Session 2, Problem 10: Warehouse inventory. Level 2

Time limit: 25 minutes, including writing your own tests. Aim for working code by about minute 20. Hard stop at 37 minutes. Start with the design block.

Add two methods to your Warehouse class. Everything from Level 1 must keep working.

New methods:

low_stock(threshold): threshold is a non-negative int. Returns a list of all items whose quantity is less than or equal to threshold, each as a string in the format "item(quantity)". The list is sorted by quantity, smallest first; items with equal quantities are sorted alphabetically by name. Returns an empty list if no items qualify.
restock_plan(threshold, target): threshold is a non-negative int, target is an int greater than threshold. For every item whose quantity is less than or equal to threshold, works out how many units are needed to bring it up to target. Returns a list of strings in the format "item(units_needed)", sorted by units needed, largest first; items with equal units needed are sorted alphabetically by name. This method doesn't change any quantities.
---------------------------------------------------------------------------------------
Session 2, Problem 10: Warehouse inventory. Level 3

Time limit: 35 minutes, including writing your own tests. Aim for working code by about minute 28. Hard stop at 52 minutes. Start with the design block, including: which existing methods will the new ones call, and what do those methods change?

Add reservations: units of an item can be held for a period of time. Everything from Levels 1 and 2 must keep working, and the old methods ignore reservations.

Every new method takes a timestamp, a non-negative int. Timestamps in successive calls never decrease.

New methods:

reserve(item, quantity, timestamp, duration): item is a string; quantity and duration are positive ints. Reserves quantity units of the item from timestamp up to, but not including, timestamp + duration. An item has at most one reservation; a new reservation replaces any existing one. Returns True if the item is in the warehouse and its current quantity is at least quantity. Otherwise returns False, and nothing changes.
available_at(item, timestamp): item is a string. Returns the item's quantity minus the units under a reservation that's active at timestamp, as an int, but never less than 0. Returns None if the item isn't in the warehouse.
remove_stock_at(item, quantity, timestamp): same as remove_stock, at time timestamp, except it returns None, with the quantity unchanged, if the item's available units at timestamp are fewer than quantity.


'''


class Warehouse:
    
    def __init__(self):
        self.records: dict[str, int] = {}
        self.reservation_expiry: dict[str, int] = {}
        self.reservation_qty: dict[str, int] = {}
                
    '''1. add_stock(item, quantity): item is a string, quantity is a positive int. 
    Adds quantity units of that item; the item may or may not already be in the warehouse. 
    Returns the item's new quantity as an int.'''
    def add_stock(self, item: str, quantity: int):
        # Check current stock
        stock_data = self.records.get(item, None)
        # If item isn't in WH, put it there with total = quantity 
        if stock_data is None:
            self.records[item] = quantity
            # Added per stage 3
            self.reservation_expiry[item] = 0
            self.reservation_qty[item] = 0
        # If item is in WH, increment by quantity
        else:
            self.records[item] += quantity
        # Return updated balance
        return self.records[item]
    
    '''2. remove_stock(item, quantity): item is a string, quantity is a positive int. 
    Removes quantity units of that item and returns its new quantity as an int. 
    Returns None, with the quantity unchanged, if the item isn't in the warehouse or if it has fewer than quantity units. 
    An item whose quantity reaches 0 stays in the warehouse.'''
    def remove_stock(self, item: str, quantity: int):
        # Pull the stock for item
        stock_data = self.records.get(item, None)
        # If item isn't avail or current stock is < quantity, return None
        if stock_data is None or stock_data < quantity:
            return None
        # Deduct quantity from stock
        self.records[item] -= quantity
        # Return updated quanity
        return self.records[item]
        

    '''3.get_quantity(item): item is a string. 
    Returns the item's current quantity as an int, or None if the item isn't in the warehouse.'''
    def get_quantity(self, item: str):
        # Pull the stock for item
        stock_data = self.records.get(item, None)
        # If item isn't avail, return None
        if stock_data is None:
            return None
        # Return the item's stock
        return stock_data

    '''4. low_stock(threshold): threshold is a non-negative int. 
    Returns a list of all items whose quantity is less than or equal to threshold, each as a string in the format "item(quantity)". 
    The list is sorted by quantity, smallest first; items with equal quantities are sorted alphabetically by name. 
    Returns an empty list if no items qualify.'''
    def low_stock(self, threshold: int):
        # Pull items and their stock
        items = {(item, quantity) for item, quantity in self.records.items()}
        print(f'items: {items}')
        # Sort by quantity, alphabet
        items_sorted = sorted(items, key=lambda kv:(kv[1], kv[0]))        
        print(f'items_sorted: {items_sorted}')
        # Return specified format
        return [(f'{item}({quantity})') for item, quantity in items_sorted if quantity <= threshold]    
        print(f'items_sorted_formatted: {items_sorted_formatted}')
    
    '''5. restock_plan(threshold, target): threshold is a non-negative int, target is an int greater than threshold. 
    For every item whose quantity is less than or equal to threshold, works out how many units are needed to bring it up to target. 
    Returns a list of strings in the format "item(units_needed)", sorted by units needed, largest first; items with equal units needed are sorted alphabetically by name. 
    This method doesn't change any quantities.'''
    def restock_plan(self, threshold: int, target: int):
        # Dict to store results
        restock_needs = {}
        
        # Loop over items in records
        for item, quantity in self.records.items():
            # For a given item, check if quantity < threshold
            if quantity <= threshold:
                # Check how much s needed to bring stock up to target and store in dict
                qty_needed = target - quantity
                restock_needs[item] = qty_needed
        # Sort by qty, name
        restock_needs_sorted = sorted(restock_needs.items(), key=lambda kv:(-kv[1], kv[0]))
        # Format per spec
        result= [(f'{item}({quantity})') for item, quantity in restock_needs_sorted]
        print(f'result: {result}')
        return result

    '''6. reserve(item, quantity, timestamp, duration): item is a string; quantity and duration are positive ints. 
    Reserves quantity units of the item from timestamp up to, but not including, timestamp + duration. 
    An item has at most one reservation; a new reservation replaces any existing one. 
    Returns True if the item is in the warehouse and its current quantity is at least quantity. 
    Otherwise returns False, and nothing changes.'''
    def reserve(self, item: str, quantity: int, timestamp: int, duration: int):
        # Pull inventory level for item
        stock_data = self.records.get(item, None)
        # If item is in stock and stock >= quantity, proceed
        if stock_data is not None and stock_data >= quantity:
            # Update reservation expiry and quantity
            self.reservation_expiry[item] = timestamp + duration
            self.reservation_qty[item] = quantity
            # Return True per spec
            return True
        # Otherwise, return False per spec
        return False
        
    '''7. available_at(item, timestamp): item is a string. 
    Returns the item's quantity minus the units under a reservation that's active at timestamp, as an int, but never less than 0. 
    Returns None if the item isn't in the warehouse.'''
    def available_at(self, item: str, timestamp: int):
        # Pull inventory and quatity reserved
        inventory = self.records.get(item, None)
        reservation_qty = self.reservation_qty.get(item, 0)
        reservation_date = self.reservation_expiry.get(item, 0)
        print(f'inventory: {inventory}, reservation_qty: {reservation_qty}, reservation_date: {reservation_date}, timestamp: {timestamp}')
        # If inventory is in WH, keep going
        if inventory is not None:
            if reservation_date <= timestamp:
                reservation_qty = 0
            return max(0, inventory-reservation_qty)
        return None

    '''8. remove_stock_at(item, quantity, timestamp): same as remove_stock, at time timestamp, 
    except it returns None, with the quantity unchanged, if the item's available units at timestamp 
    are fewer than quantity.'''
    def remove_stock_at(self, item: str, quantity: int, timestamp: int):
        # Pull inventory and quatity reserved
        inventory = self.records.get(item, None)
        reservation_qty = self.reservation_qty.get(item, 0)
        reservation_date = self.reservation_expiry.get(item, 0)
        print(f'inventory: {inventory}, reservation_qty: {reservation_qty}, reservation_date: {reservation_date}, quantity: {quantity}, timestamp: {timestamp}')
        
        # If the item is is in stock and the reseration is legit, then check if the qty requested is <= avail qty
        if inventory is not None and reservation_date > timestamp: 
            avail_qty = max(inventory - reservation_qty, 0)
            print(f'avail_qty: {avail_qty}')
            # If available units < request, return None
            if avail_qty < quantity:
                print(f'returning none')
                return None
        # If if reservation is not legit, just use strait inventory
        print(f'no valid reservation for this item')
        solution = self.remove_stock(item=item, quantity=quantity)
        print(f'solution: {solution}')
        return solution


# Complexity:
# 1. add_stock --> O(1)
# 2. remove_stock --> O(1)
# 3. get_quantity --> O(1)
# 4. low_stock --> sort O(n log n)
# 5. restock_plan --> loop O(n) + sort O(m log m) w/ m items needing refresh --> m <= n--> O(n log n)
# 6. reserve --> O(1)
# 7. available_at --> O(1)
# 8. remove_stock_at --> O(1)+ remove_stock O(1) --> O(1)
# Worst case: Complexity: O(n log n) w/ memory O(n) w n=items

# Example tests:
warehouse = Warehouse()
assert warehouse.add_stock("bolt", 50) == 50
assert warehouse.remove_stock("bolt", 20) == 30
assert warehouse.add_stock("bolt", 70) == 100 # Qty continues to add

assert warehouse.remove_stock("bolt", 100) == 0 # Qty goes to 0
assert warehouse.remove_stock("bolt", 100) is None # Subtracting too much ret None
assert warehouse.remove_stock("not avail", 100) is None # Unavil item ret None

assert warehouse.get_quantity("bolt") == 0
assert warehouse.add_stock("bolt", 50) == 50
assert warehouse.get_quantity("bolt") == 50


warehouse = Warehouse()
assert warehouse.get_quantity("bolt") is None

warehouse = Warehouse()
warehouse.add_stock("bolt", 5)
warehouse.add_stock("nut", 50)
warehouse.add_stock("screw", 2)
assert warehouse.low_stock(10) == ["screw(2)", "bolt(5)"]
warehouse.add_stock("screw", 3)
assert warehouse.low_stock(10) == ["bolt(5)", "screw(5)"]
assert warehouse.low_stock(1) == []

warehouse = Warehouse()
warehouse.add_stock("bolt", 5)
warehouse.add_stock("screw", 2)
assert warehouse.restock_plan(10, 20) == ["screw(18)", "bolt(15)"]
assert warehouse.restock_plan(10, 20) == ["screw(18)", "bolt(15)"]
warehouse.add_stock("screw", 3)
assert warehouse.restock_plan(10, 20) == ["bolt(15)", "screw(15)"]
assert warehouse.restock_plan(1, 2) == []
assert warehouse.restock_plan(5, 20) == ["bolt(15)", "screw(15)"]


warehouse = Warehouse()
warehouse.add_stock("bolt", 10)
assert warehouse.reserve("bolt", 8, 10, 5) is True
assert warehouse.available_at("bolt", 14) == 2
assert warehouse.available_at("bolt", 15) == 10
assert warehouse.available_at("cow", 14) is None # Item not in WH
warehouse.add_stock("screw", 10)
assert warehouse.reserve("cow", 8, 10, 5) is False # Item not in WH
assert warehouse.reserve("screw", 100, 10, 5) is False # Stock not enough rel to reservation


warehouse = Warehouse()
warehouse.add_stock("bolt", 10)
assert warehouse.reserve("bolt", 8, 10, 5) is True
assert warehouse.available_at("bolt", 14) == 2
assert warehouse.available_at("bolt", 15) == 10


warehouse = Warehouse()
warehouse.add_stock("bolt", 10) # Add 10
warehouse.reserve("bolt", 8, 10, 5) # Reserve 8 until time 15
assert warehouse.remove_stock_at("bolt", 5, 12) is None # Reso valid, req 5 below 2 availble stock
assert warehouse.remove_stock_at("cow", 5, 20) is None # Item not in wh
assert warehouse.remove_stock_at("bolt", 1, 12) == 9 # item not in wh



print('all tests pass')
