"""
Weather Station (Read-Only Getter) - ENCAPSULATION

Ek IoT weather monitoring system mein __temperature ki value ko
system ke bahar display karna hai, lekin use koi change na kar sake.
Is temperature ko safe tarike se print karne ke liye getter method
get_temperature() kaise likhenge?
"""

class WeatherStation:
    def __init__(self, temperature):
        self.__temperature = temperature   # private -- no direct outside access

    def get_temperature(self):
        # A getter ONLY returns the value -- it never accepts a
        # parameter to change it, so external code can read but not write.
        return self.__temperature


station = WeatherStation(28.5)

print("Current temperature:", station.get_temperature(), "°C")

# There is no set_temperature() method provided at all, so outside
# code has NO way to modify __temperature -- it's genuinely read-only.

"""
EXPLANATION:
- A "getter" method's job is simply to RETURN a private attribute's
  value, without providing any way to modify it.
- get_temperature(self) takes no extra parameters (besides 'self'),
  so it cannot be used to assign a new value -- it can only ever hand
  back whatever __temperature currently holds.
- Because we deliberately do NOT define a matching "setter" method
  (like set_temperature()), external code has no legitimate way to
  change the value at all -- making this attribute effectively
  read-only from outside the class.
"""
