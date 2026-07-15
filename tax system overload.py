"""
Tax System Overload (Simulated Method Overloading) - POLYMORPHISM

Python natively method overloading (ek hi naam ke multiple functions
different inputs ke sath) support nahi karta. Lekin agar aapko ek hi
method calculate_tax() ke zariye local income (1 parameter) aur
international income (2 parameters) ka tax nikalna ho, toh aap
default argument (tax_rate=None) ka use karke isay kaise handle
karenge?
"""

class TaxCalculator:

    def calculate_tax(self, income, tax_rate=None):
        if tax_rate is None:
            # Only ONE argument was given (local income case) ->
            # use a fixed, standard local tax rate.
            tax = income * 0.05
            print(f"Local income tax on {income}: {tax}")
        else:
            # A SECOND argument WAS given (international income case) ->
            # use the custom tax_rate that was passed in.
            tax = income * tax_rate
            print(f"International income tax on {income} at rate {tax_rate}: {tax}")

        return tax


calculator = TaxCalculator()

# Called with ONE parameter -- behaves like the "local income" version
calculator.calculate_tax(50000)

# Called with TWO parameters -- behaves like the "international income" version
calculator.calculate_tax(50000, 0.15)

"""
EXPLANATION:
- Unlike some languages (Java, C++), Python does NOT allow you to
  define multiple methods with the exact same name but different
  parameter lists -- if you tried, the LAST definition would simply
  overwrite all earlier ones.
- Instead, Python "simulates" this behavior using a DEFAULT ARGUMENT:
  tax_rate=None. This lets ONE single method handle BOTH cases:
    1. calculate_tax(50000)       -> tax_rate stays None (not provided),
       so we treat this as the "local income" scenario and apply a
       fixed, built-in tax rate (5%).
    2. calculate_tax(50000, 0.15) -> tax_rate IS provided (0.15), so we
       treat this as the "international income" scenario and use that
       custom tax rate instead.
- The 'if tax_rate is None:' check is what lets the method dynamically
  decide which behavior to run, based on how many arguments the caller
  actually supplied -- effectively mimicking method overloading using
  a single, flexible method definition.
"""
