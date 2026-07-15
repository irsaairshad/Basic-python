"""
ATM Security Check (Private Attribute) - ENCAPSULATION

Ek banking portal mein aapne security ke liye __balance ko private
variable banaya hai. Agar koi junior developer bahar se direct
customer_account.__balance likh kar value change karne ki koshish
karega, toh Python kya error dega aur kyun?
"""

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # double underscore -> "private" attribute

    def get_balance(self):
        return self.__balance


customer_account = BankAccount(15000)

# Trying to access the private attribute directly from OUTSIDE the class:
try:
    print(customer_account.__balance)
except AttributeError as e:
    print("AttributeError caught!")
    print("Error message:", e)

# The CORRECT way to access it -- through a public method:
print("Correct way (via getter):", customer_account.get_balance())

"""
ANSWER / EXPLANATION:
Python raises:
    AttributeError: 'BankAccount' object has no attribute '__balance'

WHY: When you prefix an attribute with a double underscore (__balance),
Python applies "Name Mangling" internally -- it silently renames the
attribute to _BankAccount__balance (i.e. _ClassName__attribute) inside
the object. So __balance, as literally written, doesn't exist under
that exact name from outside the class -- trying
customer_account.__balance looks for an attribute that was never
actually stored under that name, hence the AttributeError.

This is Python's way of enforcing basic encapsulation: it discourages
(though doesn't 100% forbid -- see the "Gentleman's Agreement"
solution) direct external access to internal data, pushing developers
toward using proper getter/setter methods instead.
"""
