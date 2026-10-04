'''
Session 2, Problem 7b: In-memory database (cold rewrite). Level 1

Time limit: 25 minutes, including writing your own tests. Aim for working code by about minute 20. Hard stop at 37 minutes. Start with the 3–5 minute design block.

Write a class that stores records. Each record is identified by a key and holds any number of fields, and each field has a value.

Class name: InMemoryDB

Creating an InMemoryDB() takes no arguments, and a new database starts with no records.

Methods:

1. set(key, field, value): key, field, and value are strings. Sets that field of the record with that key to value. 
If the record doesn't exist yet, it's created. If the field already has a value, it's replaced. 
Returns nothing.
2. get(key, field): key and field are strings. 
Returns the value of that field of that record, as a string. Returns None if the record or the field doesn't exist.
3. delete(key, field): key and field are strings. Removes that field from that record. 
Returns True if the field existed and was removed, or False otherwise.

---------------------------------------------------------------------------------------------------

Session 2, Problem 7b: In-memory database (cold rewrite). Level 2

Time limit: 25 minutes, including writing your own tests. Aim for working code by about minute 20. Hard stop at 37 minutes. Start with the design block.

Add two methods to your InMemoryDB class. Everything from Level 1 must keep working.

New methods:

scan(key): key is a string. Returns a list of all fields of that record, each as a string in the format "field(value)", sorted alphabetically by field. Returns an empty list if the record doesn't exist or has no fields.
scan_by_prefix(key, prefix): key and prefix are strings. Same as scan, but includes only fields whose names start with prefix.

---------------------------------------------------------------------------------------------------
Session 2, Problem 7b: In-memory database (cold rewrite). Level 3

Time limit: 35 minutes, including writing your own tests. 
Aim for working code by about minute 28. Hard stop at 52 minutes. Start with the design block, especially question 1: what must the object remember now?

Add support for fields that expire. 
Everything from Levels 1 and 2 must keep working, and fields set with the old set method never expire.

Every new method takes a timestamp, a non-negative int. Timestamps in successive calls never decrease.

New methods:

6. set_at(key, field, value, timestamp): same as set, at time timestamp. The field never expires. Returns nothing.
7. set_at_with_ttl(key, field, value, timestamp, ttl): ttl is a positive int. Same as set_at, except the field exists only from timestamp up to, but not including, timestamp + ttl. Returns nothing.
8. get_at(key, field, timestamp): same as get, at time timestamp. A field that has expired by timestamp is treated as if it doesn't exist.
9. delete_at(key, field, timestamp): same as delete, at time timestamp. Returns False if the field has expired by timestamp.
10. scan_at(key, timestamp): same as scan, at time timestamp, leaving out fields that have expired by timestamp.

'''

class InMemoryDB:
    
    def __init__(self):
        self.records: dict[str, dict] = {} # Each instance of self.records is a dict w/ key= string (key) and value=a dict holding each field (the key) and its value (the value for that field)
        self.expiries: dict[str, dict] = {} # Each instance of self.expiries is a dict w/ key= string (key) and value=a dict holding each field (the key) and its value (the expiration for that field)
    
    '''1. set(key, field, value): key, field, and value are strings. Sets that field of the record with that key to value. 
    If the record doesn't exist yet, it's created. If the field already has a value, it's replaced. 
    Returns nothing.'''
    def set(self, key: str, field: str, value: str):
        # Check if the record exists 
        field_data = self.records.get(key, None)
        # If record doesn't exist, create it with the value as an empty dict
        if field_data is None:
            self.records[key] = {}
        # Populate the dict for this record with field:value
        self.records[key][field] = value
        # ADDED IN STAGE 3
        self.expiries.get(key, {}).pop(field, None)
        
    '''2. get(key, field): key and field are strings. 
    Returns the value of that field of that record, as a string. Returns None if the record or the field doesn't exist.'''
    def get(self, key: str, field: str):
        # Check if the records exists, return None if not
        field_data = self.records.get(key, None)
        if field_data is None:
            return None
        # Check if the field exists, return None if not
        field_value = field_data.get(field, None)
        if field_value is None:
            return None
        # self.records[key] and self.records[key][field] exist. return the value of self.records[key][field]
        return field_value
    
    '''3. delete(key, field): key and field are strings. Removes that field from that record. 
    Returns True if the field existed and was removed, or False otherwise.'''
    def delete(self, key: str, field: str):
        # Check that self.records[key] exists. Return False if not
        field_data = self.records.get(key, None)
        if field_data is None:
            return False
        # Check if the field exists, return False if not
        field_value = field_data.get(field, None)
        if field_value is None:
            return False
        del(self.records[key][field])
        return True
    
    '''4. scan(key): key is a string. Returns a list of all fields of that record, each as a string in the format "field(value)", 
    sorted alphabetically by field. 
    Returns an empty list if the record doesn't exist or has no fields.'''
    def scan(self, key: str):
        field_data = self.records.get(key, None)
        # Returns an empty list if self.records[key] doesn't exist
        if field_data is None:
            return []
        # Returns an empty list if self.records[key] exists, but it has no associated fields
        if len(field_data.items()) == 0:
            return []
        # Creates the formatted "field(value)" list for each field + value associated with key
        print(f'field_data: {field_data}')
        solution_list = sorted(field_data.items())
        solution_list = [(f'{field}({value})') for field, value in solution_list]   
        return solution_list
    
    '''5. scan_by_prefix(key, prefix): key and prefix are strings. 
    Same as scan, but includes only fields whose names start with prefix'''
    def scan_by_prefix(self, key: str, prefix: str):
        # Get the fields+field values for this key
        field_data = self.records.get(key, None)
        # Returns an empty list if self.records[key] doesn't exist
        if field_data is None:
            return []
        # Returns an empty list if self.records[key] exists, but it has no associated fields
        if len(field_data.items()) == 0:
            return []
        solution_list = sorted(field_data.items())
        # List to store the filtered results
        filtered_results = []
        # Check which scan_results start with prefix and append those to filtered_results
        for field, value in solution_list:
            if field.startswith(prefix):
                # Append to the ending list, in the typical "field(value)" format
                filtered_results.append(f'{field}({value})')
        # Return the new list, still in "field(value)" format, but now only with items starting w/ prefix
        return filtered_results
        
    '''6. set_at(key, field, value, timestamp): same as set, at time timestamp. 
    The field never expires. 
    Returns nothing.'''
    def set_at(self, key: str, field: str, value:str, timestamp: int):
        # This is the same as set, which sets self.records[key][field] = value, returning nothing
        self.set(key=key, field=field, value=value)
    
    '''7. set_at_with_ttl(key, field, value, timestamp, ttl): ttl is a positive int. 
    Same as set_at, except the field exists only from timestamp up to, but not including, timestamp + ttl. 
    Returns nothing.'''
    def set_at_with_ttl(self, key: str, field: str, value: str, timestamp: int, ttl: int):
        # This is the same as set_at, which sets self.records[key][field] = value, returning nothing
        self.set(key=key, field=field, value=value)
        # Since this expires, we need to update the expiries dict too
        expiry_data = self.expiries.get(key, None)
        # Check if record exists in expiries
        if expiry_data is None:
            # If this reord doesn't exist in the expiries dict, create it
            self.expiries[key] = {}
        self.expiries[key][field] = timestamp + ttl
        
    '''8. get_at(key, field, timestamp): same as get, at time timestamp. 
    A field that has expired by timestamp is treated as if it doesn't exist.'''
    def get_at(self, key: str, field: str, timestamp: int):
        # Returns value w/o checking timestamp
        field_value = self.get(key=key, field=field)
        # Check if there is a timestamp for this
        expiry_data = self.expiries.get(key, None)
        if expiry_data is not None:
            expiry_date = expiry_data.get(field, None)
            if expiry_date is not None and expiry_date <= timestamp:
                return None
        return field_value

    '''9. delete_at(key, field, timestamp): same as delete, at time timestamp. 
    Returns False if the field has expired by timestamp.'''
    def delete_at(self, key: str, field: str, timestamp: int):
        # Check if this has a record in expiries
        expiry_data = self.expiries.get(key, None)
        if expiry_data is not None:
            # Check if this record in expiriries has an expiration date that is past
            expiry_date = expiry_data.get(field, None)
            if expiry_date is not None and expiry_date <= timestamp:
                # If expired, don't delete and return False
                return False
        # If record is not expired, run normal delete functionality
        delete_result = self.delete(key=key, field=field)        
        return delete_result
    
    '''10. scan_at(key, timestamp): same as scan, at time timestamp, leaving out fields that have expired by timestamp.'''
    def scan_at(self, key: str, timestamp: int):
        # SCAN PART --> returns list of fields+values for key
        # Check if key is in records dict
        field_data = self.records.get(key, None)
        # Returns an empty list if self.records[key] doesn't exist
        if field_data is None:
            return []
        # Returns an empty list if self.records[key] exists, but it has no associated fields
        if len(field_data.items()) == 0:
            return []
        # Sort by field
        solution_list = sorted(field_data.items())
        print(f'solution_list: {solution_list}')
        
        # EXPIRATION CHECK PART --> Checks scan list, omitting expired items and formatting the remainders
        # Check if this key has a record in expiries
        expiry_data = self.expiries.get(key, None)
        print(f'expiry_data: {expiry_data}')
        
        # If there is a record in expiries for this key, check each field+expiration date
        if expiry_data is not None:    
            result = []    
            # Loop over the items in solution_list to see which ones are expired
            for solution_list_field, solution_list_value in solution_list:
                # Get the corresponding expiry date for each field in solution_list
                expiry_date = expiry_data.get(solution_list_field, None)
                # If there is an expiry_date for this field and it's passed, iterate loop (skipping appending to solutions)
                if expiry_date is not None and expiry_date <= timestamp:
                    continue
                result.append(f'{solution_list_field}({solution_list_value})')
            print(f'returning result: {result}')
            return result
        
        # If there is no expiry data for this record, format the items in solution_list and return        
        solution_list = [(f'{field}({value})') for field, value in solution_list]   
        print(f'returning solution_list: {solution_list}')
        return solution_list
            
            
       
# Complexity: 
# 1. set: O(1)
# 2. get: O(1)
# 3. delte: O(1) 
# 4. scan: sort O(a log a) + loop O(a) w/ a = fields associated w/ key --> O(a + a log a) --> O(a log a)
# 5. scan_by_prefix:  sort O(a log a) + loop O(a) w/ a = fields associated w/ key --> O(a + a log a) --> O(a log a)
# 6. set_at: same as set --> O(1)
# 7. set_at_with_ttl --> same as set_at w/ extra lookup --> O(1)
# 8. get_at --> get with some extra lookups --> O(1)
# 9. delete_at --> runs .get() and .delete() w some lookups --> O(1)
# 10: scan_at --> runs .get() O(1) + loops over solutions_list O(x) w/ x= fields in key + sort O(x log x) --> O(x + x log x) --> O(x log x)
# Worst case complexity: O(a log a) --> a <= n --> O(n log n) w/ memory O(m + n) m=users, n = total fields

# Example tests:
db1 = InMemoryDB()
db1.set("user1", "name", "ann")
db1.set("user2", "name", "bob")
assert db1.get("user1", "name") == "ann"
assert db1.get("user2", "name") == "bob"
db1.set("user2", "name", "ann")
assert db1.get("user2", "name") == "ann"
db1.set("user2", "name", "bob")
assert db1.get("user2", "name") == "bob"

assert db1.get("user1", "name") == "ann"
assert db1.get("user3", "field not included") is None
assert db1.get("user1", "name") == "ann"
assert db1.get("user2", "name") == "bob"

assert db1.delete("user3", "name") is False
assert db1.delete("user1", "field not included") is False
assert db1.delete("user2", "name") is True
assert db1.get("user2", "name") is None


db2 = InMemoryDB()
assert db2.delete("user1", "name") is False

db3 = InMemoryDB()
db3.set("user1", "name", "ann")
db3.set("user1", "age", "30")
assert db3.scan("user1") == ["age(30)", "name(ann)"]
assert db3.scan("user2") == []
db3.set("user3", "age", "30")
assert db3.delete("user3", "age") is True
assert db3.scan("user3") == []


db4 = InMemoryDB()
db4.set("user1", "name", "ann")
db4.set("user1", "nickname", "annie")
db4.set("user1", "age", "30")
assert db4.scan_by_prefix("user1", "n") == ["name(ann)", "nickname(annie)"]
db4.set("user1", "age", "30")
assert db4.scan_by_prefix("user1", "bad prefix") == []
assert db4.delete("user1", "name") is True
assert db4.scan_by_prefix("user1", "n") == ["nickname(annie)"]
assert db4.scan_by_prefix("unlisted user", "n") == []


'''def set_at_with_ttl(self, key: str, field: str, value: str, timestamp: int, ttl: int):'''
db5 = InMemoryDB()
db5.set_at_with_ttl("user1", "name", "ann", 10, 5) # Expiration = 15
assert db5.get_at("user1", "name", 14) == "ann" # Valid
assert db5.get_at("user1", "name", 15) is None # Expired
db5.set_at_with_ttl("user1", "name", "ann", 20, 25) # Expiration = 45
assert db5.get_at("user1", "name", 24) == "ann" # Valid
assert db5.get_at("user1", "name", 45) is None # Expired


db6 = InMemoryDB()
db6.set_at("user1", "name", "ann", 10)
db6.set_at_with_ttl("user1", "age", "30", 10, 5) # Expiry = 15
assert db6.scan_at("user1", 20) == ["name(ann)"]



db7 = InMemoryDB()
db7.set_at_with_ttl("user1", "age", "30", 10, 5) # Expiry= 15
assert db7.delete_at("user1", "age", 10) is True
assert db7.delete_at("user1", "age", 20) is False
assert db7.delete_at("user1", "age", 15) is False


db8 = InMemoryDB()
db8.set_at_with_ttl("user1", "age", "30", 10, 5) # Expiry= 15

db9 = InMemoryDB()
db9.set_at_with_ttl("user1", "name", "ann", 5, 7) # Expiry = 12
db9.set_at_with_ttl("user1", "age", "30", 10, 5) # Expiry = 15
assert db9.scan_at("user1", 10) == ["age(30)", "name(ann)"]
assert db9.scan_at("user1", 12) == ["age(30)"]
assert db9.scan_at("user1", 20) == []


print('all tests complete')