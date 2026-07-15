"""
Spacing Debugger (Indentation Error) - ADVANCED-INTERMEDIATE

Aapne internet se ek code copy kiya aur jab use chalaya to
"Unexpected Indentation" ka error mila. Python mein whitespace ya
extra spaces/tabs ka kya maqsad hota hai aur hum apni marzi se rasta
chhor kar code kyun nahi likh sakte?
"""

# INCORRECT example (would raise IndentationError: unexpected indent):
#
# print("Starting...")
#     print("This line has an extra unexpected indent")
#
# Even though there's no if/for/function here, the second line has
# an indent Python doesn't expect, so it errors out.

# CORRECT example -- indentation is only added when STARTING a new
# code block (after a colon ':'), and every line within that block
# must line up with the SAME amount of indentation:
def start_system():
    print("Starting...")          # indented once: inside the function
    print("Loading modules...")   # same indentation level -> still inside
print("System ready!")            # no indent -> outside the function

start_system()

"""
EXPLANATION:
Unlike many other languages (C, Java, JavaScript) where curly braces
{ } define code blocks and whitespace is just cosmetic, PYTHON USES
INDENTATION ITSELF to define where a block of code begins and ends
(inside if-statements, loops, functions, classes, etc.).

- Indentation is only expected right after a line ending in a colon (:),
  such as `if condition:`, `for x in range(5):`, `def my_function():`.
- All statements inside that block must share the EXACT SAME indentation
  level (commonly 4 spaces, consistently).
- If you indent a line where Python does NOT expect a new block to
  start (e.g. randomly indenting a line after a plain print statement),
  Python raises: IndentationError: unexpected indent.
- If lines inside the same block don't match each other's indentation,
  Python raises: IndentationError: unindent does not match any outer
  indentation level.

Why we "can't just write code wherever we want": because Python relies
on indentation as actual SYNTAX (not just style), inconsistent or
random spacing would make it impossible for the interpreter to know
which lines belong to which block -- so it enforces strict, consistent
indentation rules instead of using braces.
"""
