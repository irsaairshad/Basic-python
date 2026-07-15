"""
E-Commerce Discount Voucher - CONDITIONALS

Ek shopping website ke checkout button par logic lagayein. User se
total cart value input lein. Agar cart value 5000 PKR se zyada hai
to total bill par 10% discount apply kar ke discounted total print
karein, warna print karein "No discount applicable".
"""

cart_value = float(input("Enter total cart value (PKR): "))

if cart_value > 5000:
    discount = cart_value * 0.10           # 10% of the cart value
    discounted_total = cart_value - discount
    print(f"10% discount applied! Discounted total: {discounted_total:.2f} PKR")
else:
    print("No discount applicable")

"""
EXPLANATION:
- "5000 PKR se zyada" means strictly greater than 5000, so we use the
  '>' operator (not >=) -- a cart of exactly 5000 would NOT qualify.
- To apply a 10% discount: multiply the cart value by 0.10 to get the
  discount amount, then subtract that from the original cart value to
  get the final discounted total.
- The f-string {discounted_total:.2f} formats the result to 2 decimal
  places, which is standard for displaying currency amounts.
"""
