"""
Smart Door Lock (Validation Setter) - ENCAPSULATION

Aap ek smart home lock system bana rahe hain jahan passcode __pin
private hai. Ek aisa setter method set_pin(new_pin) likhein jo check
kare ke agar new_pin sirf numbers (digits) par mabni hai tabhi
update kare, warna error message de.
"""

class SmartLock:
    def __init__(self, pin):
        self.__pin = pin

    def set_pin(self, new_pin):
        if new_pin.isdigit():          # True only if every character is a digit
            self.__pin = new_pin
            print("PIN updated successfully.")
        else:
            print("Error: PIN must contain digits only.")

    def get_pin(self):
        return self.__pin


lock = SmartLock("1234")

lock.set_pin("5678")          # valid -- should update
print("Current PIN:", lock.get_pin())

lock.set_pin("12ab")          # invalid -- should be rejected
print("Current PIN (unchanged):", lock.get_pin())

"""
EXPLANATION:
- A "setter" is a method whose whole purpose is to control HOW an
  attribute gets updated, instead of allowing direct, unchecked
  assignment.
- new_pin.isdigit() is a built-in string method that returns True only
  if every character in the string is a numeric digit (0-9) and the
  string isn't empty.
- If the check passes, we update the private __pin attribute inside
  the class; if it fails, we reject the change and print an error
  message instead -- this way, invalid data (like letters) can never
  get into __pin, no matter what gets passed to set_pin().
"""
