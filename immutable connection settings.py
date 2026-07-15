"""
Immutable Connection Settings - TUPLES

Aapne security reasons ke liye server connectivity details ek tuple
mein store ki hain: server_config = ("192.168.1.1", 8080). Ek test
code likhein jo is configuration ke port number (index 1) ko update
karne ki koshish kare, taake check kiya ja sake ke system data edit
to nahi ho raha (TypeError inspect karein).
"""

server_config = ("192.168.1.1", 8080)

print("Original config:", server_config)

# Attempting to change an element of a tuple by index -- this is
# EXPECTED TO FAIL, because tuples are IMMUTABLE (cannot be changed
# after creation), unlike lists.
try:
    server_config[1] = 9090   # trying to update the port number
except TypeError as e:
    print("TypeError caught! Tuples cannot be modified.")
    print("Error message:", e)

print("Config after attempted update (unchanged):", server_config)

"""
EXPLANATION:
- Tuples are created with parentheses: (item1, item2, ...), and once
  created, their contents CANNOT be changed, added to, or removed --
  this is what "immutable" means.
- Trying server_config[1] = 9090 raises:
      TypeError: 'tuple' object does not support item assignment
- This immutability is exactly WHY tuples are used for things like
  server configs or connection settings in real systems -- it protects
  important, fixed data from being accidentally (or maliciously)
  changed elsewhere in the program.
- If you truly need to "update" a tuple, the only way is to create a
  brand NEW tuple, e.g.:
      server_config = (server_config[0], 9090)
  This doesn't modify the original tuple -- it replaces the variable
  with a completely new tuple object.
"""
