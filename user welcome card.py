"""
Question 10: User Welcome Card (Formatted Output) - ADVANCED-INTERMEDIATE

User se unka first_name aur last_name do alag inputs ke zariye lein.
Phir un dono variables ko use karke single line mein
"Welcome back, [First Name] [Last Name]!" ka output print karein
bina kisi dynamic type error ke.
"""

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Using an f-string to safely combine two string variables into one
# formatted line -- no type error risk, since both inputs are already
# strings (input() always returns str).
print(f"Welcome back, {first_name} {last_name}!")

# Alternative ways to achieve the exact same result:

# Method 2: simple concatenation with '+' (works because both are strings)
print("Welcome back, " + first_name + " " + last_name + "!")

# Method 3: using .format()
print("Welcome back, {} {}!".format(first_name, last_name))

# Method 4: using print() with commas (auto-adds spaces between arguments)
print("Welcome back,", first_name, last_name, end="!\n")

"""
EXPLANATION:
Since input() always returns a string, concatenating first_name and
last_name with '+' or combining them in an f-string works safely --
there's no str + int mismatch here (that issue only arises when mixing
strings with numbers, as in Question 6). f-strings (f"...") are the
cleanest and most recommended approach in modern Python for combining
variables into readable, formatted output.
"""
