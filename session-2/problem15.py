'''
Session 2, Problem 15: Polls (progressive). Level 1

This problem has 3 levels. Each adds to the same class, and earlier levels must keep working.

Time limit: 25 minutes, including writing your own tests. Aim for working code by about minute 20. Hard stop at 37 minutes. Start by writing __init__ with an example comment on each structure, and run one example call through it.

Write a class that runs polls and counts votes.

Class name: PollService

Creating a PollService() takes no arguments, and a new service starts with no polls.

Methods:

create_poll(poll_id, options): poll_id is a string, options is a list of distinct strings. Creates a poll with those options, each starting at 0 votes. Returns True if the poll was created, or False if a poll with that id already exists (the existing poll is left unchanged).
vote(user, poll_id, option): user, poll_id, and option are strings. Records one vote from the user for that option. Returns True if the vote was counted. Returns False, with nothing changed, if the poll doesn't exist, if option isn't one of the poll's options, or if the user has already voted in that poll.
vote_count(poll_id, option): poll_id and option are strings. Returns the number of votes for that option, as an int. Returns None if the poll doesn't exist or option isn't one of its options.
'''

from select import poll
from weakref import finalize


class PollService:
    
    def __init__(self):
        self.records_poll: dict[str, dict] = {} # k=poll_id (str), v= dict w/ k= option(str) v=votes (int)
        self.records_voters: dict[str, dict] = {} # k = user (str) v=dict w/ k=poll_id (str) and v=option selected (str)

    '''1. create_poll(poll_id, options): poll_id is a string, options is a list of distinct strings. 
    Creates a poll with those options, each starting at 0 votes. 
    Returns True if the poll was created, or False if a poll with that id already exists (the existing poll is left unchanged).''' 
    def create_poll(self, poll_id: str, options: list):  # Pull existing poll data
        poll_data = self.records_poll.get(poll_id, None)
        new_dict = {}
        # If poll exists, return False
        if poll_data is not None:
            return False
        # Loop through options and populate poll's dict (option:votes)
        for option in options:
            new_dict[option] = 0
        self.records_poll[poll_id] =  new_dict
        return True
    
    '''2. vote(user, poll_id, option): user, poll_id, and option are strings. 
    Records one vote from the user for that option. 
    Returns True if the vote was counted. 
    Returns False, with nothing changed, if the poll doesn't exist, if option isn't one of the poll's options, or if the user has already voted in that poll.''' 
    def vote(self, user: str, poll_id: str, option: str):
        # Pull poll and user data
        poll_data = self.records_poll.get(poll_id, None)
        user_data = self.records_voters.get(user, None)
        print(f'poll_data: {poll_data}, user_data: {user_data}')
        
        # If (a) poll doesn't exist, (b) option isn't in poll, or (c) the user has voted in this poll, return False
        if poll_data is None or option not in poll_data or (user_data is not None and poll_id in user_data):
            return False
        # Increment the votes. Note that each aleady starts at 0, as set in create_poll
        self.records_poll[poll_id][option] += 1
        # Update the this user's voting record.
        if user_data is None:
            # If the user doesn't already have votes, need to establish inner dict first
            self.records_voters[user] = {}  
        self.records_voters[user][poll_id] = option
        print(f'self.records_poll.items(): {self.records_poll.items()}, self.records_voters.items(): {self.records_voters.items()}')
        
        return True
    
    '''3. vote_count(poll_id, option): poll_id and option are strings. 
    Returns the number of votes for that option, as an int. 
    Returns None if the poll doesn't exist or option isn't one of its options.'''
    def vote_count(self, poll_id: str, option: str):
        poll_data = self.records_poll.get(poll_id, None)
        if poll_data is not None and option in poll_data:
            return poll_data[option]
        return None

# Complexity: 
# o = num options
# p = num polls
# v = num votes
# 1. create_poll: O(o)
# 2. vote: O(1)
# 3. vote_count: O(1)

# Worst case complexity: O(o)
# Memory: O(p + o + v) --> since each num poll <= num_options --> O(o + v)
    
#Example tests:

polls = PollService()
assert polls.create_poll("lunch", ["pizza", "sushi"]) is True
assert polls.create_poll("lunch", ["pizza", "sushi"]) is False # Can't re-create poll
assert polls.vote("ann", "lunch", "pizza") is True
assert polls.vote("ann", "lunch", "sushi") is False # Can't vote twice in same poll
assert polls.vote("ann", "breakfast", "sushi") is False # Can't vote in poll that doesn't exist
assert polls.vote("ann", "lunch", "burgers") is False # Can't vote for option that doesn't exist

polls = PollService()
polls.create_poll("lunch", ["pizza", "sushi"])
assert polls.vote_count("lunch", "sushi") == 0
assert polls.vote("ann", "lunch", "pizza") is True
assert polls.vote_count("lunch", "pizza") == 1 # Increments
assert polls.vote_count("breakfast", "pizza") is None # poll doesn't exist
assert polls.vote_count("lunch", "soup") is None # option doesn't exist

print('tests pass')