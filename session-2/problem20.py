'''
Session 2, Problem 20: Document versions (progressive). Level 1

Time limit: 25 minutes, including writing your own tests. Aim for working code by about minute 20. Hard stop at 37 minutes. Before coding: write __init__ with an example comment, run one example call through it, and check which row of your structures table this is.

Write a class that saves versions of documents over time, keeping every version.

Class name: DocumentStore

Creating a DocumentStore() takes no arguments, and a new store starts empty.

For any one document, the timestamps in successive save calls always strictly increase.

Methods:

save(doc, text, timestamp): doc and text are strings, timestamp is a non-negative int. Saves text as a new version of the document at time timestamp, keeping all earlier versions. Returns the new version’s number, as an int: 1 for a document’s first version, 2 for its second, and so on.
text_at(doc, timestamp): doc is a string, timestamp is a non-negative int. Returns the text of the version saved at the largest timestamp less than or equal to timestamp. Returns None if the document doesn’t exist or has no version saved at or before timestamp.
first_saved(doc): doc is a string. Returns the timestamp of the document’s first version, as an int, or None if the document doesn’t exist.
Session 2, Problem 20: Document versions. Level 2

Time limit: 25 minutes, including writing your own tests. Aim for working code by about minute 20. Hard stop at 37 minutes. Start with your one-line variable list and one example call through your structure.

Add two methods to your DocumentStore class. Everything from Level 1 must keep working.

New methods:

version_at(doc, timestamp): doc is a string, timestamp is a non-negative int. Returns the number of the version in effect at that time, as an int: the number of versions saved at or before timestamp. Returns 0 if the document doesn’t exist or has no version saved at or before timestamp.
recently_edited(since): since is a non-negative int. Returns a list of all documents whose most recent version was saved at a timestamp greater than or equal to since. The list is sorted by that most recent timestamp, latest first; documents with equal timestamps are sorted alphabetically. Returns an empty list if there are none.

'''
# Example tests:

class DocumentStore:
    
    def __init__(self):
        self.records: dict[str, dict[int, str]] = {} #k=doc(str), inner dict k=ts(int), v=text(str)
        
    '''1. save(doc, text, timestamp): doc and text are strings, timestamp is a non-negative int. 
    Saves text as a new version of the document at time timestamp, keeping all earlier versions. 
    Returns the new version’s number, as an int: 1 for a document’s first version, 2 for its second, and so on.'''
    def save(self, doc: str, text: str, timestamp: int):
        text_info = self.records.get(doc, None)
        
        # If a new doc, set the initial dict
        if text_info is None:
            version = 1
            self.records[doc] = {timestamp: text}
            return version
        # If not new, append the new version
        self.records[doc][timestamp] = text
        length = len(self.records[doc])
        return length

    '''2.text_at(doc, timestamp): doc is a string, timestamp is a non-negative int. 
    Returns the text of the version saved at the largest timestamp less than or equal to timestamp. 
    Returns None if the document doesn’t exist or has no version saved at or before timestamp.'''
    def text_at(self, doc: str, timestamp: int):
        doc_data = self.records.get(doc, None)
        # Return None if doc doesn't exist
        if doc_data is None:
            return None
        # Before looping, set result to None, in case the loop doesn't return results
        result= None
        # Loop through each item assoc with doc
        for doc_timestamp, doc_text in doc_data.items():
            # Check if timestamp has crossed the threshold
            if doc_timestamp > timestamp:
                break
            # Returns the prior text
            result = doc_text
        return result
        
    '''3. first_saved(doc): doc is a string. 
    Returns the timestamp of the document’s first version, as an int, or None if the document doesn’t exist.'''
    def first_saved(self, doc: str):
        if self.records.get(doc, None) is not None:
            return min(timestamp for timestamp, text in self.records[doc].items())
        return None

    '''4. version_at(doc, timestamp): doc is a string, timestamp is a non-negative int. 
    Returns the number of the version in effect at that time, as an int: the number of versions saved at or before timestamp. 
    Returns 0 if the document doesn’t exist or has no version saved at or before timestamp.'''
    def version_at(self, doc: str, timestamp: int):
        book_data = self.records.get(doc, None)
        solution_list = []
        if book_data is not None:
            for book_timestamp, book_text in book_data.items():
                if book_timestamp > timestamp:
                    break
                solution_list.append(book_text)
        solution = len(solution_list)
        print(f'solution: {solution}')
        return solution


    '''5. recently_edited(since): since is a non-negative int. 
    Returns a list of all documents whose most recent version was saved at a timestamp greater than or equal to since. 
    The list is sorted by that most recent timestamp, latest first; documents with equal timestamps are sorted alphabetically. 
    Returns an empty list if there are none.'''
    def recently_edited(self, since: int): 
        doc_list = []
        # Loop through each doc
        for doc, doc_data in self.records.items():
            # Get the max timestamp for each doc (the key in doc_data)
            max_timestamp = max(doc_data)
            # Check if this timestamp is >= since
            if max_timestamp >= since:
                # If yes, append doc, timestamp to list
                doc_list.append((doc, max_timestamp))
        # Sort list by most recent timestamp, then alpha
        sorted_pairs = sorted(doc_list, key=lambda kv: (-kv[1], kv[0]))
        solution = [doc_title for doc_title, doc_timestamp in sorted_pairs]
        print(f'solution: {solution}')
        return solution
        
          




# Complexity
# v = all versions for a given book
# t = total versions across all books
# b = total books
# 1. save --> O(1)
# 2. text_at --> O(v)
# 3. first_saved --> min on all the versions for a book --> O(v)
# 4. version_at --> O(v)
# 5. recently_edited --> loops through all books O(b) --> Looks across the various versions of each book, which add up to O(t) --> O(b + t) --> since b <= t --> O(t) --> then sort by books O(b log b) --> O(t + b log b) --> then extract titles O(b) --> O(t + b log b + b) --> since b < b log b --> O(t + b log b)

# Worst case complexity: O(t + b log b)
# Memory: O(b + t)


store = DocumentStore()
assert store.save("notes", "draft", 10) == 1
assert store.save("notes", "final", 20) == 2
assert store.save("book", "draft", 20) == 1 # New book still 1

assert store.text_at("notes", 15) == "draft"
assert store.text_at("notes", 10) == "draft" # At timestamp
assert store.text_at("notes", 1) is None # No text at timestamp
assert store.text_at("notes", 30) == "final" # Greater than timestamp


store = DocumentStore()
store.save("notes", "draft", 10)
assert store.first_saved("notes") == 10
assert store.first_saved("book") is None # doesn't exist

store = DocumentStore()
store.save("notes", "a", 10)
store.save("notes", "b", 20)
store.save("notes", "c", 30)
assert store.version_at("notes", 25) == 2
assert store.version_at("book", 25) == 0 # no such doc
assert store.version_at("notes", 1) == 0 # No version saved at this time


store = DocumentStore()
assert store.recently_edited(15) == [] # No books to return
store.save("notes", "a", 10)
store.save("plan", "a", 30)
store.save("todo", "a", 20)
assert store.recently_edited(15) == ["plan", "todo"]
assert store.recently_edited(100) == [] # Nothing after spec time



print(f'all tests pass')