'''
Session 3, Problem 3: Recent searches (progressive). Level 1

Time limit: 25 minutes, including writing your own tests. Before coding, read all three methods, note what data each one needs, then write __init__ with an example comment and run one example call through it. Aim for working code by about minute 20. Hard stop at 37 minutes.

Write a class that keeps, for each user, a limited history of their most recent searches.

Class name: SearchHistory

Creating a SearchHistory(limit) takes one argument: limit, a positive int, the most searches kept for any one user. It starts with no users.

Methods:

search(user, query): user and query are strings. Records that the user searched for the query, making it their most recent search. If this makes the user’s history hold more than limit queries, removes their oldest query. Returns the removed query, or None if nothing was removed.
times_searched(user, query): user and query are strings. Returns how many times the user has searched for the query while it has been in their history, as an int. If a query is removed and later searched again, its count starts over from 1. Returns 0 if the query isn’t in the user’s history.
last_search(user): user is a string. Returns the user’s most recent query, or None if they have no history.

Session 3, Problem 3: Recent searches. Level 2

Time limit: 25 minutes, including writing your own tests. Before coding, read both methods, note what data each needs, and run one example call through your structure. Aim for working code by about minute 20. Hard stop at 37 minutes.

Add two methods to your SearchHistory class. Everything from Level 1 must keep working.

New methods:

recent(user, n): user is a string, n is a non-negative int. Returns a list of the user’s n most recent queries, most recent first. If the user has fewer than n queries in their history, returns all of them. Returns an empty list if the user has no history.
popular(n): n is a non-negative int. Adds up, for each query, its times-searched counts across every user’s history. Returns a list of the n queries with the highest totals, each as a string in the format "query(total)". The list is sorted by total, largest first; queries with equal totals are sorted alphabetically. If fewer than n queries exist, returns all of them.


Session 3, Problem 3: Recent searches. Level 3

Time limit: 35 minutes, including writing your own tests. Aim for working code by about minute 28. Hard stop at 52 minutes. Before coding: read all three methods and the changes section, note what data each needs, and check which existing methods have to change.

Add times to searches. Everything from Levels 1 and 2 must keep working.

Every new method takes a timestamp, a non-negative int. Timestamps in successive calls never decrease.

New methods:

search_at(user, query, timestamp): same as search (including the view count, the removal of the oldest query when over the limit, and the return value), and also records timestamp as the time of this query’s latest search.
searched_since(user, since): user is a string, since is a non-negative int. Returns a list of the user’s queries whose latest search time is at or after since, most recently used first. Returns an empty list if there are none.
expire(timestamp, max_age): max_age is a positive int. For every user, removes each query whose latest search time is earlier than timestamp - max_age. Returns the total number of queries removed, as an int.

Changes to existing behavior:

A query recorded with plain search has no time: it never expires and is never included in searched_since. A plain search on a query that had a time removes that time.
Whenever a query leaves a user’s history, for any reason, its time is discarded too.
'''
import keyword


class SearchHistory:
    
    def __init__(self, limit: int):
        self.limit = limit
        self.records: dict[str, dict[str, int]] = {} # k=user, k=query,v=count(int)
        self.timestamps: dict[str, dict[str, int]] = {} #k=user, k=query, v=timestamp(int)

    '''1. search(user, query): user and query are strings. 
    Records that the user searched for the query, making it their most recent search. 
    If this makes the user’s history hold more than limit queries, removes their oldest query. 
    Returns the removed query, or None if nothing was removed.'''
    def search(self, user:str, query:str):
        user_data = self.records.get(user, None)
        timestamp_data = self.timestamps.get(user, {}).get(query, None)
        # Per stage 3: simple search removes any existing timestamp for this query
        if timestamp_data is not None:
            self.timestamps[user].pop(query)
        if user_data is not None:
            # If query already in queue, pop it
            value_removed = self.records[user].pop(query, 0)
            # Re-add the item, with an updated view count
            self.records[user][query] = value_removed+1        
        else:
            # If no user_data, set up dict
            self.records[user] = {query:1}
        records = len(self.records[user])
        # Check if over the limit
        if records > self.limit:
            # if over the limit, remove the first item, returning that query (the key)
            oldest_query = next(iter(self.records[user]))
            self.records[user].pop(oldest_query, None)
            return oldest_query 
        return None
    
    '''2. times_searched(user, query): user and query are strings. 
    Returns how many times the user has searched for the query while it has been in their history, as an int. 
    If a query is removed and later searched again, its count starts over from 1. 
    Returns 0 if the query isn’t in the user’s history.'''
    def times_searched(self, user: str, query: str):
        return self.records.get(user, {}).get(query, 0)
    
    
    '''3. last_search(user): user is a string. 
    Returns the user’s most recent query, or None if they have no history.'''
    def last_search(self, user:str):
        user_history = self.records.get(user, None)
        print(f'user_history: {user_history}')
        if user_history is not None:
            return next(reversed(user_history))
        return None
    
    
    '''4. recent(user, n): user is a string, n is a non-negative int. 
    Returns a list of the user’s n most recent queries, most recent first. 
    If the user has fewer than n queries in their history, returns all of them. 
    Returns an empty list if the user has no history.'''
    def recent(self, user: str, n: int):
        user_data = self.records.get(user, None)
        items = []
        print(f'user:data: {user_data}')
        if user_data is not None:
            for query, count in reversed(user_data.items()):
                items.append(query)
        print(f'items: {items}')
        return items[:n]


    '''5. popular(n): n is a non-negative int. Adds up, for each query, its times-searched counts across every user’s history. 
    Returns a list of the n queries with the highest totals, each as a string in the format "query(total)". 
    The list is sorted by total, largest first; queries with equal totals are sorted alphabetically. 
    If fewer than n queries exist, returns all of them.'''
    def popular(self, n:int):
        solution_dict = {}
        for user, data in self.records.items():
            for query, count in data.items():
                if solution_dict.get(query, None) is None:
                    solution_dict[query] = count
                else:
                    solution_dict[query] += count
        print(f'solution_dict: {solution_dict}')  
        return [f'{query}({total})' for query, total in sorted(solution_dict.items(), key=lambda kv:(-kv[1], kv[0]))][:n]
    
    
    '''6. search_at(user, query, timestamp): same as search 
    (including the view count, the removal of the oldest query when over the limit, and the return value), 
    and also records timestamp as the time of this query’s latest search.'''
    def search_at(self, user:str, query:str, timestamp:int):
        # Use old search
        search_result = self.search(user=user, query=query)
        # Add timestamp
        timestamp_data = self.timestamps.get(user, None)
        if timestamp_data is None:
            self.timestamps[user] = {query:timestamp}
        else:
            self.timestamps[user][query] = timestamp
        return search_result


    '''7. searched_since(user, since): user is a string, since is a non-negative int. 
    Returns a list of the user’s queries whose latest search time is at or after since, most recently used first. 
    Returns an empty list if there are none.'''
    def searched_since(self, user:str, since: int):
        user_data = self.records.get(user, None)
        timestamp_data = self.timestamps.get(user, None)
        print(f'user_data: {user_data}, timestamp_data: {timestamp_data}')
        solution = []
        queries_windowed = []
        if timestamp_data is not None and len(timestamp_data) > 0:
            queries_windowed = [queries for queries, timestamps in timestamp_data.items() if timestamps >= since]
            print(f'queries_windowed: {queries_windowed}')
        if user_data is not None:
            solution = [queries for queries, counts in user_data.items() if (queries in queries_windowed)]
            print(f'solution: {solution}')
            return solution
        return solution
    
    '''8. expire(timestamp, max_age): max_age is a positive int. 
    For every user, removes each query whose latest search time is earlier than timestamp - max_age. 
    Returns the total number of queries removed, as an int.'''
    def expire(self, timestamp: int, max_age: int):
        # Assumption: Only deal with items that have a timestamp.
        n = 0
        to_delete = {}
        # Cyclce across users
        for user, data in self.timestamps.items():
            for user_query, user_timestamp in data.items():
                if user_timestamp <= timestamp-max_age:
                    to_delete[user] = user_query
                    n += 1
        for user, query in to_delete.items():
            self.timestamps[user].pop(query)
            self.records[user].pop(query)
        return n
        

# Complexity:
# u = total users
# q = total queries across all users
# i = queries for a given user
# e = queries for a given user that have expiration
# a = total queries across all users that have an expiration
# x = total expired items
# 1. search --> O(1)
# 2. times_searched --> O(1)
# 3. last_searched --> O(1)
# 4. recent --> Loops over queries for a given user O(i)
# 5. popular --> loops over all users O(u) + loops over queries for each user O(q) --> O(u+q) + sorts queries O(q log q)
# 6. search_at --> uses old search --> O(1)
# 7. searched_since --> loops over user's records O(i) + loops over user's expiry records O(e) --> O(i + e)
# 8. expire --> loop over ALL users' timestamped items O(a) + loop over expired items O(x) --> O(a + x)


# Worst-case complexity: O(u+q + q log q) --> O(u + q lot q) 
# Memory: O(u+q+a)


# Example tests:


history = SearchHistory(2)
history.search("ann", "python")
history.search("ann", "rust")
assert history.last_search("ann") == "rust" # Normal functionality
history.search("ann", "python")
assert history.last_search("ann") == "python"
assert history.times_searched("ann", "python") == 2
assert history.times_searched("ann", "dogs") == 0 # term not in search history
assert history.last_search("bob") is None # No history

history = SearchHistory(2)
history.search("ann", "python")
history.search("ann", "rust")
assert history.search("ann", "go") == "python"

history = SearchHistory(200)
history.search("ann", "python")
history.search("ann", "rust")
assert history.search("ann", "go") is None # nothing removed bc not over limit


history = SearchHistory(3)
history.search("ann", "python")
history.search("ann", "rust")
history.search("ann", "go")
assert history.recent("ann", 2) == ["go", "rust"]
assert history.recent("ann", 3) == ["go", "rust", "python"] # limit at # items
assert history.recent("ann", 300) == ["go", "rust", "python"] # limit beyond # items

history = SearchHistory(3)
history.search("ann", "python")
history.search("ann", "python")
history.search("bob", "python")
history.search("bob", "rust")

assert history.popular(2) == ["python(3)", "rust(1)"]
assert history.popular(3) == ["python(3)", "rust(1)"] # limit at # items
assert history.popular(300) == ["python(3)", "rust(1)"] # limit beyond # items
assert history.popular(0) == [] # empty list
history.search("bob", "apples")
assert history.popular(2) == ["python(3)", "apples(1)"] # apples beats rust in tie (alpha as second sort)

history = SearchHistory(3)
assert history.popular(2) == [] # no search items


history = SearchHistory(5)
history.search_at("ann", "python", 10)
history.search_at("ann", "rust", 20)
assert history.searched_since("ann", 15) == ["rust"]
history.search("ann", "rust")
assert history.searched_since("ann", 15) == [] # Item with plain search is not included 

history = SearchHistory(5)
history.search_at("ann", "python", 10)
history.search("ann", "go")
history.search_at("ann", "rust", 50)
assert history.expire(60, 30) == 1

print('all tests pass')