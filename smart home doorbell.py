"""
Question 02: Smart Home Doorbell - SIMPLE

Ek variable banayein time. Agar time 10 (baje) ke baad ka hai, toh
if-else ka use karke "Silent Mode On" print karein, warna "Ring Loud"
print karein.
"""

time = 22   # example: 24-hour format, so 22 means 10 PM

if time > 10:
    print("Silent Mode On")
else:
    print("Ring Loud")

"""
EXPLANATION:
- We compare the variable 'time' against 10 using the '>' operator.
- If time > 10 is True (meaning it's after 10 o'clock), the doorbell
  goes silent; otherwise (10 or earlier), it rings loudly.
- Note: in a real smart home system you'd likely use 24-hour format
  and also check for early morning hours (e.g. time > 22 or time < 7),
  but this solution follows the question exactly as it's phrased --
  a simple single-condition check against 10.
"""
