"""
Food Delivery App (Aggregation) - RELATIONSHIPS

Ek food delivery app mein class Restaurant hai aur dusri class Menu
hai. In dono ke darmiyan "Has-A" relationship hai. Agar hum
Restaurant ka object banate waqt Menu ka object as an input parameter
pass karein, toh code mein is setup ko kya kehte hain?
"""

class Menu:
    def __init__(self, items):
        self.items = items   # e.g. a list of dishes

    def show_items(self):
        print("Menu items:", ", ".join(self.items))


class Restaurant:
    def __init__(self, name, menu):
        self.name = name
        self.menu = menu   # storing a Menu OBJECT inside the Restaurant object


# Create the Menu object FIRST, independently
burger_menu = Menu(["Burger", "Fries", "Cold Drink"])

# Then pass that existing Menu object INTO the Restaurant's constructor
restaurant = Restaurant("Fast Bites", burger_menu)

print(f"Welcome to {restaurant.name}!")
restaurant.menu.show_items()

"""
ANSWER: This setup is called AGGREGATION.

EXPLANATION:
- Aggregation is a "Has-A" relationship where one class (Restaurant)
  HOLDS/USES an object of another class (Menu), but that Menu object
  is created INDEPENDENTLY, outside of the Restaurant, and simply
  PASSED IN as a parameter (rather than being created from scratch
  inside Restaurant's own constructor).
- This means the Menu object can exist on its own, separately from any
  particular Restaurant, and could even be shared/reused by multiple
  restaurants -- the two objects have a looser, more flexible
  relationship than if Restaurant had built its OWN internal Menu
  object completely from scratch (which would be a stronger form of
  "Has-A" called Composition, where the child object's lifetime is
  tightly tied to the parent).
- In short: Aggregation = "Restaurant HAS-A Menu, but the Menu can
  exist independently of any specific Restaurant."
"""
