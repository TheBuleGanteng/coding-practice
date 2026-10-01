'''
Problem 1: Inventory (class warm-up)

Time limit: none. 
This is an untimed warm-up to refresh class syntax. 
As a rough guide, aim for about 20 minutes. Try it from memory first. 
If you're stuck on syntax for more than 5 minutes, looking it up is fine; note that you did.

Write a class that tracks how many units of each item a shop holds.

Class name: Inventory

Methods:
add(item, qty): item is a string, qty an int ≥ 1. Adds qty units of item. Returns nothing.
remove(item, qty): item is a string, qty an int ≥ 1. If the inventory holds at least qty units of item, it removes them and returns True. Otherwise it changes nothing and returns False.
count(item): item is a string. Returns the number of units of item held, as an int. That's 0 if the item was never added or has been fully removed.
list_items(): no arguments. Returns a list of (item, qty) tuples for every item with a quantity greater than 0, sorted alphabetically by item name.

Creating an Inventory() takes no arguments, and a new inventory starts empty.
'''
# USING A DATACLASS
from dataclasses import dataclass, field # Step 1: Imports

@dataclass # Step 2: Add decorator
class Inventory: # Step 3: Define class name
    
    stock: dict = field(default_factory=dict)   # each Inventory() gets its own new, empty dict, That dict is accessed via self.stock

    def add(self, item, qty):
        # 1. Checks if "item" exists in the "stock" dict
        # 2a. If yes, returns the quantity via self.stock[item] 
        # 2b. If no, returns the fallback value of 0
        # 3. Adds qty, and updates self.stock[item] with the resulting sum
        self.stock[item] = self.stock.get(item, 0) + qty 
        print(f'self.stock[item] updated to: {self.stock[item]}')

    def remove(self, item, qty):
        # 1. Checks if "item" exists in the "stock" dict
        # 2a. If yes, returns the quantity via self.stock[item]
        # 2b. If no, returns fallback value of 0
        # 3. Checks if qty > qty available
        # 4a. If qty > qty_available, returns False, per spec
        # 4b: If qty <= qty_available, updates value (pieces on hand) for self.stock[item] and returns True, per spec
        qty_available = self.stock.get(item, 0)
        if qty > qty_available:
            remove_result = False
            print(f'returning remove_result: {remove_result}')
            return remove_result
        else:
            self.stock[item] -= qty
            print(f'self.stock[item] updated to: {self.stock[item]}')
            remove_result = True
            print(f'returning remove_result: {remove_result}')
            return remove_result
            
        
    def count(self, item):
        # Check if item is in dict
        # 2a. If yes, returns the quantity via self.stock[item]
        # 2b. If no, returns fallback value of 0
        count_result = self.stock.get(item, 0) 
        print(f'count_result: {count_result}')
        return count_result

    def list_items(self):
        # List comprehension with the following elements:
        # 1. [] --> result is a list
        # 2. (item, qty) --> put item and qty in the new list
        # 3. for item, qty in self.stock.items() --> what to loop over
        # 4. if count(item) > 0 --> keeps items with count > 0 (optional), per spec
        
        list_items_result = sorted([(item, qty) for item, qty in self.stock.items() if qty > 0]) 
        print(f'list_items_result: {list_items_result}')
        return list_items_result



#Tests

# First create the object
inv = Inventory()
# Test that an item not in dict returns 0 per spec
assert inv.count("apple") == 0 
# Update inventory
inv.add("apple", 5) 
inv.add("banana", 2)
inv.add("apple", 3)
# More tests per spec
assert inv.count("apple") == 8
assert inv.remove("apple", 10) is False
assert inv.count("apple") == 8
assert inv.remove("apple", 8) is True
assert inv.count("apple") == 0
assert inv.list_items() == [("banana", 2)]
assert inv.remove("cherry", 1) is False
inv.add("cherry", 1)
assert inv.list_items() == [("banana", 2), ("cherry", 1)]

# First create the object
inv2 = Inventory()
assert inv2.list_items() == []    # a second inventory must not share data with the first
print("all tests passed")