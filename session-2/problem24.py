'''
Session 2, Problem 24: Meeting room bookings (progressive). Level 1

Time limit: 25 minutes, including writing your own tests. Aim for working code by about minute 20. Hard stop at 37 minutes. Before coding: write __init__ with an example comment, run one example call through it, and check that your dict keys are unique and are what the spec looks things up by.

Write a class that books meeting rooms by the hour.

Class name: RoomScheduler

Creating a RoomScheduler() takes no arguments, and a new scheduler starts with no bookings. Any room name can be booked; rooms don’t need to be created first.

Methods:

book(room, person, hour): room and person are strings, hour is a non-negative int. Books the room for that person for that hour. Returns True if the booking was made, or False, with nothing changed, if the room is already booked for that hour.
cancel(room, person, hour): room and person are strings, hour is a non-negative int. Cancels the booking for that room and hour, but only if it belongs to person. Returns True if a booking was cancelled. Returns False, with nothing changed, if the room isn’t booked for that hour or is booked by someone else.
booked_by(room, hour): room is a string, hour is a non-negative int. Returns the name of the person who booked that room for that hour, or None if it isn’t booked.

Session 2, Problem 24: Meeting room bookings. Level 2

Time limit: 25 minutes, including writing your own tests. Aim for working code by about minute 20. Hard stop at 37 minutes. Start with your one-line variable list and one example call through your structure.

Add two methods to your RoomScheduler class. Everything from Level 1 must keep working.

New methods:

free_hours(room, start, end): room is a string; start and end are non-negative ints with start ≤ end. Returns a list of every hour from start to end, inclusive, for which the room is not booked, in increasing order. A room with no bookings is free for every hour.
person_schedule(person): person is a string. Returns a list of all the person’s bookings, each as a string in the format "room(hour)". The list is sorted by hour, earliest first; bookings at the same hour are sorted alphabetically by room. Returns an empty list if the person has no bookings.

'''

class RoomScheduler:
    def __init__(self):
        self.records: dict[str, dict[int, str]] = {} # k = room, k=hour, v=person
    

    '''1. book(room, person, hour): room and person are strings, hour is a non-negative int. 
    Books the room for that person for that hour. 
    Returns True if the booking was made, or False, with nothing changed, if the room is already booked for that hour.'''
    def book(self, room: str, person: str, hour: int):
        room_data = self.records.get(room, None)
        if room_data is None:
            self.records[room] = {hour:person}
            return True
        elif hour not in room_data:
            self.records[room][hour] =person
            return True
        return False


    '''2. cancel(room, person, hour): room and person are strings, hour is a non-negative int. 
    Cancels the booking for that room and hour, but only if it belongs to person. Returns True if a booking was cancelled. 
    Returns False, with nothing changed, if the room isn’t booked for that hour or is booked by someone else.'''
    def cancel(self, room: str, person: str, hour: int):
        result = self.records.get(room, {}).get(hour, None)
        print(f'result: {result}, person: {person}')
        if result is not None and result == person:
            self.records.get(room, {}).pop(hour, None)
            return True
        return False


    '''3. booked_by(room, hour): room is a string, hour is a non-negative int. 
    Returns the name of the person who booked that room for that hour, or None if it isn’t booked.'''
    def booked_by(self, room: str, hour: int):
        return self.records.get(room, {}).get(hour, None)


    '''4. free_hours(room, start, end): room is a string; start and end are non-negative ints with start ≤ end. 
    Returns a list of every hour from start to end, inclusive, for which the room is not booked, in increasing order. 
    A room with no bookings is free for every hour.'''
    def free_hours(self, room: str, start: int, end: int):
        room_data = self.records.get(room, None)
        free = []
        n = start
        print(f'n: {n}, start: {start}, end: {end}')
        while n <= end:
            if self.records.get(room, {}).get(n, None) is None:
                free.append(n)
            n += 1
        print(f'free: {free}')
        return free
                
        
    '''5. person_schedule(person): person is a string. 
    Returns a list of all the person’s bookings, each as a string in the format "room(hour)". 
    The list is sorted by hour, earliest first; bookings at the same hour are sorted alphabetically by room. 
    Returns an empty list if the person has no bookings.'''
    def person_schedule(self, person: str):
        solution_list = []
        for booking_room, booking_data in self.records.items():
            for booking_hour, booking_name in booking_data.items():
                if booking_name == person:
                    solution_list.append((booking_room, booking_hour))
        return [f'{room}({hour})' for room, hour in sorted(solution_list, key=lambda kv:(kv[1], kv[0]))]
    

# Complexity
# r = total rooms
# h = total hours with a booking across all rooms
# b = hours booked for a given room
# t = time between booking checking window
# p = a given person's bookings across all rooms
# 1. book --> O(1)
# 2. cancel --> O(1)
# 3. booked_by --> O(1)
# 4. free_hours --> while over all booking times within window --> O(t)
# 5. person_schedule --> loop over rooms O(r) + Loop over hours booked for that room, e.g. total hours in aggregate O(h) + sort O(p log p)--> O(r+h)


# Worst case complexity: O(r*b)
# Memory: O(r+h)


# Example tests:


scheduler = RoomScheduler()
assert scheduler.book("blue", "ann", 9) is True
assert scheduler.book("blue", "bob", 9) is False
assert scheduler.cancel("blue", "bob", 9) is False
assert scheduler.book("blue", "ann", 9) is False # Same person, same time

scheduler = RoomScheduler()
scheduler.book("blue", "ann", 9)
assert scheduler.cancel("blue", "bob", 9) is False # This person doesn't have the booking
assert scheduler.cancel("red", "ann", 9) is False # No such room
assert scheduler.cancel("blue", "ann", 9) is True
assert scheduler.cancel("blue", "ann", 9) is False # Cannot double-cancel

assert scheduler.booked_by("blue", 9) is None

scheduler = RoomScheduler()
scheduler.book("blue", "ann", 10)
scheduler.book("blue", "bob", 12)
assert scheduler.free_hours("blue", 9, 13) == [9, 11, 13]
scheduler.book("blue", "ann", 11)
assert scheduler.free_hours("blue", 10, 12) == [] # No hours free


scheduler = RoomScheduler()
assert scheduler.free_hours("blue", 9, 13) == [9, 10, 11, 12, 13] # All hours free

scheduler = RoomScheduler()
scheduler.book("red", "ann", 14)
scheduler.book("blue", "ann", 9)
scheduler.book("green", "ann", 14)
assert scheduler.person_schedule("ann") == ["blue(9)", "green(14)", "red(14)"]
scheduler.book("zebra", "ann", 1)
assert scheduler.person_schedule("ann") == ["zebra(1)", "blue(9)", "green(14)", "red(14)"]



scheduler = RoomScheduler()
assert scheduler.person_schedule("ann") == [] # No bookings

print('all tests pass')