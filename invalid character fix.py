"""
Question 04: Invalid Character Fix (Naming Rules) - BASIC

System configuration file mein variables ke naam
system-status = "Active" aur user$salary = 45000 rakhe gaye hain.
In mein kaunse special characters rules ke mutabiq allowed nahi
hain aur inhein correct kaise kiya jaye?
"""

# INVALID (would raise SyntaxError if run):
# system-status = "Active"   # hyphen '-' is not allowed (looks like subtraction!)
# user$salary = 45000         # dollar sign '$' is not allowed

# CORRECTED versions -- Python variable names can only contain
# letters, digits, and underscores (_), and cannot start with a digit.
system_status = "Active"
user_salary = 45000

print("system_status:", system_status)
print("user_salary  :", user_salary)

"""
EXPLANATION:
Python naming rules for variables:
1. Allowed characters: letters (a-z, A-Z), digits (0-9), and underscore (_).
2. The name cannot start with a digit.
3. No special characters like -, $, %, @, !, spaces, etc. are allowed.
4. Names are case-sensitive (userSalary and usersalary are different).

Why these specifically fail:
- 'system-status' -> Python reads the hyphen as the subtraction
  operator, so it looks like "system - status" (two variables being
  subtracted), causing a SyntaxError.
- 'user$salary' -> '$' is not a valid identifier character at all in
  Python, so it raises a SyntaxError immediately.

Fix: replace invalid characters with an underscore:
    system-status  -->  system_status
    user$salary    -->  user_salary
"""
