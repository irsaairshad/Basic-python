"""
Smart Traffic Control System - CONDITIONALS

Ek traffic signal automation script likhein jo user se light ka
current color ("Red", "Yellow", "Green") as input le. Agar light
"Red" ho to "Stop your vehicle", agar "Yellow" ho to "Slow Down",
aur agar "Green" ho to "Go" print kare.
"""

light = input("Enter the current traffic light color (Red/Yellow/Green): ")

if light == "Red":
    print("Stop your vehicle")
elif light == "Yellow":
    print("Slow Down")
elif light == "Green":
    print("Go")
else:
    print("Invalid input. Please enter Red, Yellow, or Green.")

"""
EXPLANATION:
- if / elif / else lets the program check MULTIPLE conditions in order,
  running only the first block whose condition is True.
- Here we compare the string exactly ("Red", "Yellow", "Green") using
  the '==' operator.
- An extra 'else' branch was added as good practice, to handle any
  unexpected input (e.g. if the user types "red" in lowercase or
  misspells it) rather than silently doing nothing.
"""
