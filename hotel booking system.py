"""
Hotel Booking System (State Mutation) - SIMPLE

Ek HotelRoom class banayein jismein is_occupied = True ho. Ek method
checkout() banayein jo is value ko update karke False kar de.
"""

class HotelRoom:
    def __init__(self):
        self.is_occupied = True   # room starts as occupied

    def checkout(self):
        self.is_occupied = False


room = HotelRoom()
print("Before checkout, occupied:", room.is_occupied)

room.checkout()
print("After checkout, occupied: ", room.is_occupied)

"""
EXPLANATION:
- self.is_occupied = True is set in the constructor, so every new
  HotelRoom object starts out marked as occupied.
- checkout(self) is a method that MUTATES (changes) the object's own
  state -- calling room.checkout() directly updates that specific
  room's is_occupied attribute from True to False.
- This shows how an object's data isn't fixed forever -- methods can
  update ("mutate") an object's attributes over time to reflect
  changes in the real world, like a guest checking out of a room.
"""
