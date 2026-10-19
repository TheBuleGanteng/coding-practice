'''
Session 2, Problem 23: Room bookings (progressive). Level 1

Time limit: 25 minutes, including writing your own tests. Aim for working code by about minute 20. Hard stop at 37 minutes. Before coding: write __init__ with an example comment, run one example call through it, and check which row of your structures table this is.

Write a class that books hotel rooms for individual nights.

Class name: Hotel

Creating a Hotel() takes no arguments, and a new hotel starts with no bookings. Any room name can be booked; rooms don’t need to be created first.

Methods:

book(room, guest, night): room and guest are strings, night is a non-negative int. Books the room for that guest on that night. Returns True if the booking was made, or False, with nothing changed, if the room is already booked that night.
cancel(room, night): room is a string, night is a non-negative int. Cancels that room’s booking for that night and returns the name of the guest whose booking was cancelled. Returns None if the room isn’t booked that night.
guest_on(room, night): room is a string, night is a non-negative int. Returns the name of the guest booked in that room on that night, or None if it isn’t booked.
'''

class Hotel:
    
    def __init__(self):
        self.records: dict[str, dict[int, str]] = {} # k= room (str), k=night(int), v=guest(str)
        
    '''1. book(room, guest, night): room and guest are strings, night is a non-negative int. 
    Books the room for that guest on that night. 
    Returns True if the booking was made, or False, with nothing changed, if the room is already booked that night.'''
    def book(self, room: str, guest: str, night: int):
        # Check if room is freee
        room_data = self.records.get(room, None)
        # If room doesn't have bookings, set up inner dict
        if room_data is None:
            self.records[room] = {night: guest}
            return True
        # If room has bookings, check if there is a booking for that night
        if night not in room_data:
            # If no booking exists, book the room for that person+night
            self.records[room][night] = guest
            print(f'self.records.items(): {self.records.items()}')
            return True

        # If no booking made, return False
        print(f'self.records.items(): {self.records.items()}')
        return False
            

    '''2. cancel(room, night): room is a string, night is a non-negative int. 
    Cancels that room’s booking for that night and returns the name of the guest whose booking was cancelled. 
    Returns None if the room isn’t booked that night.'''
    def cancel(self, room: str, night: int):
        # Returns value (guest name) if successful, None if not
        return self.records.get(room, {}).pop(night, None)
            

    '''3. guest_on(room, night): room is a string, night is a non-negative int. 
    Returns the name of the guest booked in that room on that night, or None if it isn’t booked.'''
    def guest_on(self, room: str, night: int):
        return self.records.get(room, {}).get(night, None)

# Complexity:
# r = total number of rooms
# n = total number of nights booked across all rooms
# 1. book --> O(1)
# 2. cancel --> get+pop O(1)
# 3. guest_on --> get+get O(1)

# Worst-case complexity: O(1)
# Memory: O(r + n)


#Example tests:

hotel = Hotel()
assert hotel.book("101", "ann", 5) is True
assert hotel.book("101", "bob", 5) is False
assert hotel.guest_on("101", 5) == "ann"
assert hotel.book("101", "bob", 6) is True # New booking
assert hotel.guest_on("102", 5) is None # no such room
assert hotel.guest_on("101", 4) is None # no booking on that date

hotel = Hotel()
hotel.book("101", "ann", 5)
assert hotel.cancel("101", 5) == "ann"
assert hotel.cancel("100", 5) is None # No such room
assert hotel.cancel("101", 6) is None # No booking on that date