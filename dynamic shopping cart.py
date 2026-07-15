"""
Dynamic Shopping Cart - LISTS

Ek e-commerce application ke liye empty list cart = [] banayein.
List operations ka istemal karte hue usmein sequentially teen items
("Eggs", "Milk", "Bread") add karein. Aakhir mein list ka total size
built-in function ke zariye print karein.
"""

cart = []   # start with an empty list

# .append() adds one item at a time to the END of the list
cart.append("Eggs")
cart.append("Milk")
cart.append("Bread")

print("Cart contents:", cart)

# len() is the built-in function used to get the total number of
# items currently in a list
print("Total items in cart:", len(cart))

"""
EXPLANATION:
- A list is created empty with square brackets: cart = [].
- The .append(item) method adds a single item to the end of the list,
  one at a time -- calling it 3 times in sequence builds up the cart
  step by step, in the order the items were added.
- len(cart) is Python's built-in function for counting the number of
  elements in any list (or string, tuple, dict, etc.), so len(cart)
  returns 3 here.
"""
