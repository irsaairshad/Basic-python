"""
Question 01: User Registration System - SIMPLE

User se uska name, age, aur city input lein aur ek Formatted String
(f-string) ka istemal karte hue welcome message print karein
(e.g., "Welcome [Name] from [City]").
"""

name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")

# f-string: put variables directly inside {curly braces} within the
# string, prefixed with 'f' -- Python fills in the values automatically.
print(f"Welcome {name} from {city}")

# Bonus: showing all 3 collected fields together
print(f"Registration complete -> Name: {name}, Age: {age}, City: {city}")

"""
EXPLANATION:
- An f-string (formatted string literal) starts with f" or f' before
  the quotes, and lets you embed variables directly inside {} without
  needing to manually concatenate with '+' or convert types with str().
- f"Welcome {name} from {city}" automatically inserts whatever values
  'name' and 'city' currently hold into the string at those positions.
- This is the modern, cleanest way to build formatted output in Python
  3.6+.
"""
