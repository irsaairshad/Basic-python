"""
Portal Voting Eligibility - CONDITIONALS

Ek government portal par user check karna chahta hai ke kya woh
vote de sakta hai. User ki age input lein. Agar age 18 ya usse
barhi hai to "You are eligible to vote" print karein, warna
"You are not eligible to vote" print karein.
"""

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

"""
EXPLANATION:
- A simple two-way decision only needs 'if' and 'else' (no 'elif'
  required), since there are only two possible outcomes.
- age is converted to an integer with int() because input() always
  returns a string, and we need to compare it numerically with >=.
- The condition age >= 18 means "18 or older", exactly matching the
  requirement "18 ya usse barhi".
"""
