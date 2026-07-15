"""
Automated Grade Calculator - INTERMEDIATE

Ek function calculate_grade(marks) banayein jo marks check kar ke
return kare: >90 pe "A", >80 pe "B", aur baki pe "C".
"""

def calculate_grade(marks):
    if marks > 90:
        return "A"
    elif marks > 80:
        return "B"
    else:
        return "C"

# Testing the function with a few different values
print("Marks 95 ->", calculate_grade(95))
print("Marks 85 ->", calculate_grade(85))
print("Marks 60 ->", calculate_grade(60))

"""
EXPLANATION:
- The function calculate_grade(marks) takes one parameter, 'marks',
  and uses 'return' to send a value (the grade letter) BACK to
  whatever code called the function -- unlike print(), which just
  displays something, return actually hands the value back so it can
  be stored, printed, or used elsewhere.
- Only ONE branch of the if/elif/else ever runs per call, and 'return'
  immediately exits the function with that value the moment a matching
  condition is found.
- marks > 90 -> "A", marks > 80 (but not > 90) -> "B", anything else
  -> "C".
"""
