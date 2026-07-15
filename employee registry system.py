"""
Employee Registry System - HARD

Ek khali dictionary employees = {} banayein. for loop aur range(3)
ka istemal karte hue user se 3 dafa employee ka name aur salary
input lein. Name ko Key aur Salary ko Value bana kar dictionary mein
add karein aur aakhir mein print karein.
"""

employees = {}   # empty dictionary to start

for i in range(3):
    name = input(f"Enter name for employee {i + 1}: ")
    salary = input(f"Enter salary for {name}: ")
    employees[name] = salary   # name becomes the KEY, salary becomes the VALUE

print("\nEmployee Registry:", employees)

"""
EXPLANATION:
- employees = {} starts as a completely empty dictionary.
- range(3) makes the for loop run exactly 3 times (i = 0, 1, 2), once
  for each employee we need to register.
- Inside the loop, we collect a name and salary from the user each
  time, then use employees[name] = salary to add a NEW key-value pair
  to the dictionary -- the employee's name becomes the dictionary KEY,
  and their salary becomes the corresponding VALUE.
- By the time the loop finishes, 'employees' holds all 3 entries
  together, e.g. {"Ali": "50000", "Sara": "62000", "Zain": "48000"}.
"""
