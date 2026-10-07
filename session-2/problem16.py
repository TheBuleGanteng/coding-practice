'''
ession 2, Problem 16: Tagging system (progressive). Level 1

This problem has 3 levels. Each adds to the same class, and earlier levels must keep working.

Time limit: 25 minutes, including writing your own tests. Aim for working code by about minute 20. Hard stop at 37 minutes. Before coding: write __init__ with an example comment on each structure, run one example call through it, and skim the five syntax lines in your notes.

Write a class that attaches tags to items.

Class name: TagStore

Creating a TagStore() takes no arguments, and a new store starts with no items.

Methods:

add_item(item): item is a string. Adds the item with no tags. Returns True if the item was added, or False if that item already exists.
tag(item, tag): item and tag are strings. Attaches the tag to the item. Returns True if the tag was attached. Returns False, with nothing changed, if the item doesn't exist or already has that tag.
untag(item, tag): item and tag are strings. Removes the tag from the item. Returns True if the item had that tag and it has been removed, or False otherwise.
---------------------------------------------------------
Session 2, Problem 16: Tagging system. Level 2

Time limit: 25 minutes, including writing your own tests. Aim for working code by about minute 20. Hard stop at 37 minutes. Start with your one-line variable list and one example call through your structure.

Add two methods to your TagStore class. Everything from Level 1 must keep working.

New methods:

items_with_tag(tag): tag is a string. Returns a list of all items that currently have that tag, sorted alphabetically. Returns an empty list if no item has it.
top_tags(n): n is a non-negative int. Returns a list of the n tags attached to the most items, each as a string in the format "tag(count)", where count is the number of items that currently have that tag. The list is sorted by count, largest first; tags with equal counts are sorted alphabetically. Only tags currently attached to at least one item are included. If there are fewer than n such tags, returns all of them.


'''
class TagStore():
    
    def __init__(self):
        self.records: dict[str, set] = {}
        
        
    '''1. add_item(item): item is a string. Adds the item with no tags. 
    Returns True if the item was added, or False if that item already exists.''' 
    def add_item(self, item: str):
        # If item already exists, return False
        if self.records.get(item, None) is not None:
            return False
        # Add item w/o any tags (empty set)
        self.records[item] = set()
        # Ret True
        return True

    '''2. tag(item, tag): item and tag are strings. Attaches the tag to the item. 
    Returns True if the tag was attached. 
    Returns False, with nothing changed, if the item doesn't exist or already has that tag.'''
    def tag(self, item: str, tag: str):
        tags = self.records.get(item, None)
        # if item doesn't exist or has tag, return False
        if tags is None or tag in tags:
            return False
        # Apply tag to item and return True
        self.records[item].add(tag)
        return True
    
    '''3. untag(item, tag): item and tag are strings. Removes the tag from the item. 
    Returns True if the item had that tag and it has been removed, or False otherwise.'''
    def untag(self, item: str, tag: str):
        tags = self.records.get(item, None)
        # if item exists and previously had the tag, remove it and return True
        if tags is not None and tag in tags:
            self.records[item].remove(tag)
            return True
        # Else, return False
        return False
    
    '''4. items_with_tag(tag): tag is a string. 
    Returns a list of all items that currently have that tag, sorted alphabetically. 
    Returns an empty list if no item has it.'''
    def items_with_tag(self, tag: str):
        return sorted([(item) for item, tags in self.records.items() if tag in tags])
    
    '''5. top_tags(n): n is a non-negative int. 
    Returns a list of the n tags attached to the most items, each as a string in the format "tag(count)", 
    where count is the number of items that currently have that tag. 
    The list is sorted by count, largest first; tags with equal counts are sorted alphabetically. 
    Only tags currently attached to at least one item are included. 
    If there are fewer than n such tags, returns all of them.'''
    def top_tags(self, n: int):
        solution_dict = {}# k=tag, v = count
        # Loop over all the records
        print(f'self.records.items(): {self.records.items()}')
        for item, tag_set in self.records.items():
            # For a given item, check the tag set
            for tag in tag_set:
                print(f'item: {item}, tag is: {tag}, tag_set is: {tag_set}')
                # If that tag is not in soluton (never seen yet), initialize and set to 1
                if tag not in solution_dict:
                    solution_dict[tag] = 1
                # If tag already in solution, increment count by 1
                else:
                    solution_dict[tag] += 1
        solution_sorted = sorted(solution_dict.items(), key=lambda kv:(-kv[1], kv[0]))[:n]
        print(f'solution_sorted: {solution_sorted}')
        solution_list = []
        for solution in solution_sorted:
            solution_list.append(f'{solution[0]}({solution[1]})') 
        print(f'solution_sorted: {solution_sorted}')
        return solution_list
# Complexity:
# r = # records
# t = # abs num of tags (can repreat same tag on diff items)
# i = items
# d = # distinct tags (not counting reuse)
# k = items with a tag
# 1. add_item --> O(1)
# 2. tag --> O(1)
# 3. untag --> O(1)
# 4. items_with_tag --> loop over records O(r) + sort the items with a tag (k log k)
# 5. top_tags --> loop over all tags O(t) + sort all distinct tags O(d log d)

# Worst case complexity: O(r + k log k) <-- dominates if lots of items have tags OR O(t + d log d) <-- dominates if items ahve many tags
# Memory: O(r + t)

# Example tests:

store = TagStore()
assert store.add_item("photo1") is True
assert store.add_item("photo1") is False # can't re-add same item
assert store.tag("photo1", "beach") is True
assert store.tag("photo1", "beach") is False
assert store.tag("photo2", "beach") is False # Item doesn't exist

store = TagStore()
assert store.untag("photo1", "beach") is False # Item doesn't exist
assert store.add_item("photo1") is True
assert store.untag("photo1", "beach") is False # Item isn't tagged
assert store.tag("photo1", "beach") is True
assert store.untag("photo1", "beach") is True # Valid untag


store = TagStore()
store.add_item("photo1")
store.add_item("photo2")
store.tag("photo2", "beach")
store.tag("photo1", "beach")
assert store.items_with_tag("beach") == ["photo1", "photo2"]


store = TagStore()
store.add_item("photo1")
store.add_item("photo2")
store.tag("photo1", "beach")
store.tag("photo2", "beach")
store.tag("photo1", "sunset")
assert store.top_tags(2) == ["beach(2)", "sunset(1)"]


print('tests pass')