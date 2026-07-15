"""
Question 06: Type Error in Logging (Concatenation) - ADVANCED-INTERMEDIATE

Ek developer server logging ke liye code likhta hai:
print("Active connections: " + 15).
Python is par error kyun dega (Hint: string aur integer concatenation
issue), aur isay user ko baghair error dikhaye sahi tarike se print
karne ke do tareeqe kya hain?
"""

# The ORIGINAL broken code (do not uncomment -- shown as reference):
# print("Active connections: " + 15)
# TypeError: can only concatenate str (not "int") to str

active_connections = 15

# METHOD 1: Convert the integer to a string using str(), then concatenate with '+'
print("Active connections: " + str(active_connections))

# METHOD 2: Use an f-string (formatted string literal) -- no manual conversion needed
print(f"Active connections: {active_connections}")

# BONUS METHOD 3: Use commas in print() -- Python auto-converts each argument to string
print("Active connections:", active_connections)

"""
EXPLANATION:
The '+' operator, when used between strings, means "concatenation"
(joining text together) -- and it requires BOTH sides to be the SAME
type (str + str). Here, "Active connections: " is a string, but 15 is
an integer (int). Python refuses to silently guess what you meant, so
it raises:
    TypeError: can only concatenate str (not "int") to str

Fixes:
1. str(15) explicitly converts the integer to a string first, so you're
   now doing str + str, which works.
2. f-strings (f"...{variable}...") let Python handle the conversion
   automatically inside the curly braces -- cleaner and preferred in
   modern Python.
3. print() with a comma automatically converts and space-separates each
   argument, avoiding the type error entirely.
"""
