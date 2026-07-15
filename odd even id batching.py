"""
Odd/Even ID Batching - INTERMEDIATE

Ek while loop 1 se 20 tak chalayein. Modulo operator % ka istemal
karte hue check karein, agar ID even hai toh "Process Batch A", agar
odd hai toh "Process Batch B" print karein.
"""

id_number = 1

while id_number <= 20:
    if id_number % 2 == 0:
        print(f"ID {id_number}: Process Batch A")
    else:
        print(f"ID {id_number}: Process Batch B")
    id_number += 1

"""
EXPLANATION:
- The modulo operator (%) gives the REMAINDER of a division. Any
  number % 2 will be either 0 (if the number is even) or 1 (if odd).
- id_number % 2 == 0 checks "is this ID evenly divisible by 2?" -- if
  yes, it's an even ID, so it goes to "Batch A"; otherwise (remainder
  is 1), it's odd, so it goes to "Batch B".
- The while loop runs from id_number = 1 up to and including 20,
  incrementing id_number by 1 each pass, and stops once id_number
  becomes 21 (since 21 <= 20 is False).
"""
