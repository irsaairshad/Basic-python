"""
Question 03: Memory Caching Debugger (id Function) - BASIC

Aapko check karna hai ke system memory mein ek variable
session_token = "XYZ789" kis address/location par store hua hai.
Aap is location ko check karne ke liye kis function ka use karenge?
"""

session_token = "XYZ789"

# The built-in id() function returns the memory address (identity)
# of an object, as an integer, in the current Python implementation.
memory_address = id(session_token)

print("session_token value  :", session_token)
print("session_token address:", memory_address)

"""
EXPLANATION:
Python's built-in id() function is used to check the memory
location/identity of any object. It returns a unique integer for
that object for as long as it exists. In CPython (the standard
Python implementation), this integer often corresponds directly
to the object's memory address.

Example:
    id(session_token)   ->  returns something like 140234501928496

Note: this address can change between different runs of the program,
and two variables can share the same id() if they point to the exact
same object in memory (e.g. small cached integers or interned strings).
"""
