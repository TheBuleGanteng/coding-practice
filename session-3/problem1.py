'''
Session 3, Problem 1: LRU cache (progressive). Level 1

Time limit: 25 minutes, including writing your own tests. Aim for working code by about minute 20. Hard stop at 37 minutes. Before coding: write __init__ with an example comment, run one example call through it, and check that your dict keys are unique and are what the spec looks things up by.

Write a cache that holds a limited number of items and, when full, discards the item that was used least recently.

Class name: LRUCache

Creating an LRUCache(capacity) takes one argument: capacity, a positive int, the maximum number of items the cache can hold. A new cache starts empty.

An item counts as used when it’s added, updated, or successfully read with get.

Methods:

put(key, value): key and value are strings. Stores value under key, replacing any existing value, and marks the item as most recently used. If adding a new key makes the cache hold more than capacity items, removes the least recently used item. Returns the key that was removed, or None if nothing was removed.
get(key): key is a string. Returns the value stored under key and marks the item as most recently used. Returns None if the key isn’t in the cache.
oldest(): no arguments. Returns the key of the least recently used item, or None if the cache is empty.
newest(): no arguments. Returns the key of the most recently used item, or None if the cache is empty.

Session 3, Problem 1: LRU cache. Level 2

Time limit: 25 minutes, including writing your own tests. Aim for working code by about minute 20. Hard stop at 37 minutes. Start with one example call through your structure.

Add two methods to your LRUCache class. Everything from Level 1 must keep working.

New methods:

peek(key): key is a string. Returns the value stored under key without marking the item as used, so its position in the usage order doesn’t change. Returns None if the key isn’t in the cache.
resize(new_capacity): new_capacity is a positive int. Changes the cache’s capacity to new_capacity. If the cache now holds more items than the new capacity, removes least recently used items until it fits. Returns a list of the removed keys, in the order they were removed (least recently used first). Returns an empty list if nothing was removed.


Session 3, Problem 1: LRU cache. Level 3

Time limit: 35 minutes, including writing your own tests. Aim for working code by about minute 28. Hard stop at 52 minutes. Start with your structures (with examples) and one example call, and check which existing methods need to change.

Add items that expire. Everything from Levels 1 and 2 must keep working.

Every new method takes a timestamp, a non-negative int. Timestamps in successive calls never decrease.

New methods:

put_at(key, value, timestamp, ttl): key and value are strings; timestamp and ttl are ints, with ttl positive. Same as put (including marking the item as used, removing the least recently used item when over capacity, and the return value), except the item expires: it exists from timestamp up to, but not including, timestamp + ttl.
get_at(key, timestamp): key is a string. Same as get, except that if the item has expired by timestamp, it’s removed from the cache and None is returned (and it isn’t marked as used).
purge_expired(timestamp): removes every item that has expired by timestamp. Returns the number of items removed, as an int.

Changes to existing behavior:

A plain put on a key removes any expiry that key had, so the item no longer expires.
Whenever an item leaves the cache for any reason, its expiry is discarded too.

'''
class LRUCache():
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.records: dict[str, str] = {} # k=key, v=value
        self.expiries: dict[str, int] = {} # k=key, v= expiration
        
    '''1. put(key, value): key and value are strings. 
    Stores value under key, replacing any existing value, and marks the item as most recently used. 
    If adding a new key makes the cache hold more than capacity items, removes the least recently used item. 
    Returns the key that was removed, or None if nothing was removed.'''
    def put(self, key: str, value: str):
        # If the items is in the dict, remove it
        self.records.pop(key, None)
        # Remove the expiry, if there is one
        self.expiries.pop(key, None)
        # Set the dict
        self.records[key] = value
        # Check if we are over capacity
        if len(self.records) > self.capacity:
            # If so, pop the first (oldest) item in the dict and return its key
            oldest_key = next(iter(self.records))
            self.records.pop(oldest_key, None)
            # Update per part 3: Also remove the expiry
            self.expiries.pop(oldest_key, None)
            return oldest_key
        # If nothing removed, return None
        return None

    '''2. get(key): key is a string. 
    Returns the value stored under key and marks the item as most recently used. 
    Returns None if the key isn’t in the cache.'''
    def get(self, key: str):
        # Need to pop the item
        pop_val = self.records.pop(key, None)
        expiration = self.expiries.get(key, None)
        # Update per part 3: Also remove the expiry
        self.expiries.pop(key, None)
        # Reset dict
        if pop_val is not None:
            self.records[key] = pop_val
            if expiration is not None:
                self.expiries[key] = expiration
        return pop_val


    '''3. oldest(): no arguments. 
    Returns the key of the least recently used item, or None if the cache is empty.'''
    def oldest(self):
        return next(iter(self.records), None)


    '''4. newest(): no arguments. 
    Returns the key of the most recently used item, or None if the cache is empty.'''
    def newest(self):
        return next(reversed(self.records), None)
    
    '''5. peek(key): key is a string. 
    Returns the value stored under key without marking the item as used, so its position in the usage order doesn’t change. 
    Returns None if the key isn’t in the cache.'''
    def peek(self, key: str):
        return self.records.get(key, None)
    
    
    
    '''6. resize(new_capacity): new_capacity is a positive int. 
    Changes the cache’s capacity to new_capacity. 
    If the cache now holds more items than the new capacity, removes least recently used items until it fits. 
    Returns a list of the removed keys, in the order they were removed (least recently used first). 
    Returns an empty list if nothing was removed.'''
    def resize(self, new_capacity: int):
        # List to store removed keys
        removed = []
        # Change capacity
        self.capacity = new_capacity
        # Check if cache is over limit
        while len(self.records) > new_capacity:
            # Get the key to remove and append to list
            rm_key = next(iter(self.records))
            removed.append(rm_key)
            # Pop the first record
            self.records.pop(rm_key)
            # Update per part 3: Also remove the expiry
            self.expiries.pop(rm_key, None)
        return removed
    
    '''7. put_at(key, value, timestamp, ttl): key and value are strings; timestamp and ttl are ints, with ttl positive. 
    Same as put (including marking the item as used, removing the least recently used item when over capacity, and the return value), except the item expires: it exists from timestamp up to, but not including, timestamp + ttl.'''
    def put_at(self, key: str, value: str, timestamp: int, ttl: int):
        # Call put
        put_result = self.put(key=key, value=value)
        # Update expiration
        self.expiries[key] = timestamp+ttl
        return put_result
        
    
    '''8. get_at(key, timestamp): key is a string. 
    Same as get, except that if the item has expired by timestamp, it’s removed from the cache and None is returned (and it isn’t marked as used).'''
    def get_at(self, key: str, timestamp: int):
        # Check if this key has an expiration date
        expiry_data = self.expiries.get(key, None)
        # If has expiration date, remove if expired
        if expiry_data is not None and expiry_data <= timestamp:
            # Remove item from both dicts
            self.expiries.pop(key)
            self.records.pop(key)
            return None
        result= self.get(key=key)
        return result
    
    '''9. purge_expired(timestamp): removes every item that has expired by timestamp. 
    Returns the number of items removed, as an int.'''
    def purge_expired(self, timestamp: int):
        to_remove = []
        for key, value in self.records.items():
            expiration = self.expiries.get(key, None)
            if expiration is not None and expiration <= timestamp:
                to_remove.append(key)
        for key in to_remove:
            self.expiries.pop(key)
            self.records.pop(key)
        return len(to_remove)
            
    
    
# Complexity:
# k = number of key:value pairs
# n = items in excess of new capacity
# r = items to delete
# 1. put --> O(1)
# 2. get --> O(1)
# 3. oldest --> O(1)
# 4. newest --> O(1)
# 5. peek --> O(1)
# 6. resize --> O(n)
# 7. put_at --> O(1)
# 8. get_at --> O(1)
# 9. purge_expired --> loop over all records O(k) + Loop over keys to remove O(r)


# Worst-case complexity: O(k + r) with r <= k--> O(k)
# Memory: O(k + r)

# Example tests:

cache = LRUCache(2)
cache.put("a", "1")
cache.put("b", "2")
cache.get("a")
assert cache.put("c", "3") == "b"


cache = LRUCache(100)
cache.put("a", "1")
cache.put("b", "2")
assert cache.put("d", "3") is None # nothing removed

cache = LRUCache(2)
cache.put("a", "1")
cache.put("b", "2")
assert cache.oldest() == "a"
assert cache.newest() == "b"
cache.put("a", "3")
assert cache.oldest() == "b" # Updates newest/oldest
assert cache.newest() == "a" # Updates newest/oldest
assert cache.get("b") == "2" # basic use of get
assert cache.newest() == "b" # Updates newest based on get


cache = LRUCache(2)
cache.put("a", "1")
cache.put("b", "2")
assert cache.peek("a") == "1"
assert cache.put("c", "3") == "a"
assert cache.peek("d") is None # Key isn't in there

cache = LRUCache(3)
cache.put("a", "1")
cache.put("b", "2")
cache.put("c", "3")
assert cache.resize(1) == ["a", "b"]
assert cache.resize(100) == [] # Nothing removed


cache = LRUCache(2)
cache.put_at("a", "1", 10, 5)
assert cache.get_at("a", 14) == "1"
assert cache.get_at("a", 15) is None
assert cache.get_at("b", 14) is None # Key doesn't exist

cache = LRUCache(3)
cache.put_at("a", "1", 10, 5)
cache.put("b", "2")
assert cache.purge_expired(20) == 1

cache = LRUCache(3)
cache.put_at("a", "1", 10, 50)
cache.put("b", "2")
assert cache.purge_expired(20) == 0 # nothing expired

print('all tests pass')