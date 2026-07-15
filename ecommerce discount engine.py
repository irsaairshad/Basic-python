"""
E-Commerce Discount Engine - HARD

Ek list mein cart items ki prices di gayi hain. Ek for loop chalayein.
Agar price 100 se upar hai, toh us par 10% discount apply kar ke
print karein. Agar koi price 0 aati hai (jaise free item), toh
continue use kar ke us iteration ko skip kar dein.
"""

cart_prices = [250, 0, 80, 500, 0, 120]

for price in cart_prices:
    if price == 0:
        continue   # skip free items entirely -- nothing to discount or print

    if price > 100:
        discounted_price = price - (price * 0.10)
        print(f"Original: {price} -> After 10% discount: {discounted_price}")
    else:
        print(f"Price {price} -- no discount applicable (100 or below)")

"""
EXPLANATION:
- The for loop goes through each price in the cart, one at a time.
- 'if price == 0: continue' immediately skips to the NEXT item in the
  list whenever a free item (price 0) is found -- no discount logic or
  print statement runs for that particular item at all.
- For all other (non-zero) prices, we check if price > 100:
    - If yes, apply a 10% discount: price - (price * 0.10), and print
      both the original and discounted price.
    - If no (100 or below, but not 0), print that no discount applies.
- This models a realistic e-commerce cart: free promotional items are
  ignored entirely, low-cost items get no discount, and higher-value
  items automatically receive 10% off.
"""
