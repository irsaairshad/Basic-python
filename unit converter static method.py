"""
Unit Converter (Static Method) - STATIC KEYWORDS

Ek cloud backend script mein aapko Fahrenheit se Celsius temperature
convert karne ke liye ek tool chahiye jise chalane ke liye kisi object
(self) ki zaroorat nahi hai. @staticmethod decorator ka use karke is
conversion method ka basic structure banayein.
"""

class TemperatureConverter:

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        # Notice: NO 'self' parameter here at all -- a static method
        # doesn't need an object/instance to operate.
        celsius = (fahrenheit - 32) * 5 / 9
        return celsius


# Called directly on the CLASS -- no object needs to be created first!
result = TemperatureConverter.fahrenheit_to_celsius(98.6)
print(f"98.6°F = {result:.2f}°C")

"""
EXPLANATION:
- @staticmethod is a decorator that tells Python "this method doesn't
  need access to the object (self) or the class itself -- it just
  behaves like a regular, standalone function that happens to live
  inside a class for organizational purposes".
- Because there's no 'self' parameter, you can call it directly on the
  CLASS NAME (TemperatureConverter.fahrenheit_to_celsius(98.6)) without
  ever creating an object/instance first -- which matches "kisi object
  ki zaroorat nahi hai" from the question.
- This is ideal for utility/helper functions (like unit conversions,
  math calculations, or validation checks) that don't need to read or
  modify any instance-specific data.
"""
