'''
Session 2, Problem 8: File storage (progressive). Level 1

This problem has 4 levels, and we'll do Levels 1–3. Each level adds to the same class, and your earlier levels must keep working.

Time limit: 25 minutes, including writing your own tests. 
Aim for working code by about minute 20. Hard stop at 37 minutes. Start with the design block.

Write a class that stores files by name.

Class name: FileStorage

Creating a FileStorage() takes no arguments, and a new storage starts with no files.

Methods:

1. add_file(name, size): name is a string, size is a non-negative int. Adds a file with that name and size. Returns True if the file was added, or False if a file with that name already exists (the existing file is left unchanged).
2. get_file_size(name): name is a string. Returns the file's size as an int, or None if there is no file with that name.
3. delete_file(name): name is a string. Removes the file and returns its size, as an int. Returns None if there is no file with that name.

----------------------------------------------------
Session 2, Problem 8: File storage. Level 2

Time limit: 25 minutes, including writing your own tests. Aim for working code by about minute 20. Hard stop at 37 minutes. Start with the design block.

Add two methods to your FileStorage class. Everything from Level 1 must keep working.

New methods:

find_files(prefix, suffix): prefix and suffix are strings. Returns a list of all files whose names start with prefix and end with suffix, each as a string in the format "name(size)". The list is sorted by size, largest first; files with equal sizes are sorted alphabetically by name. Returns an empty list if no files match.
largest(n): n is a non-negative int. Returns a list of the n largest files, in the same format and order as find_files. If there are fewer than n files, returns all of them.

----------------------------------------------------
Session 2, Problem 8: File storage. Level 3

Time limit: 35 minutes, including writing your own tests. 
Aim for working code by about minute 28. Hard stop at 52 minutes. 
Start with the design block, especially: what must the object remember now?

Add support for files that expire. 
Everything from Levels 1 and 2 must keep working, and files added with the old add_file method never expire.

Every new method takes a timestamp, a non-negative int. Timestamps in successive calls never decrease.

New methods:

add_file_at(name, size, timestamp): same as add_file, at time timestamp. The file never expires. A file that has expired by timestamp is treated as if it doesn't exist, so adding a file with that name succeeds and replaces it.
add_file_at_with_ttl(name, size, timestamp, ttl): ttl is a positive int. Same as add_file_at, except the new file exists only from timestamp up to, but not including, timestamp + ttl.
get_file_size_at(name, timestamp): same as get_file_size, at time timestamp. A file that has expired by timestamp is treated as if it doesn't exist.
find_files_at(prefix, suffix, timestamp): same as find_files, at time timestamp, leaving out files that have expired by timestamp.

'''

class FileStorage:
    
    def __init__(self):
        self.records : dict[str, int] = {}
        self.expirations: dict[str, int] = {}
    
    '''1. add_file(name, size): name is a string, size is a non-negative int. Adds a file with that name and size. 
    Returns True if the file was added, or False if a file with that name already exists (the existing file is left unchanged).'''        
    def add_file(self, name: str, size: int):       
        # Check if the file is already in records
        file_data = self.records.get(name, None)
        # If file is already there, return False, per spec
        if file_data is not None:
            return False
        # If file isn't already there, insert it into recods and return True
        self.records[name] = size
        # If there's an expiration for this file, pop it. the new expiration will be written in add_file_at_with_ttl
        self.expirations.pop(name, None)
        return True
    
    '''2. get_file_size(name): name is a string. 
    Returns the file's size as an int, or None if there is no file with that name.'''
    def get_file_size(self, name: str):
        file_data = self.records.get(name, None)
        if file_data is None:
            return None
        return self.records[name]
        
    '''3. delete_file(name): name is a string. 
    Removes the file and returns its size, as an int. 
    Returns None if there is no file with that name.'''
    def delete_file(self, name: str):
        file_data = self.records.get(name, None)
        if file_data is None:
            return None
        self.records.pop(name, None)
        return file_data

    '''4. find_files(prefix, suffix): prefix and suffix are strings. 
    Returns a list of all files whose names start with prefix and end with suffix, each as a string in the format "name(size)". 
    The list is sorted by size, largest first; files with equal sizes are sorted alphabetically by name. 
    Returns an empty list if no files match.'''
    def find_files(self, prefix: str, suffix: str):
        # Pull all records
        file_data = self.records.items()
        print(f'file_data: {file_data}')
        # Sort by size, then alphabet
        file_data_sorted = sorted(file_data, key=lambda kv:(-kv[1], kv[0]))
        print(f'find_files...returning file_data_sorted: {file_data_sorted}')
        # Filter again for prefix+suffix and return formatted version
        file_data_sorted_filtered = [(f'{name}({size})') for name, size in file_data_sorted if name.startswith(prefix) and name.endswith(suffix)]
        print(f'find_files...returning file_data_sorted_filtered: {file_data_sorted_filtered}')
        return file_data_sorted_filtered

    '''5. largest(n): n is a non-negative int. 
    Returns a list of the n largest files, in the same format and order as find_files. 
    If there are fewer than n files, returns all of them.'''
    def largest(self, n: int):
        # Pull file data
        file_data = self.records.items()
        
        # Sort files
        file_data_sorted = sorted(file_data, key=lambda kv:(-kv[1], kv[0]))
        print(f'file_data_sorted: {file_data_sorted}')
        
        solution_formatted = [(f'{name}({size})') for name, size in file_data_sorted]
        # If fewer than n files, return all of them, per spec
        # Otherwise, return top n files
        # Note: the splice handles all of this
        return solution_formatted[:n]
    
    
    '''6. add_file_at(name, size, timestamp): same as add_file, at time timestamp.
    The file never expires. 
    A file that has expired by timestamp is treated as if it doesn't exist, so adding a file with that name succeeds and replaces it.'''
    def add_file_at(self, name:str, size: int, timestamp: int):
        # If the file is (a) in expirations and (b) has expired, remove it from records and then use the normal add functionality
        expiration_date = self.expirations.get(name, None)
        if expiration_date is not None and expiration_date <= timestamp:
            self.records.pop(name, None)
                    
        # If file isn't in the record and it's not expired, insert it into recods and return True
        return self.add_file(name=name, size=size)

        
    '''7. add_file_at_with_ttl(name, size, timestamp, ttl): ttl is a positive int. 
    Same as add_file_at, except the new file exists only from timestamp up to, but not including, timestamp + ttl.'''
    def add_file_at_with_ttl(self, name: str, size: int, timestamp: int, ttl: int):
        # Check if file is expired
        expiration_date = self.expirations.get(name, None)
        # If there is an expiration date and the file is expired, remove it from records, so that it doesn't trip up that function
        if expiration_date is not None and expiration_date <= timestamp:
            self.records.pop(name, None)
        # Add file to records dict 
        result = self.add_file(name=name, size=size)
        # If the record was added to results successfully also add/update the expirations table
        if result is True:
            # Add corresponding expiration to dict
            self.expirations[name] = timestamp + ttl
        return result

    '''8. get_file_size_at(name, timestamp): same as get_file_size, at time timestamp. 
    A file that has expired by timestamp is treated as if it doesn't exist.'''
    def get_file_size_at(self, name: str, timestamp: int):
        expiration_date = self.expirations.get(name, None)
        print(f'get_file_size_at...self.expirations.items(): {self.expirations.items()}')
        print(f'get_file_size_at...expiration_date: {expiration_date}')
        
        # If the expiration date is <= today, return None
        if expiration_date is not None and expiration_date <= timestamp:
            print(f'get_file_size_at...returning none')
            return None
        
        # If file isn't expired, then run the typical get_file_size
        print(f'get_file_size_at... returning self.get_file_size(name=name): {self.get_file_size(name=name)}')
        return self.get_file_size(name=name)
    
    '''9. find_files_at(prefix, suffix, timestamp): same as find_files, at time timestamp, 
    leaving out files that have expired by timestamp.'''
    def find_files_at(self, prefix: str, suffix: str, timestamp: int):
        
        # List to store formatted results
        solutions = {}
        
        # Loop across all the file data to get the name and size of each
        for name, size in self.records.items():
            expiration_date = self.expirations.get(name, None)
            # If there is an expiration date for this file and it's passed, continue (do not append)
            if expiration_date is not None and expiration_date <= timestamp:
                print(f'find_files_at...skipping name: {name} w/ expiration_date: {expiration_date} at timestamp: {timestamp}')
                continue
            solutions[name] = size
        
        # Sort by size, then alphabet
        solutions_sorted = sorted(solutions.items(), key=lambda kv:(-kv[1], kv[0]))
        print(f'find_files_at...returning solutions_sorted: {solutions_sorted}')
        # Filter again for prefix+suffix and return formatted version
        solutions_sorted_filtered = [(f'{name}({size})') for name, size in solutions_sorted if name.startswith(prefix) and name.endswith(suffix)]
        print(f'find_files_at...returning solutions_sorted_filtered: {solutions_sorted_filtered}')
        return solutions_sorted_filtered
                


# Complexity:
# 1. add_file --> O(1)
# 2. get_file_size --> O(1)
# 3. delete_file --> O(1)
# 4. find_files --> sorting O(n log n) + list comprehension O(n) --> O(n log n)
# 5. largest --> sorting O(n log n) + list comprehension O(n) --> O(n log n)
# 6. add_file_at --> pop on a dict --> O(1)
# 7. add_file_at_with_ttl --> add_file O(1) + pop() on a dict O(1) --> O(1)
# 8. get_file_size_at --> some lookups + get_file_size --> O(1)
# 9. find_files_at --> loop over records O(n) + sorting non-expired files O(n log n) + filtering for prefix/suffit O(n) --> O(n log n)
# Worst case: O(n log n) w/ memory O(n) w/ n=number of files


# Example tests:
storage = FileStorage()
assert storage.add_file("a.txt", 100) is True
assert storage.add_file("a.txt", 100) is False


assert storage.get_file_size("a.txt") == 100
assert storage.get_file_size("missing file") is None

storage2 = FileStorage()
assert storage2.delete_file("a.txt") is None
assert storage2.add_file("a.txt", 100) is True
assert storage2.delete_file("a.txt") == 100
assert storage2.get_file_size("a.txt") is None

storage3 = FileStorage()
storage3.add_file("a.txt", 100)

storage3.add_file("b.txt", 300)
storage3.add_file("a.csv", 200)
assert storage3.find_files("a", ".txt") == ["a.txt(100)"]
assert storage3.find_files("bad prefix", "bad suffix") == []
assert storage3.find_files("a", "bad suffix") == []

storage3.add_file("za.txt", 100)
storage3.add_file("zb.txt", 100)
assert storage3.find_files("z", ".txt") == ["za.txt(100)", "zb.txt(100)"]
assert storage3.find_files("z", ".txt") == ["za.txt(100)", "zb.txt(100)"]

storage4 = FileStorage()
storage4.add_file("a.txt", 100)
storage4.add_file("b.txt", 300)
assert storage4.largest(1) == ["b.txt(300)"]
storage4.add_file("c.txt", 300)
storage4.add_file("d.txt", 300)
assert storage4.largest(1) == ["b.txt(300)"]
assert storage4.largest(2) == ["b.txt(300)", "c.txt(300)"]
assert storage4.largest(10) == ["b.txt(300)", "c.txt(300)", "d.txt(300)", "a.txt(100)"]

storage5 = FileStorage()
storage5.add_file("za.txt", 100)
storage5.add_file("zb.txt", 200)
assert storage5.find_files("z", ".txt") == ["zb.txt(200)", "za.txt(100)"]

storage6 = FileStorage()
storage6.add_file("za.txt", 100)
storage6.add_file("zb.txt", 200)

storage7 = FileStorage()
assert storage7.add_file_at_with_ttl("a.txt", 100, 10, 5) is True
assert storage7.get_file_size_at("a.txt", 14) == 100
assert storage7.get_file_size_at("a.txt", 15) is None

storage8 = FileStorage()
storage8.add_file_at_with_ttl("a.txt", 100, 10, 5) # Expiration 15
assert storage8.add_file_at("a.txt", 50, 20) is True # Expired so gets added
assert storage8.get_file_size_at("a.txt", 30) == 50 


print('tests pass')