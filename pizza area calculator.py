"""
Question 07: Pizza Area Calculator (Formula Assignment) - ADVANCED-INTERMEDIATE

Ek online pizza delivery app ke liye, user se pizza ka diameter input
lein. Is diameter ka use karte hue pizza ka total area calculate karein:

    Area = 3.14 * (diameter / 2) ** 2

User se input lete waqt typecasting ka khyal rakhein kyunki input
hamesha string return karta hai.
"""

# input() ALWAYS returns a string, even if the user types a number.
# So we must convert ("typecast") it to a float before doing math with it.
diameter = float(input("Enter the pizza's diameter (in inches/cm): "))

radius = diameter / 2
area = 3.14 * (radius ** 2)

print(f"The pizza's total area is: {area:.2f} square units")

"""
EXPLANATION:
- input() collects whatever the user types as a STRING (str), no matter
  if they typed "12" or "12.5". If we tried diameter / 2 directly on
  the raw string, Python would raise a TypeError, because you can't
  divide a string by an int.
- Typecasting with float() converts that string into a decimal number
  we can actually do arithmetic on. (int() would also work if you only
  expect whole numbers, but float() is safer since diameters can be
  decimals like 12.5.)
- Formula breakdown:
    radius = diameter / 2
    area   = 3.14 * radius**2      (i.e. pi * r^2)
- The f-string {area:.2f} rounds the output to 2 decimal places for a
  clean, readable result (e.g. 113.04 instead of 113.03999999999999).
"""
