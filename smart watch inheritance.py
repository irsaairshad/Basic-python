"""
Smart Watch OS (Basic Inheritance) - RELATIONSHIPS

Ek parent class Watch jismein show_time() method likha hai. Ek child
class SmartWatch jo Watch se inherit karti hai. Bina kisi extra code
ke, SmartWatch ka object parent ke show_time() method ko kaise call
karega?
"""

class Watch:
    def show_time(self):
        print("Displaying time: 10:30 AM")


class SmartWatch(Watch):   # SmartWatch INHERITS from Watch
    pass   # no extra code needed at all -- it automatically gets everything from Watch


my_smartwatch = SmartWatch()

# Calling show_time() directly on the child object -- it works even
# though SmartWatch itself never defined this method!
my_smartwatch.show_time()

"""
ANSWER / EXPLANATION:
class SmartWatch(Watch): -- putting Watch inside the parentheses makes
SmartWatch a CHILD (subclass) of the PARENT class Watch. This means
SmartWatch automatically INHERITS every method and attribute that
Watch has, without needing to rewrite or redefine any of that code.

So my_smartwatch.show_time() works perfectly, EVEN THOUGH SmartWatch's
own class body is empty (just 'pass') -- Python looks at the
SmartWatch object, doesn't find show_time() defined directly there,
then automatically checks its PARENT class (Watch), finds it there,
and runs that version.

This is the core benefit of inheritance: shared, reusable behavior
defined once in a parent class, automatically available to any number
of child classes "for free," with zero extra code required.
"""
