'''
Drill A — Unique visitors per page.
You're given a list of strings, each "user_id,page,timestamp", e.g. "u42,/home,2026-09-24T10:00:00". 
Write unique_visitors(events) returning a dict mapping each page to the number of distinct users who visited it. 
(Wrinkle: it's distinct users — if u42 hits /home five times, that's 1, not 5. Think about what data structure counts distinct things.)
'''

def unique_visitors(logs):
    page_visitors = {} # declare the dict to be populated
    
    for log in logs: # iterate through each string
        substrings = log.split(",") # parse based on commas
        if len(substrings) != 3: # skip if doesn't have the usual 3 parts
            continue
        
        page, user = substrings[1], substrings[0] # take the important bits
        
        if page not in page_visitors: # if this page is new (e.g. not already in the dict)
            page_visitors[page] = set() # Start an empty set for this page wherein key = page name and value = set containing unique usernames. Sets only store unique values, so dedup is built-in.
            
        page_visitors[page].add(user) # Add this user to the current page's (the key) set (the value)
        
    results = {}
    for page in page_visitors:
        results[page] = len(page_visitors[page]) # This accesses the value (e.g. the set) associated with the current page. Result is {<page name>: <# visitors>}
        
    return results # return the populated results dict
        
    # Question: What is time complexity in terms of n (number of lines)?
    # Answer: The time complexity to run would be n (e.g the loop runs once for each line in the list). No additional time bc no sort.