"""
Question 05: Syntax Halt Analysis (Interpreter Behavior) - BASIC

Aapke code file mein 3 lines hain:
Line 1: print("Starting System...")
Line 2: print("Loading Database (unclosed quote error)
Line 3: print("System Ready!")

Jab aap is program ko run karenge, to kya Line 1 execute hogi ya
program pehle hi ruk jayega? Python interpreter ke line-by-line
chalne aur error handle karne ka behavior samjhayein.
"""

# The ORIGINAL broken code (do not uncomment -- shown here only as reference):
#
# print("Starting System...")
# print("Loading Database (unclosed quote error)
# print("System Ready!")
#
# Result: NOTHING prints at all -- not even Line 1!

# ANSWER: Line 1 will NOT execute.
#
# Python is not a "line-by-line runs-then-checks" language in the way
# people sometimes assume. Before running ANY code, Python's interpreter
# first fully PARSES/compiles the entire file into bytecode. Since
# Line 2 has an unclosed string (missing closing quote), this is a
# SyntaxError, and syntax errors are caught at *compile time*, before
# execution of ANY line begins -- including Line 1.
#
# So the output is simply a traceback like:
#   File "script.py", line 2
#       print("Loading Database (unclosed quote error)
#            ^
#   SyntaxError: unterminated string literal (detected at line 2)
#
# and "Starting System..." is never printed.

# CORRECTED version (this WILL print all 3 lines correctly):
print("Starting System...")
print("Loading Database (unclosed quote error)")   # quote closed properly
print("System Ready!")

"""
EXPLANATION:
- Syntax errors (like unclosed quotes, mismatched brackets, bad
  indentation) are caught during the PARSING/COMPILING stage, before
  the program starts running at all. So even earlier, "correct" lines
  won't execute if a later line has a syntax error.
- This is different from RUNTIME errors (like ZeroDivisionError or
  TypeError), which only happen once the program starts running and
  execution actually reaches that specific line -- so earlier lines
  DO print in that case.
"""
