"""
E-Commerce Product Registry (Class & Object) - SIMPLE

Ek online store ke liye Product class banayein jismein name aur
price ke default attributes hon. Is class ke do objects (e.g.,
Laptop aur Smartphone) instantiate karein aur dono ki details print
karein.
"""

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


# Creating (instantiating) two separate objects from the same class
laptop = Product("Laptop", 150000)
smartphone = Product("Smartphone", 85000)

print(f"Product: {laptop.name}, Price: {laptop.price}")
print(f"Product: {smartphone.name}, Price: {smartphone.price}")

"""
EXPLANATION:
- 'class Product:' defines the BLUEPRINT for what a product looks like
  (it has a name and a price).
- __init__ is the constructor -- it runs automatically every time a
  new object is created, and sets up that object's own name and price
  based on whatever arguments are passed in.
- laptop = Product("Laptop", 150000) creates one INSTANCE (object) of
  the Product class, and smartphone = Product(...) creates a
  completely separate, independent instance -- each with its own name
  and price, even though both come from the same class definition.
"""
