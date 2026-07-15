"""
Variable Mutability (Price Override) - BASIC

Ek product ki initial price discount_price = 1500 set ki gayi hai.
Black Friday sale khatam hone par aapko is variable ki value ko
update karke original_price = 2000 ke barabar assign karna hai.
Assignment operator ka use karke value update karein aur updated
price print karein.
"""

# Initial price
discount_price = 1500
print("Before update (sale price):", discount_price)

# Sale ended -> original price
original_price = 2000

# Reassigning discount_price to original_price using the assignment operator (=)
discount_price = original_price

print("After update (sale ended):", discount_price)

"""
EXPLANATION:
Variables in Python are "mutable" in the sense that you can reassign
them to a new value at any time using the '=' operator. The old value
(1500) is simply discarded/overwritten, and 'discount_price' now points
to the same value as 'original_price' (2000). This is normal reassignment,
not a special "mutability" feature of the object itself (ints are actually
immutable) -- it's the *variable name* that gets re-bound to a new value.
"""
