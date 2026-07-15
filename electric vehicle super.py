"""
Electric Vehicle Upgrade (super() Constructor) - RELATIONSHIPS

ElectricCar (child class) ka apna constructor __init__ hai, jiski
wajah se parent class Vehicle ke variables automatic initialize nahi
ho rahe. Parent ke variables ko force-initialize karne ke liye child
constructor ke andar super() keyword kaise use karenge?
"""

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class ElectricCar(Vehicle):
    def __init__(self, brand, model, battery_capacity):
        # super() gives us access to the PARENT class (Vehicle), so we
        # can call ITS __init__ directly and let it set up 'brand' and
        # 'model' exactly as it normally would.
        super().__init__(brand, model)

        # Now handle the CHILD class's own extra attribute:
        self.battery_capacity = battery_capacity


my_car = ElectricCar("Tesla", "Model 3", "75 kWh")

print("Brand:", my_car.brand)
print("Model:", my_car.model)
print("Battery Capacity:", my_car.battery_capacity)

"""
EXPLANATION:
- When a child class (ElectricCar) defines its OWN __init__ method,
  Python does NOT automatically run the parent class's __init__
  anymore -- the child's constructor completely overrides/replaces it,
  UNLESS we explicitly tell Python to also run the parent's version.
- super().__init__(brand, model) calls Vehicle's original __init__
  method, passing along 'brand' and 'model', so Vehicle can set up
  self.brand and self.model exactly like it would for any plain
  Vehicle object.
- After that line runs, we continue the CHILD's constructor to set up
  its own ADDITIONAL attribute (battery_capacity), which only
  ElectricCar objects need.
- This lets us reuse the parent's setup logic instead of duplicating
  "self.brand = brand" and "self.model = model" all over again inside
  ElectricCar.
"""
