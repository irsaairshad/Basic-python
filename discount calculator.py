"""
Discount Calculator - SIMPLE

User se product ki price input lein, usay int mein typecast karein,
aur 10% discount minus kar ke final price print karein.
"""

price = int(input("Enter product price: "))   # input() returns a string, so we typecast it to int

discount = price * 0.10          # 10% of the price
final_price = price - discount   # subtract the discount from the original price

print(f"Original price: {price}")
print(f"Discount (10%): {discount}")
print(f"Final price after discount: {final_price}")

"""
EXPLANATION:
- input() always returns a STRING, even if the user types digits like
  "1000". Wrapping it with int() converts ("typecasts") that string
  into a whole number we can actually do math with.
- 10% of the price is calculated as price * 0.10.
- The final price is the original price minus that discount amount:
  final_price = price - discount.
- Note: since discount involves multiplying by 0.10 (a float), the
  result (discount and final_price) will be a float (decimal number),
  even though 'price' itself was typecast to int -- this is normal in
  Python, since int * float always produces a float.
"""
