'''
Session 2, Problem 4: Election

Time limit: 25 minutes, including writing your own tests. Aim for working code by about minute 20. Hard stop at 37 minutes.

Write a class that counts votes in an election.

Class name: Election

Creating an Election() takes no arguments, and a new election starts with no candidates.

Methods:

1. add_candidate(name): name is a string. Adds a candidate with 0 votes. 
Returns True if the candidate was added, or False if a candidate with that name already exists (their votes are left unchanged).
2. vote(name): name is a string. Adds one vote for that candidate and returns their new vote count as an int. 
Returns None if there is no candidate with that name.
3. votes(name): name is a string. 
Returns the candidate's current vote count as an int, or None if there is no candidate with that name.
4. winner(): no arguments. 
Returns the name of the candidate with the most votes. If candidates tie for the most votes, returns the name that comes first alphabetically. 
Returns None if no candidate has received any votes.
'''

'''
Classes
Election --> No arguments --> Dict with y=name (str), v=votes (int)

'''

class Election:
    
    def __init__(self):
        self.records: dict[str, int] = {}
        
    def add_candidate(self, name):
        candidate_data = self.records.get(name, None)
        if candidate_data is None:
            self.records[name] = 0
            return True
        return False
    
    def vote(self, name):
        candidate_data = self.records.get(name, None)
        if candidate_data is None:
            return None
        self.records[name] += 1
        return self.records[name]
    
    def votes(self, name):
        return self.records.get(name, None)
        
    def winner(self):
        if len(self.records.items()) == 0: # No candidates? Return None
            return None
        top_cand = min(self.records.items(), key=lambda kv:(-kv[1], kv[0]))
        if top_cand[1] == 0: # Candidates, but no votes? Return None
            return None
        return top_cand[0]

# Efficiency:
# add_candidate: O(1)
# vote: O(1)
# votes: O(1)
# winner: min --> O(m)
# Worst case: O(m) w/ m = candidates
# Memory: O(m) 

# Example tests:
election = Election()

# add_candidate
assert election.add_candidate("ann") is True
assert election.add_candidate("ann") is False
assert election.votes("ann") == 0

# vote
assert election.vote("ann") == 1
assert election.vote("ann") == 2
assert election.vote("bob") is None

# votes
assert election.votes("ann") == 2
assert election.votes("bob") is None

# Winner
assert election.winner() == "ann"
assert election.add_candidate("bob") is True
assert election.vote("bob") == 1
assert election.vote("bob") == 2
assert election.winner() == "ann"
election2 = Election()
assert election2.winner() is None

election3 = Election()
assert election3.add_candidate("ann") is True
assert election3.add_candidate("bob") is True
assert election3.winner() is None
print('all tests pass')
