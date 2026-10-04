'''
Session 2, Problem 7: In-memory database (progressive)

This problem has 4 levels. 
Each level adds to the same class, and you get the next level only after finishing the current one. 
Your code for earlier levels must keep working as you add later ones.

Level 1. Time limit: 25 minutes, including writing your own tests. 
Aim for working code by about minute 20. Hard stop at 37 minutes.

Write a class that stores records. 
Each record is identified by a key and holds any number of fields, and each field has a value.

Class name: InMemoryDB

Creating an InMemoryDB() takes no arguments, and a new database starts with no records.

Methods:
1. set(key, field, value): key, field, and value are strings. 
Sets that field of the record with that key to value. 
If the record doesn't exist yet, it's created. If the field already has a value, it's replaced.
Returns nothing.
2. get(key, field): key and field are strings. 
Returns the value of that field of that record, as a string. Returns None if the record or the field doesn't exist.
3. delete(key, field): key and field are strings. 
Removes that field from that record. Returns True if the field existed and was removed, or False otherwise.
--------------------------------------------------------------
Session 2, Problem 7: In-memory database. Level 2

Time limit: 25 minutes, including writing your own tests. Aim for working code by about minute 20. Hard stop at 37 minutes.

Add two methods to your InMemoryDB class. Everything from Level 1 must keep working.

New methods:
1. scan(key): key is a string. 
Returns a list of all fields of that record, each as a string in the format "field(value)", sorted alphabetically by field. 
Returns an empty list if the record doesn't exist or has no fields.
2. scan_by_prefix(key, prefix): key and prefix are strings. 
Same as scan, but includes only fields whose names start with prefix.
---------------------------------------------------------------------
Session 2, Problem 7: In-memory database. Level 3

Time limit: 35 minutes, including writing your own tests. 
Aim for working code by about minute 28. Hard stop at 52 minutes.

Add support for fields that expire. 
Everything from Levels 1 and 2 must keep working, and fields set with the old set method never expire.

Every new method takes a timestamp, a non-negative int. 
Timestamps in successive calls never decrease.

New methods:

1. set_at(key, field, value, timestamp): same as set, at time timestamp. 
The field never expires. 
Returns nothing.
2. set_at_with_ttl(key, field, value, timestamp, ttl): ttl is a positive int. 
Same as set_at, except the field exists only from timestamp up to, but not including, timestamp + ttl. 
Returns nothing.
3. get_at(key, field, timestamp): same as get, at time timestamp. 
A field that has expired by timestamp is treated as if it doesn't exist.
4. delete_at(key, field, timestamp): same as delete, at time timestamp. 
Returns False if the field has expired by timestamp.
5. scan_at(key, timestamp): same as scan, at time timestamp, leaving out fields that have expired by timestamp.
'''
    

from math import exp


class InMemoryDB():
    
    def __init__(self):
        # self.records = {"user1": {"name": "ann", "age": "30"}}   # key -> {field: value}
        self.records: dict[str, dict] = {} # Idea: the interior dict holds field:value pairs
        self.expiries: dict[str, dict] = {} # Introduced in phase 3: A second dict that mirrors the first, but for each field's expirations

    def set(self, key: str, field: str, value: str):
        # Pull the fields assocaited with this key
        record_data = self.records.get(key, None)
        # If this key doesn't have fields, attach a dict to populate
        if record_data is None:
            self.records[key] = {}
        # Populate the retrieved (or newly created) dict with this field and that field's value
        self.records[key][field] = value
        print(f'running set...self.records.items() updated to: {self.records.items()}')
        # Ensure the expiries table is updated for this key
        expiry_data = self.expiries.get(key, None)
        if expiry_data is not None:
            # If there is expiry data for this key, remove the field and it's associated expiration. Pop auto-stores the result
            expiry_data.pop(field, None)
            
    def get(self, key: str, field: str):
        # Pulls the fields for this key
        record_data = self.records.get(key, None)
        # If this key doesn't have fields, return None, per spec
        if record_data is None:
            return None
        # If this key has fields, get the value associated with the field name passed in as an argument
        field_data = record_data.get(field, None)
        # If the specified field isn't already saved, return none
        if field_data is None:
            return None
        # Return the value for the field name passed in as an argument
        return field_data
    
     # delete(key, field) -> True if removed | False if missing
    def delete(self, key: str, field: str):
        record_data = self.records.get(key, None)
        if record_data is None:
            return False
        field_data = record_data.get(field, None)
        if field_data is None:
            return False
        del(record_data[field])
        return True

    # scan(key) -> ["field(value)", ...] sorted by field | [] if missing/empty
    def scan(self, key: str):
        record_data = self.records.get(key, None)
        if record_data is None or len(record_data.items()) == 0:
            return []
        sorted_data = sorted(record_data.items())
        print(f'sorted_data: {sorted_data}')
        record_fields = [f'{fields}({values})' for fields, values in sorted_data]
        print(f'running scan...record_fields: {record_fields}')
        return record_fields
    
    def scan_by_prefix(self, key: str, prefix: str):
        # Get the felds pertaining to key
        record_data = self.records.get(key, None)
        # If the key isn't in records, or there are no fields assocaiated w/ that key, return an empty list, per the spec
        if record_data is None or len(record_data.items()) == 0:
            return []
        
        # If the key exists and there are fields assocaited w/ that key, retrieve those fields and their values
        sorted_data = sorted(record_data.items())
        # Create a list into which we will put the filtered and formatted resuls
        record_fields_filtered = []
        # Loop over the retrieved fields and include only those fields where field name starts with prefix
        for field, value in sorted_data:
            if field.startswith(prefix):
                record_fields_filtered.append(f'{field}({value})')
        return record_fields_filtered
    
    '''
    Stage 3 thoughts:
    1. To set expirations for fields --> 
    set_at --> the same as set --> just call self.set
    set_at_with_ttl --> needs to attach expirations to one or more fields within a record
    '''
    '''
    1. set_at(key, field, value, timestamp): same as set, at time timestamp. 
    The field never expires. 
    Returns nothing.
    '''
    def set_at(self, key: str, field: str, value: str, timestamp: int):
        self.set(key=key, field=field, value=value)
        
    '''
    2. set_at_with_ttl(key, field, value, timestamp, ttl): ttl is a positive int. 
    Same as set_at, except the field exists only from timestamp up to, but not including, timestamp + ttl. 
    Returns nothing.
    '''
    def set_at_with_ttl(self, key: str, field: str, value: str, timestamp: int, ttl: int):
        self.set(key=key, field=field, value=value) # Set value, ex expiry
        
        # Get the expiry felds pertaining to key
        expiry_data = self.expiries.get(key, None)
        
        # If there aren't already expiry fields for this key, create an empty dict as the value for that key
        if expiry_data is None:
            self.expiries[key] = {}
        
        # Populate that key's expiry dict
        self.expiries[key][field] = timestamp + ttl
        
        
    '''
    3. get_at(key, field, timestamp): same as get, at time timestamp. 
    A field that has expired by timestamp is treated as if it doesn't exist.
    '''
    def get_at(self, key: str, field: str, timestamp: int):
        get_result = self.get(key, field)
        expiry_data = self.expiries.get(key, None)
        # If there is expiry data for this key, 
        if expiry_data is not None:
            field_expiry = expiry_data.get(field, None)
            if field_expiry is not None and field_expiry <= timestamp:
                return None
        return get_result
    
    '''
    4. delete_at(key, field, timestamp): same as delete, at time timestamp. 
    Returns False if the field has expired by timestamp.
    '''
    def delete_at(self, key: str, field: str, timestamp: int):
        # Check if this key+field is expired
        expiry_data = self.expiries.get(key, None)
        if expiry_data is not None:
            expiration = expiry_data.get(field, None)
            if expiration is not None and expiration <= timestamp:
                # If there is an expiration AND the expiration is passed, return False, per the spec
                return False
            # If there is expiry data for this key+field remove it
            expiry_data.pop(field, None)
        return self.delete(key, field)
    
    '''
    5. scan_at(key, timestamp): same as scan, at time timestamp, leaving out fields that have expired by timestamp.
    '''
    def scan_at(self, key: str, timestamp: int):
        # Pull the fields and their values for key
        record_data = self.records.get(key, None)
        
        # If the key isn't in the class or there are no fields for the key, return []
        if record_data is None or len(record_data.items()) == 0:
            return []
        
        # Otherwise, sort the keys and their values alphabetically by key 
        sorted_data = sorted(record_data.items())
        print(f'sorted_data: {sorted_data}')
        
        # List of non-expired items to actually return
        non_expired = []
        
        # Check if this key is even in the expiries dict
        expiry_data = self.expiries.get(key, None)
        
        # If there is relevant data in the expiries table, check it
        if expiry_data is not None:
            # Look up these keys in the expiry table to check they aren't expired
            for field, value in sorted_data:        
                # Find the expiration date for that field
                expiration_date = expiry_data.get(field, None)
                # If expired, stop and increment loop, skipping appending
                if expiration_date is not None and expiration_date <= timestamp:
                    continue
                # If the record isn't expired (key not in the expiration table, key in table, but no record for field, record for field but not expired), then add to list
                non_expired.append((field, value))
        # If there's no data for this key in the expiries table, just run with the sorted_data from the records table
        else:
            non_expired = sorted_data
            
        result = [f'{fields}({values})' for fields, values in non_expired]
        return result
        
# Complexity: 
# 1. set --> lookups --> O(1)
# 2. get --> O(1)
# 3. delete --> O(1)
# Worst case complexity: O(1)
# Memory --> O(m + n) w/ m = users and n total fields

# 4. scan --> sorting --> O(f log f) w/ f == number of fields in a given record
# 5: scan_by_prefix --> scorting via scan O(f log f) + a loop of those items O(f log f) --> O(f log f) 

# Example tests:
db = InMemoryDB()
db.set("user1", "name", "ann")
db.set("user1", "job", "builder")
db.set("user2", "job", "police")


assert db.get("user1", "name") == "ann"
assert db.get("user1", "job") == "builder"
assert db.get("user2", "name") is None
assert db.get("user2", "job") == "police"

assert db.delete("user2", "job") is True
assert db.delete("user2", "name") is False
assert db.delete("user3", "job") is False

db = InMemoryDB()
assert db.delete("user1", "name") is False

db2 = InMemoryDB()
db2.set("user1", "name", "ann")
db2.set("user1", "age", "30")
assert db2.scan("user1") == ["age(30)", "name(ann)"]

db3 = InMemoryDB()
db3.set("user1", "name", "ann")
db3.set("user1", "nickname", "annie")
db3.set("user1", "age", "30")
assert db3.scan_by_prefix("user1", "n") == ["name(ann)", "nickname(annie)"]
assert db3.scan_by_prefix("user1", "a") == ["age(30)"]
assert db3.scan_by_prefix("user1", "z") == []
assert db3.scan_by_prefix("unlisted user", "z") == []
assert db3.scan_by_prefix("user1", "") == ["age(30)", "name(ann)", "nickname(annie)"]

db4 = InMemoryDB()
db4.set_at_with_ttl("user1", "name", "ann", 10, 5)
assert db4.get_at("user1", "name", 14) == "ann"
assert db4.get_at("user1", "name", 15) is None

db5 = InMemoryDB()
db5.set_at("user1", "name", "ann", 10)
db5.set_at_with_ttl("user1", "age", "30", 10, 5)
assert db5.scan_at("user1", 20) == ["name(ann)"]

print('all tests pass')