"""
Smart Home Light (Methods) - SIMPLE

Ek SmartBulb class banayein jismein ek attribute state = "OFF" ho.
Isme ek method turn_on() banayein jo state ko "ON" kar de.
"""

class SmartBulb:
    def __init__(self):
        self.state = "OFF"   # every bulb starts off

    def turn_on(self):
        self.state = "ON"


bulb = SmartBulb()
print("Before:", bulb.state)

bulb.turn_on()
print("After: ", bulb.state)

"""
EXPLANATION:
- self.state = "OFF" is set inside the constructor, so every new
  SmartBulb object starts in the "OFF" state by default.
- turn_on(self) is a METHOD -- a function defined inside the class
  that operates on a specific object's data. Calling bulb.turn_on()
  changes THAT bulb's own 'state' attribute to "ON", using self to
  refer to the exact object the method was called on.
- This demonstrates how methods can MODIFY an object's own attributes
  after it's already been created.
"""
