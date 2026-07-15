"""
Traffic Light Controller - INTERMEDIATE

Ek if-elif-else block banayein jo user input ("Red", "Yellow",
"Green") ke mutabiq instructions print kare: Red par "Stop", Yellow
par "Slow Down", Green par "Go".
"""

light = input("Enter the traffic light color (Red/Yellow/Green): ")

if light == "Red":
    print("Stop")
elif light == "Yellow":
    print("Slow Down")
elif light == "Green":
    print("Go")
else:
    print("Invalid color entered.")

"""
EXPLANATION:
- if/elif/else checks each condition in order, running only the FIRST
  block whose condition is True, then skipping the rest.
- Comparing with '==' checks for an exact match against the string the
  user typed.
- The 'else' branch is added as good practice, to gracefully handle
  any unexpected input that isn't Red, Yellow, or Green.
"""
