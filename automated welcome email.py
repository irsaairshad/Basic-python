"""
Automated Welcome Email - SIMPLE

Ek function banayein send_welcome(name) jo user ka naam as a
parameter le aur usay welcome email ka message print kare.
"""

def send_welcome(name):
    print(f"Dear {name}, welcome to our platform! We're glad to have you.")

# Calling the function with different names
send_welcome("Sara")
send_welcome("Ahmed")

"""
EXPLANATION:
- def send_welcome(name): defines a function named 'send_welcome' that
  accepts one PARAMETER, 'name'. A parameter is a placeholder for
  whatever value gets passed in when the function is actually called.
- Inside the function, we use 'name' in an f-string to build and print
  a personalized welcome message.
- Each call, send_welcome("Sara") and send_welcome("Ahmed"), passes a
  different ARGUMENT (the actual value) into the 'name' parameter, so
  the function reuses the same logic to greet different users without
  rewriting the print statement each time -- this is the whole point
  of functions: reusable, parameterized blocks of code.
"""
