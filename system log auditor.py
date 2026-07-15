"""
System Log Auditor - TUPLES

Ek server security log database access sessions ko store karta hai:
access_logs = (101, 105, 101, 102, 101, 108, 105). Tuple methods ka
use karke check karein ke User ID 101 ne kitni dafa database access
kiya hai, aur User ID 102 pehli dafa kis index position par logged
hai.
"""

access_logs = (101, 105, 101, 102, 101, 108, 105)

# .count(value) -- a built-in tuple method that counts how many times
# a specific value appears in the tuple.
user_101_count = access_logs.count(101)

# .index(value) -- a built-in tuple method that returns the index of
# the FIRST occurrence of a specific value.
user_102_first_index = access_logs.index(102)

print("Access logs:", access_logs)
print("User 101 accessed the database", user_101_count, "time(s)")
print("User 102 was first logged at index position:", user_102_first_index)

"""
EXPLANATION:
- Tuples only have TWO built-in methods (since they're immutable,
  they don't need methods like .append() or .remove()):
    1. .count(value) -> returns how many times 'value' appears in
       the tuple. Here, access_logs.count(101) scans the tuple and
       finds 101 appears 3 times.
    2. .index(value) -> returns the index of the FIRST occurrence of
       'value'. Here, access_logs.index(102) finds that 102 first
       appears at index 3 (remember: indexing starts at 0, so
       positions are 0,1,2,3,... and 102 is the 4th item overall,
       at index 3).
- These two methods are typically enough for basic auditing/searching
  tasks on fixed, unchanging data like security logs.
"""
