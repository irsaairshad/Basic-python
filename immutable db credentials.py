"""
Immutable DB Credentials - SIMPLE

Database ka Host aur Port ek tuple mein store karein aur code mein
usay change karne ki koshish karein taake error aaye aur sabit ho ke
credentials (tuples) safe hain.
"""

db_credentials = ("localhost", 5432)   # (host, port)

print("DB credentials:", db_credentials)

# Attempting to modify an element of the tuple -- this SHOULD fail,
# proving tuples are immutable (cannot be changed after creation).
try:
    db_credentials[1] = 5433   # trying to change the port
except TypeError as e:
    print("TypeError caught! Credentials could not be changed.")
    print("Error message:", e)

print("DB credentials (still unchanged):", db_credentials)

"""
EXPLANATION:
- Tuples are IMMUTABLE, meaning once created, their individual elements
  cannot be reassigned. Trying db_credentials[1] = 5433 raises:
      TypeError: 'tuple' object does not support item assignment
- This is exactly why sensitive, fixed data like database host/port
  credentials is a good candidate for a tuple -- it guarantees nothing
  in the program can accidentally alter these values later on.
- If different credentials are genuinely needed, you'd have to create
  a brand NEW tuple (e.g. db_credentials = ("localhost", 5433)) rather
  than editing the existing one in place.
"""
