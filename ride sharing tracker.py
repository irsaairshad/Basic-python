"""
Ride-Sharing Tracker (Counter) - STATIC KEYWORDS

Aik ride-sharing platform (jaise Uber/Indrive) par jab bhi koi
customer naya ride book karta hai (Ride class ka object banta hai),
toh system ko total rides ka count +1 barhana hota hai. Is dynamic
counter ko update karne ke liye aap instance variable use karenge ya
class/static variable?
"""

class Ride:
    total_rides = 0   # CLASS (static) variable -- shared counter across ALL rides

    def __init__(self, passenger_name):
        self.passenger_name = passenger_name   # instance variable -- unique per ride

        # Updating the CLASS variable through the class name (not self),
        # so the change is reflected globally for every object.
        Ride.total_rides += 1


ride1 = Ride("Sara")
ride2 = Ride("Ahmed")
ride3 = Ride("Zain")

print(f"Total rides booked so far: {Ride.total_rides}")

"""
ANSWER / EXPLANATION:
This should be a CLASS (static) VARIABLE, not an instance variable.

WHY: An instance variable belongs to ONE specific object and starts
fresh for each new object -- it can't naturally "remember" a running
total across MULTIPLE different ride bookings. A class variable, on
the other hand, is shared across every object of that class, so
updating it inside __init__ (Ride.total_rides += 1) means EVERY new
Ride object contributes to the SAME shared counter, giving us an
accurate running total of ALL rides ever created -- exactly what's
needed to track "total rides across the whole platform".

Note: we update it using the CLASS name (Ride.total_rides += 1) rather
than self.total_rides += 1, because using 'self.' for a += operation
would actually create a brand NEW instance variable shadowing the
class variable, instead of updating the shared one.
"""
