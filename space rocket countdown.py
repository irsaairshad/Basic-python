"""
Space Rocket Countdown - INTERMEDIATE

Ek while loop banayein jo user se number le aur wahan se 0 tak ulta
(reverse) count down print kare.
"""

count = int(input("Enter the countdown starting number: "))

while count >= 0:
    print(count)
    count -= 1   # decrease by 1 each time (reverse counting)

print("Liftoff!")

"""
EXPLANATION:
- We take the starting number from the user and typecast it to int
  (since input() always returns a string).
- The while loop keeps running AS LONG AS count >= 0 stays True,
  printing the current value of 'count' each time.
- count -= 1 (short for count = count - 1) decreases the number by one
  on every pass, moving it toward 0 -- this is what makes it a REVERSE
  countdown, as opposed to counting upward.
- The loop naturally stops once count becomes -1, since -1 >= 0 is
  False, and then "Liftoff!" prints once, after the loop ends.
"""
