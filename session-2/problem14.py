'''
Session 2, Problem 14: Chat rooms (progressive). Level 1

This problem has 3 levels. Each adds to the same class, and earlier levels must keep working.

Time limit: 25 minutes, including writing your own tests. Aim for working code by about minute 20. Hard stop at 37 minutes. Start by writing __init__ with an example comment on each structure, and run one example call through it.

Write a class that manages chat rooms and their members.

Class name: ChatServer

Creating a ChatServer() takes no arguments, and a new server starts with no rooms.

Methods:

create_room(room): room is a string. Creates an empty room. Returns True if the room was created, or False if a room with that name already exists (the existing room is left unchanged).
join(user, room): user and room are strings. Adds the user to the room. Returns True if the user joined. Returns False, with nothing changed, if the room doesn't exist or the user is already in it.
delete_room(room): room is a string. Deletes the room, removing all its members from it, and returns the number of members it had, as an int. Returns None if the room doesn't exist.
---------------------------------------------------------
Session 2, Problem 14: Chat rooms. Level 2

Time limit: 25 minutes, including writing your own tests. Aim for working code by about minute 20. Hard stop at 37 minutes. Start with your one-line variable list and one example call through your structure.

Add two methods to your ChatServer class. Everything from Level 1 must keep working.

New methods:

leave(user, room): user and room are strings. Removes the user from the room. Returns True if the user was in the room and has left, or False otherwise, including when the room doesn't exist.
shared_rooms(user_a, user_b): user_a and user_b are strings. Returns a list of the names of all rooms that both users are currently in, sorted alphabetically. Returns an empty list if they share no rooms.
-----------------------------------------------------
Session 2, Problem 14: Chat rooms. Level 3

Time limit: 35 minutes, including writing your own tests. Aim for working code by about minute 28. Hard stop at 52 minutes. Start with your structures (with examples) and one example call, and check: which existing methods need to change?

Add timed mutes and message sending. Everything from Levels 1 and 2 must keep working.

Every new method takes a timestamp, a non-negative int. Timestamps in successive calls never decrease.

New methods:

mute(user, room, timestamp, duration): user and room are strings, duration is a positive int. Mutes the user in that room from timestamp up to, but not including, timestamp + duration. A new mute for the same user in the same room replaces the old one. Returns True if the user is in the room, or False, with nothing changed, otherwise (including when the room doesn't exist).
is_muted(user, room, timestamp): user and room are strings. Returns True if the user is muted in that room at timestamp, or False otherwise.
send_at(user, room, timestamp): user and room are strings. The user sends one message to the room. Returns the total number of messages sent to that room so far, as an int, including this one. Returns None, with nothing counted, if the room doesn't exist, if the user isn't in it, or if the user is muted in it at timestamp.

One change to existing behavior: when a user leaves a room, or the room is deleted, any mute on that user in that room is removed. 
A deleted room's message count is also gone, so if the room is created again, its count starts from 0.


'''

class ChatServer:
    
    def __init__(self):
        self.records: dict[str, set] = {} # k=room(str) v= set(users (strs))
        self.records_messages: dict[str, int] = {} # k=room(str), v=msg count (int)
        self.records_mutes: dict[str, dict] = {} # k=user(str), v=dict(room:expiry)
        
        
    '''1. create_room(room): room is a string. 
    Creates an empty room. 
    Returns True if the room was created, or False if a room with that name already exists (the existing room is left unchanged).'''
    def create_room(self, room: str):
        # participatnt data
        part = self.records.get(room, None)
        # if room doesn't exist, ret False
        if part is not None:
            return False
        # Create room and return True
        self.records[room] = set()
        # Adds empty set for messages
        self.records_messages[room] = 0
        return True
    
    '''2. join(user, room): user and room are strings. 
    Adds the user to the room. 
    Returns True if the user joined. 
    Returns False, with nothing changed, if the room doesn't exist or the user is already in it.'''
    def join(self, user: str, room: str):
        # participatnt data
        part = self.records.get(room, None)
        if part is None or user in part:
            return False
        self.records[room].add(user)
        return True
    
    '''3. delete_room(room): room is a string. 
    Deletes the room, removing all its members from it, and returns the number of members it had, as an int. 
    Returns None if the room doesn't exist.'''
    def delete_room(self, room: str):
        part = self.records.get(room, None)
        # Return None if room doesn't exist
        if part is None:
            return None
        # IF room exists, delete room, and return no. participants
        del(self.records[room])
        # Remove msg count (part 3)
        del(self.records_messages[room])
        # Loop over the lines in records_mutes to check if a given user has a mute for this room.
        for user, record in self.records_mutes.items():
            # If the user has a mute for this room, remove it via pop
            self.records_mutes.get(user, {}).pop(room, None)
        return len(part)
    
    '''4. leave(user, room): user and room are strings. 
    Removes the user from the room. 
    Returns True if the user was in the room and has left, or False otherwise, including when the room doesn't exist.'''
    def leave(self, user: str, room: str):
        part = self.records.get(room, None) 
        # If room exists, and user is in it, remove and ret True
        if part is not None and user in part:
            self.records[room].remove(user)
            # Check if the user has a mute for this room
            user_mutes = self.records_mutes.get(user, None)
            if user_mutes is not None:
                self.records_mutes[user].pop(room, None)
            return True
        # Else ret false
        return False
    
    '''5. shared_rooms(user_a, user_b): user_a and user_b are strings. 
    Returns a list of the names of all rooms that both users are currently in, sorted alphabetically. 
    Returns an empty list if they share no rooms.'''
    def shared_rooms(self, user_a: str, user_b: str):
        solution = sorted([rooms for rooms, users in self.records.items() if (user_a in users and user_b in users)])
        print(f'solution: {solution}')
        return solution
    
    '''6. mute(user, room, timestamp, duration): user and room are strings, duration is a positive int. 
    Mutes the user in that room from timestamp up to, but not including, timestamp + duration. 
    A new mute for the same user in the same room replaces the old one. 
    Returns True if the user is in the room, or False, with nothing changed, otherwise (including when the room doesn't exist).'''
    def mute(self, user: str, room: str, timestamp: int, duration: int):
        par = self.records.get(room, None)
        mutes = self.records_mutes.get(user, {})
        if par is not None and user in par:
            # Mute user up to, but not including timestamp + duration (hence -1)
            mutes[room] = timestamp + duration - 1
            self.records_mutes[user] = mutes
            print(f'self.records_mutes[user]: {self.records_mutes[user]}')
            return True
        return False
    
    '''7. is_muted(user, room, timestamp): user and room are strings. 
    Returns True if the user is muted in that room at timestamp, or False otherwise.'''
    def is_muted(self, user: str, room: str, timestamp: int):
        par = self.records.get(room, None)
        mutes = self.records_mutes.get(user, None)
        print(f'mutes: {mutes}')
        if mutes is not None:
            for mutes_room, mutes_expiry in mutes.items():
                if room == mutes_room and mutes_expiry >= timestamp:
                    return True
        return False
    
    '''8. send_at(user, room, timestamp): user and room are strings. 
    The user sends one message to the room. Returns the total number of messages sent to that room so far, as an int, including this one. 
    Returns None, with nothing counted, if the room doesn't exist, if the user isn't in it, or if the user is muted in it at timestamp.'''
    def send_at(self, user: str, room: str, timestamp: int):
        par = self.records.get(room, None)
        msgs = self.records_messages.get(room, None)
        if self.is_muted(user=user, room=room, timestamp=timestamp) or par is None or user not in par:
            return None
        if msgs is None:
            self.records_messages[room] = 1
        else:
            self.records_messages[room] += 1
        return self.records_messages[room]
        
        


# Complexity:
# m = number of members
# r = total rooms
# o = overlapping rooms btwn user_a, user_b
# c = rooms in which a given user is muted
# e = expiration for a given mute
# w = users with a mute
# 1. create_room: O(1)
# 2. join: O(1)
# 3. delete_room: loops over O(w)
# 4. leave: O(1)
# 5. shared_rooms: loop over records O(r) + sort overlapping rooms O(o log o) --> O(r + o log o)
# 6. mute: loops over each user with any mute in place --> O(w)
# 7. is_muted: O(c) 
# 8. send_at: calls self.is_muted O(c)



# Worst case complexity: O(r + o log o + c) --> c <= r --> O(r + o log o)
# Memory: O(r * m + c + e) r = rooms, m = members, c = rooms in which user is muted, e expiration for a given mute, since c == e --> O(r * m + c)
    
# Example tests:


server = ChatServer()
assert server.create_room("general") is True
assert server.join("ann", "general") is True
assert server.join("ann", "general") is False
assert server.create_room("general") is False # Room already exists, so ret false
assert server.join("ann", "blah") is False # Can't join room that doesn't exist
assert server.join("bob", "general") is True # Second user can join room


server = ChatServer()
server.create_room("general")
server.join("ann", "general")
assert server.delete_room("general") == 1
assert server.delete_room("blah") is None # Can't delete room that doesn't exist
server.create_room("general")
server.join("ann", "general")
assert server.join("bob", "general") is True
assert server.delete_room("general") == 2


server = ChatServer()
server.create_room("general")
server.join("ann", "general")
assert server.leave("ann", "general") is True
assert server.leave("ann", "general") is False # user not in room
assert server.leave("bob", "general") is False # no such user
assert server.leave("ann", "random") is False # no such room




server = ChatServer()
server.create_room("general")
server.create_room("random")
server.create_room("music")
server.join("ann", "general")
server.join("ann", "music")
server.join("bob", "music")
server.join("bob", "general")
server.join("bob", "random")
assert server.shared_rooms("ann", "bob") == ["general", "music"]
server.create_room("alpha")
server.join("ann", "alpha")
server.join("bob", "alpha")
assert server.shared_rooms("ann", "bob") == ["alpha", "general", "music"] #alph sorting
assert server.leave("bob", "alpha") is True 
assert server.leave("bob", "general") is True 
assert server.shared_rooms("ann", "bob") == ["music"] # Depricates shared
assert server.leave("bob", "music") is True  
assert server.shared_rooms("ann", "bob") == [] # List goes to len 0 


server = ChatServer()
server.create_room("general")
server.join("ann", "general")
assert server.mute("ann", "general", 10, 5) is True
assert server.is_muted("ann", "general", 14) is True
assert server.is_muted("ann", "general", 15) is False
assert server.is_muted("ann", "general", 16) is False # past date
assert server.is_muted("bob", "general", 10) is False # no such user
assert server.is_muted("ann", "none", 10) is False # no such room



server = ChatServer()
server.create_room("general")
server.join("ann", "general")
assert server.send_at("ann", "general", 1) == 1
server.mute("ann", "general", 2, 5)
assert server.send_at("ann", "general", 3) is None
assert server.send_at("ann", "general", 7) == 2 # Increments
assert server.send_at("bob", "general", 7) is None # No such user
assert server.send_at("ann", "none", 7) is None # No such room


server = ChatServer()
server.create_room("general")
server.join("ann", "general")
server.mute("ann", "general", 10, 50)
server.leave("ann", "general")
server.join("ann", "general")
assert server.is_muted("ann", "general", 20) is False

print(f'all tests pass')
