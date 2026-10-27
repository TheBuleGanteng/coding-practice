'''
Session 3, Problem 4: Recently played (progressive). Level 1

Time limit: 25 minutes, including writing your own tests. Before coding, read all three methods, note what data each needs, then write __init__ with an example comment and run one example call through it. Aim for working code by about minute 20. Hard stop at 37 minutes. Before running your tests, point at the line that handles each “Returns…” sentence.

Write a class that keeps, for each user, a limited list of the songs they played most recently.

Class name: RecentlyPlayed

Creating a RecentlyPlayed(limit) takes one argument: limit, a positive int, the most songs kept for any one user. It starts with no users.

Methods:

play(user, song): user and song are strings. Records that the user played the song, making it their most recently played. If this makes the user’s list hold more than limit songs, removes the one they played least recently. Returns the removed song, or None if nothing was removed.
plays(user, song): user and song are strings. Returns how many times the user has played the song while it has been in their list, as an int. If a song is removed and later played again, its count starts over from 1. Returns 0 if the song isn’t in the user’s list.
least_recent(user): user is a string. Returns the song in the user’s list that they played least recently, or None if their list is empty.
'''

class RecentlyPlayed:
    
    def __init__(self, limit: int):
        self.limit = limit
        self.records: dict[str, dict[str, int]] = {} # k=user(str) k=song (str), v = plays (int)
        
    '''1. play(user, song): user and song are strings. 
    Records that the user played the song, making it their most recently played. 
    If this makes the user’s list hold more than limit songs, removes the one they played least recently. 
    Returns the removed song, or None if nothing was removed.'''
    def play(self, user:str, song:str):
        user_data = self.records.get(user, None)
        print(f'user: {user}, song: {song}, user_data: {user_data}')
        # If the user doesn't exist set up the inner dict
        if user_data is None:
            self.records[user] = {song:1}
        else:
            song_data = user_data.get(song, None)
            print(f'song_data: {song_data}')
            # If there is song data, pop it and add it back with correct play count
            if song_data is not None:
                self.records[user].pop(song, None)
                self.records[user][song] = song_data+1
            else:
                self.records[user][song] = 1
        # Check new length against limit
        if len(self.records[user]) > self.limit:
            removed = next(iter(self.records[user]))
            self.records[user].pop(removed)
            return removed
        return None

    '''2. plays(user, song): user and song are strings. 
    Returns how many times the user has played the song while it has been in their list, as an int. 
    If a song is removed and later played again, its count starts over from 1. 
    Returns 0 if the song isn’t in the user’s list.'''
    def plays(self, user: str, song:str):
        return self.records.get(user, {}).get(song, 0)


    '''3. least_recent(user): user is a string. 
    Returns the song in the user’s list that they played least recently, 
    or None if their list is empty.'''
    def least_recent(self, user:str):
        return next(iter(self.records.get(user, {})), None)


# Example tests:


rp = RecentlyPlayed(2)
rp.play("ann", "song1")
rp.play("ann", "song2")
rp.play("ann", "song1")
assert rp.least_recent("ann") == "song2"
assert rp.plays("ann", "song1") == 2

rp = RecentlyPlayed(2)
rp.play("ann", "song1")
rp.play("ann", "song2")
assert rp.play("ann", "song3") == "song1"