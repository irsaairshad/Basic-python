"""
Online Grocery Invoice (Operator Overloading) - POLYMORPHISM

Aapke paas shopping cart ke do objects hain: cart1 aur cart2. Aap
chahte hain ke jab bhi code mein cart1 + cart2 likha jaye, toh dono
carts ke total bills aapas mein add ho jayein. Python mein is
operator behavior ko custom dunder method __add__ ke zariye kaise
control karenge?
"""

class Cart:
    def __init__(self, total_bill):
        self.total_bill = total_bill

    def __add__(self, other):
        # 'self' is the LEFT-hand cart (cart1), 'other' is the
        # RIGHT-hand cart (cart2) in the expression cart1 + cart2.
        combined_total = self.total_bill + other.total_bill
        return Cart(combined_total)   # return a NEW Cart with the combined total


cart1 = Cart(1500)
cart2 = Cart(2300)

combined_cart = cart1 + cart2   # this line triggers our custom __add__ method!

print("Cart 1 total:", cart1.total_bill)
print("Cart 2 total:", cart2.total_bill)
print("Combined cart total:", combined_cart.total_bill)

"""
EXPLANATION:
- __add__ is a "dunder" (double underscore) method that Python calls
  automatically whenever the '+' operator is used between two objects
  of that class. Writing cart1 + cart2 is essentially shorthand for
  Python internally calling cart1.__add__(cart2).
- Inside __add__(self, other): 'self' refers to the object on the LEFT
  of the '+' (cart1), and 'other' refers to the object on the RIGHT
  (cart2).
- We add their total_bill values together and return a brand NEW Cart
  object holding that combined total -- so combined_cart is a fresh
  Cart, separate from cart1 and cart2, with total_bill = 3800.
- This is called OPERATOR OVERLOADING: giving a standard operator
  (like +) custom, class-specific behavior instead of its normal
  numeric/string meaning.
"""
