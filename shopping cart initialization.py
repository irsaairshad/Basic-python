"""
Question 03: Shopping Cart Initialization - SIMPLE

Ek khali (empty) list banayein cart. Phir .append() method ka
istemal karte hue usme "Milk", "Eggs", aur "Bread" add karein.
"""

cart = []   # empty list

cart.append("Milk")
cart.append("Eggs")
cart.append("Bread")

print("Shopping cart:", cart)

"""
EXPLANATION:
- cart = [] creates an empty list with no items in it yet.
- .append(item) adds ONE item to the END of the list at a time. Calling
  it three times in sequence builds up the cart in the exact order the
  items were added: Milk first, then Eggs, then Bread.
- Final result: cart = ["Milk", "Eggs", "Bread"]
"""
