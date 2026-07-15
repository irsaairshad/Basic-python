"""
Automated Marks Grading - CONDITIONALS

Ek school portal ke liye automatic grading program banayein jo
student ke exam marks (0 to 100) input le. Agar marks 90 ya usse
zyada hon to "Grade A", agar 80 se 89 ke darmiyan hon to "Grade B",
aur baqi tamam marks par "Grade C" print kare.
"""

marks = float(input("Enter student's marks (0-100): "))

if marks >= 90:
    print("Grade A")
elif marks >= 80:   # this only runs if marks < 90, so it effectively covers 80-89
    print("Grade B")
else:
    print("Grade C")

"""
EXPLANATION:
- input() returns a string, so we convert it to a number with float()
  before comparing it with >= (typecasting, as covered in Chapter 1).
- Notice the elif marks >= 80 does NOT need "80 <= marks <= 89" written
  out, because by the time Python reaches this line, it has already
  confirmed marks is NOT >= 90 (that's how if/elif chains work -- each
  condition is only checked if the ones above it were False). So
  "elif marks >= 80" correctly captures the 80-89 range.
- 'else' catches everything else (0-79), printing "Grade C".
"""
