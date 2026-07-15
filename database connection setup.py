"""
Database Connection Setup (Tuple Usage) - SIMPLE

Ek DatabaseConfig class banayein jismein host aur port ko aik tuple
attribute credentials = ("localhost", 3306) mein store kiya jaye
taake credentials immutable rahin.
"""

class DatabaseConfig:
    def __init__(self):
        self.credentials = ("localhost", 3306)   # (host, port) stored as a tuple


config = DatabaseConfig()

print("Host:", config.credentials[0])
print("Port:", config.credentials[1])

# Attempting to change the credentials would fail, proving they're safe:
try:
    config.credentials[1] = 5432
except TypeError as e:
    print("TypeError caught! Credentials are protected:", e)

"""
EXPLANATION:
- credentials is stored as a TUPLE: ("localhost", 3306), combining the
  host and port into a single, fixed pair of values.
- Tuples are IMMUTABLE in Python -- once created, individual elements
  inside them cannot be reassigned. Trying
  config.credentials[1] = 5432 raises:
      TypeError: 'tuple' object does not support item assignment
- This is exactly why a tuple is a good choice here: database
  connection details are sensitive, fixed configuration values that
  shouldn't be accidentally modified anywhere else in the program --
  using a tuple enforces that safety at the language level.
"""
