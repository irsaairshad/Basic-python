"""
Server Price Revision (Mutability) - LISTS

Ek hosting provider ki package price list hai. Inflation ki sababu se
dusre product (index 1) ki price ko update karke 1800 karna hai. List
ke mutability behavior ka faida uthate hue price update karein aur
updated list print karein.
"""

prices = [1200, 1500, 2000, 2500]   # example hosting package prices

print("Before update:", prices)

# Lists are MUTABLE, meaning we can change an individual element
# in-place using its index, without creating a whole new list.
prices[1] = 1800   # index 1 = the second item ("dusre product")

print("After update: ", prices)

"""
EXPLANATION:
- Indexing starts at 0 in Python, so "the second product" is at
  index 1 (index 0 is the first, index 1 is the second, and so on).
- Because lists are MUTABLE (unlike tuples or strings), we can directly
  reassign a value at a specific index using prices[1] = 1800, and it
  updates that one slot in the SAME list object -- we don't need to
  rebuild the whole list from scratch.
- This is the key difference lists have over tuples, which will come up
  again in Section C (Question 13), where tuples do NOT allow this.
"""
