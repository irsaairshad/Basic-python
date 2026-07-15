"""
Single-Element Config Entry - TUPLES

Aapko server ka deployment mode "Production" aik single-value tuple
mein store karna hai. Ek aisa code likhein jo isay sahi tarike se
single-item tuple banaye (bina string treat kiye) aur user ko iska
proper data type check karke print karwaye.
"""

# COMMON MISTAKE (do NOT do this):
# deployment_mode = ("Production")
# This does NOT create a tuple! Parentheses around a single value,
# without a comma, are just treated as normal parentheses (like in
# math: (5) is just 5). So this actually creates a plain STRING.

# CORRECT way -- a single-item tuple REQUIRES a trailing comma:
deployment_mode = ("Production",)

print("Value:", deployment_mode)
print("Data type:", type(deployment_mode))

"""
EXPLANATION:
- The thing that makes a tuple a tuple is the COMMA, not the
  parentheses! Parentheses are actually optional in most cases
  (e.g. x = 1, 2, 3 is already a tuple).
- For a SINGLE-item tuple specifically, you MUST include a trailing
  comma: ("Production",) -- without it, ("Production") is just a
  string wrapped in redundant parentheses, and type() would show
  <class 'str'> instead of <class 'tuple'>.
- Running type(deployment_mode) confirms it's genuinely a tuple:
      <class 'tuple'>
  This is a classic beginner "gotcha" in Python that this question is
  specifically testing.
"""
