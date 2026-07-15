"""
Unique Employee ID (Static/Class Variable Counter) - STATIC KEYWORDS

Aapke HR system mein jab bhi naya employee register ho, use
auto-incremented ID (jaise 101, 102, 103) milni chahiye. Constructor
ke andar class variable ko update karke unique identity dynamic
tarike se kaise assign karenge?
"""

class Employee:
    next_id = 101   # CLASS variable -- acts as the starting point / running counter

    def __init__(self, name):
        self.name = name
        self.employee_id = Employee.next_id   # assign the current counter value to THIS employee
        Employee.next_id += 1                  # then bump the shared counter for the NEXT employee


emp1 = Employee("Hina")
emp2 = Employee("Usman")
emp3 = Employee("Noor")

print(f"{emp1.name} -> ID {emp1.employee_id}")
print(f"{emp2.name} -> ID {emp2.employee_id}")
print(f"{emp3.name} -> ID {emp3.employee_id}")

"""
EXPLANATION:
- Employee.next_id is a CLASS variable, shared by every Employee
  object, and it acts as a running counter starting at 101.
- Every time a NEW Employee object is created, the constructor:
    1. Assigns the employee's OWN employee_id (an instance variable)
       to whatever Employee.next_id currently is.
    2. THEN increases the shared class variable Employee.next_id by 1,
       so the NEXT employee created will automatically get a fresh,
       higher ID.
- This gives each employee a permanently fixed, unique ID (101, 102,
  103, ...) the moment they're created, while the shared counter keeps
  advancing for whoever registers next.
"""
