"""
Question 05: Security Login Lockout - SIMPLE

Ek while loop ka istemal karein jo 1 se 3 tak "Login Attempt X"
print kare taake 3 attempts ke baad system lock hone ka logic
banaya ja sake.
"""

attempt = 1

while attempt <= 3:
    print(f"Login Attempt {attempt}")
    attempt += 1   # increase the counter each time, or the loop never ends

print("3 attempts used. System is now locked.")

"""
EXPLANATION:
- A while loop keeps repeating its block of code AS LONG AS its
  condition stays True. Here, the condition is "attempt <= 3".
- We start attempt at 1, print "Login Attempt 1", then increase
  attempt by 1 (attempt += 1, same as attempt = attempt + 1) each time
  through the loop -- this is called the "increment" step.
- The loop runs for attempt = 1, 2, 3 (three times total), and stops
  as soon as attempt becomes 4, since 4 <= 3 is False.
- Forgetting the increment step (attempt += 1) is a classic beginner
  mistake that causes an "infinite loop" -- since attempt would always
  stay at 1, the condition would never become False.
"""
