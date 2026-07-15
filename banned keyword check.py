"""
Banned Keyword Check (Naming Rules) - BASIC

Aap user roles save karne ke liye variable ka naam for = "Admin"
rakhna chahte hain. Python is par error kyun deta hai, aur Python
ke "reserved words/keywords" ka variable naming se kya talluq hai?
"""

# This line would cause a SyntaxError if uncommented, because
# 'for' is a reserved keyword in Python (used for loops):
#
# for = "Admin"     # SyntaxError: invalid syntax

# Correct way -- choose a name that is NOT a reserved keyword:
user_role = "Admin"
print("User role:", user_role)

"""
EXPLANATION:
Python has a fixed set of "reserved words" (keywords) that are part of
its own grammar/syntax -- words like for, if, else, while, class, def,
import, True, False, None, etc. These words have special meaning to the
Python interpreter, so they CANNOT be used as identifiers (variable
names, function names, etc.), because doing so would confuse the parser
about whether you mean the keyword's built-in behavior or a variable.

You can see the full list of keywords in Python using:
    import keyword
    print(keyword.kwlist)

Naming rule: a variable name must not be a reserved keyword.
"""

import keyword
print("\nPython's reserved keywords:")
print(keyword.kwlist)
