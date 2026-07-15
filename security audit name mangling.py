"""
Security Audit (Gentleman's Agreement) - ENCAPSULATION

Junior developer ko lagta hai ke double underscore __ lagane ke baad
Python mein data 100% lock ho jata hai. Aap use kaise samjhayenge ke
Python mein back-end par Name Mangling kya hoti hai aur isay
"Gentleman's Agreement" kyun kaha jata hai?
"""

class Employee:
    def __init__(self, salary):
        self.__salary = salary   # looks "private" because of __


emp = Employee(75000)

# The "normal" way fails, as expected:
try:
    print(emp.__salary)
except AttributeError as e:
    print("Direct access blocked:", e)

# BUT -- Python only RENAMES the attribute internally, it doesn't
# truly hide it. If you know the mangled name, you CAN still access it:
print("Accessed via mangled name:", emp._Employee__salary)

"""
ANSWER / EXPLANATION:
Name Mangling: when Python sees an attribute name starting with two
underscores (like __salary) inside a class, it automatically renames
it internally to:
    _ClassName__attributeName
So self.__salary inside class Employee actually gets stored as
_Employee__salary. This is why emp.__salary (the "raw" name) raises
an AttributeError -- that exact name was never used internally.

However, as shown above, the attribute IS still fully accessible if
you use its real, mangled name: emp._Employee__salary. Nothing in
Python truly PREVENTS this access -- it's just deliberately made
inconvenient and non-obvious.

This is why it's called a "Gentleman's Agreement": Python doesn't
enforce TRUE privacy/security the way some other languages
(like Java's 'private' keyword) do. Instead, it relies on developers
AGREEING, by convention, to respect the double-underscore as a signal
of "please don't touch this from outside the class" -- but a
determined developer can still bypass it if they really want to.
True protection in Python is more about discipline and clean
API design than an unbreakable technical barrier.
"""
