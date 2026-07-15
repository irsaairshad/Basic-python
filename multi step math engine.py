"""
Multi-Step Math Engine - HARD

Ek function banayein jo ek parameter n le. Function ke andar (local
variables use karte hue) ek while loop chalayein jo 1 se lekar n tak
tamam natural numbers ko aapas mein plus (sum) kare aur aakhir mein
total sum return kare.
"""

def sum_up_to_n(n):
    total = 0     # local variable -- only exists inside this function
    counter = 1   # local variable -- used to track the current number

    while counter <= n:
        total += counter   # add the current number to the running total
        counter += 1        # move on to the next number

    return total


result = sum_up_to_n(10)
print("Sum of numbers from 1 to 10:", result)

result2 = sum_up_to_n(5)
print("Sum of numbers from 1 to 5:", result2)

"""
EXPLANATION:
- 'total' and 'counter' are LOCAL VARIABLES -- they are created fresh
  each time the function runs, exist only inside sum_up_to_n(), and
  disappear once the function finishes. They cannot be accessed from
  outside the function.
- The while loop starts counter at 1 and keeps adding it to 'total',
  then increases counter by 1 each pass, continuing AS LONG AS
  counter <= n. This adds up every whole number from 1 through n.
- 'return total' sends the final accumulated sum back to wherever the
  function was called, so it can be stored (as 'result') or printed.
- Example: sum_up_to_n(10) computes 1+2+3+4+5+6+7+8+9+10 = 55.
"""
