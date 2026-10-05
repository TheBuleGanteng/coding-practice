'''
Session 2, Problem 12: Social follows (progressive). Level 1

This problem has 3 levels. Each adds to the same class, and earlier levels must keep working.

Time limit: 25 minutes, including writing your own tests. Aim for working code by about minute 20. Hard stop at 37 minutes. Start with the design block.

Write a class that tracks which users follow which other users.

Class name: SocialNetwork

Creating a SocialNetwork() takes no arguments, and a new network starts with no users.

Methods:

add_user(user): user is a string. Adds the user to the network. Returns True if the user was added, or False if that user already exists.
follow(follower, followee): follower and followee are strings. Makes follower follow followee. Returns True if the follow was created. Returns False, with nothing changed, if either user doesn't exist, if follower and followee are the same user, or if follower already follows followee.
unfollow(follower, followee): follower and followee are strings. Removes the follow. Returns True if follower was following followee and the follow has been removed, or False otherwise.
--------------------------------------------------------------------------
Session 2, Problem 12: Social follows. Level 2

Time limit: 25 minutes, including writing your own tests. Aim for working code by about minute 20. Hard stop at 37 minutes. Start with the design block.

Add two methods to your SocialNetwork class. Everything from Level 1 must keep working.

New methods:

following(user): user is a string. Returns a list of all users that user currently follows, sorted alphabetically. Returns an empty list if the user doesn't exist or follows no one.
mutuals(user): user is a string. Returns a list of all users who both follow user and are followed by user, sorted alphabetically. Returns an empty list if the user doesn't exist or has no mutuals.
--------------------------------------------------------------------------

'''

class SocialNetwork:
    
    def __init__(self):
        self.records_users: set = set()
        self.records_following: dict[str, set] = {} #k=followee v=followers
        
        
    '''1.add_user(user): user is a string. 
    Adds the user to the network. 
    Returns True if the user was added, or False if that user already exists.''' 
    def add_user(self, user: str):
        if user in self.records_users:
            return False
        self.records_users.add(user)
        self.records_following[user] = set()
        return True
    
    '''2. follow(follower, followee): follower and followee are strings. 
    Makes follower follow followee. 
    Returns True if the follow was created. 
    Returns False, with nothing changed, if either user doesn't exist, if follower and followee are the same user, or if follower already follows followee.'''
    def follow(self, follower: str, followee: str):
        # Returns False, with nothing changed, if either user doesn't exist, if follower and followee are the same user
        if follower not in self.records_users or followee not in self.records_users or follower == followee:
            return False
        # pull follow data
        follow_data = self.records_following.get(followee, None)
        
        # if the followee already has follower in their set of followers, return False
        if follow_data is not None and follower in follow_data:
            return False
        self.records_following[followee].add(follower)
        return True
    
    '''3. unfollow(follower, followee): follower and followee are strings. 
    Removes the follow. 
    Returns True if follower was following followee and the follow has been removed, or False otherwise.'''
    def unfollow(self, follower: str, followee: str):
        # pull follow data
        follow_data = self.records_following.get(followee, None)
        # Check if follower is following followee
        if follow_data is not None and follower in follow_data:
            self.records_following[followee].remove(follower)
            return True
        return False
               
    '''4. following(user): user is a string. 
    Returns a list of all users that user currently follows, sorted alphabetically. 
    Returns an empty list if the user doesn't exist or follows no one.'''
    def following(self, user: str):
        # list into which we will put the ppl user follows
        following_list = []
        # loop through all the following records
        for followee, followers in self.records_following.items():
            # For a given followeee, if the user is in the followers, append the followee to that user's list
            if user in followers:
                following_list.append(followee)
        # sort list and return
        return sorted(following_list)
        
    
    '''5. mutuals(user): user is a string. 
    Returns a list of all users who both (a) follow user and (b) are followed by user, sorted alphabetically. 
    Returns an empty list if the user doesn't exist or has no mutuals.'''
    def mutuals(self, user: str):
        # throw empty list if user doesn't exist
        if user not in self.records_users:
            return []        
        # get set of users this person follows
        following_set = set(self.following(user))
        # get set of users who follow this person
        follower_set = self.records_following[user]
        # list for results
        mutuals_list = []
        # loop over list of ppl who follow this user
        for follower in follower_set:
            # Check if each of them in this list of ppl this user follows 
            if follower in following_set:
                mutuals_list.append(follower)
        return sorted(mutuals_list)
        
        

# Complexity:
# 1. add_user = O(1)
# 2. follow = O(1)
# 3. unfollow = O(1)
# 4. following --> loop over followees for every user which is n bc all users have a record, so O(n) + sort the number ppl the user follows (a) O(a log a) --> O(n + a log a)
# 5. mutuals --> call to self.following O(n + a log a) + loops over set O(n) n=users, checks sets O(1), sort O(m log m) m=mutuals --> O(n + a log a + n + m log m) --> O(2n + a log a + m log m) --> O(n + a log a + m log m) --> mutuals (m) <= ppl user follows (a) --> O(n + a log a)


# Worst case: O(n + a log a)
# Memory: O(n + f) w/ n=users, f=number

# Tests
network = SocialNetwork()
network.add_user("ann")
network.add_user("bob")
assert network.add_user("ann") is False # user already registered
assert network.follow("ann", "bob") is True
assert network.follow("ann", "bob") is False
assert network.follow("ann", "bill") is False # follower doesn't exist
assert network.follow("bill", "bob") is False # followee doesn't exist
assert network.unfollow("ann", "bob") is True # legit unfollow
assert network.unfollow("ann", "bob") is False # no longer following one another

network = SocialNetwork()
network.add_user("ann")
assert network.unfollow("ann", "bob") is False
assert network.unfollow("ann", "bob") is False

network = SocialNetwork()
network.add_user("ann")
network.add_user("bob")
network.add_user("cat")
network.follow("ann", "bob")
network.follow("ann", "cat")
assert network.following("ann") == ["bob", "cat"]
assert network.following("bob") == [] # no followers
assert network.following("joe") == [] # not a user



network = SocialNetwork()
network.add_user("ann")
network.add_user("bob")
network.add_user("cat")
network.follow("ann", "bob")
network.follow("bob", "ann")
network.follow("ann", "cat")
assert network.mutuals("ann") == ["bob"]
assert network.mutuals("cat") == [] # no mutuals for user
assert network.mutuals("frank") == [] # no mutuals for user


print('tests pass')