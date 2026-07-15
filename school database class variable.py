"""
School Database (Class vs Instance Variable) - STATIC KEYWORDS

Aapko ek school management portal design karna hai. Portal mein har
student ka apna name aur roll_number hai, lekin sab ka
school_name = "Future Academy" bilkul same hai. Memory bachaane ke
liye aap school_name ko class ke andar kahan aur kis variable ke tor
par define karenge?
"""

class Student:
    # CLASS VARIABLE -- defined directly inside the class body, OUTSIDE
    # any method. Shared by ALL instances/objects of this class.
    school_name = "Future Academy"

    def __init__(self, name, roll_number):
        # INSTANCE VARIABLES -- defined inside __init__ using self.
        # Each object gets its OWN separate copy of these.
        self.name = name
        self.roll_number = roll_number


student1 = Student("Ayesha", "FA23-BCS-001")
student2 = Student("Bilal", "FA23-BCS-002")

print(student1.name, student1.roll_number, student1.school_name)
print(student2.name, student2.roll_number, student2.school_name)

"""
ANSWER / EXPLANATION:
school_name should be defined as a CLASS VARIABLE -- written directly
inside the class body (Student), but OUTSIDE of __init__ or any other
method.

WHY: A class variable is shared by ALL objects created from that
class -- there's only ONE copy of it in memory, no matter how many
students you create. Since every student genuinely has the exact same
school_name ("Future Academy"), storing it as an INSTANCE variable
(self.school_name = "Future Academy" inside __init__) would waste
memory by duplicating the identical string separately for every single
student object.

In contrast, 'name' and 'roll_number' are different for each student,
so they correctly belong as INSTANCE variables (created fresh, per
object, using self. inside __init__).
"""
