"""
Automated Vehicle Diagnostic (Simple Method) - SIMPLE

Ek Vehicle class banayein jismein ek method run_diagnostic() ho jo
print kare "System check complete: 0 errors found."
"""

class Vehicle:
    def run_diagnostic(self):
        print("System check complete: 0 errors found.")


car = Vehicle()
car.run_diagnostic()

"""
EXPLANATION:
- run_diagnostic(self) is a simple METHOD defined inside the Vehicle
  class -- it doesn't need any extra parameters besides 'self' (which
  Python passes automatically, referring to whichever object called
  the method).
- Creating an object (car = Vehicle()) and then calling
  car.run_diagnostic() executes the code inside that method for THAT
  specific object, printing the fixed diagnostic message.
- This is the simplest form of a method: no input needed, no value
  returned -- it just performs an action (printing a message) when
  called.
"""
