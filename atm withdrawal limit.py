"""
QATM Cash Withdrawal Limit - CONDITIONALS

Ek ATM transaction check system likhein jahan user ka current
balance balance = 15000 set ho. User se withdraw hone wala amount
input lein. Agar amount balance ke barabar ya usse kam hai, to
balance se deduct karke updated balance dikhayein, warna
"Insufficient Funds" print karein.
"""

balance = 15000

withdraw_amount = float(input("Enter amount to withdraw: "))

if withdraw_amount <= balance:
    balance = balance - withdraw_amount   # deduct the withdrawn amount
    print("Withdrawal successful. Updated balance:", balance)
else:
    print("Insufficient Funds")

"""
EXPLANATION:
- The condition "amount balance ke barabar ya usse kam" translates to
  withdraw_amount <= balance (less than OR equal to).
- If that condition is True, we update 'balance' by subtracting the
  withdrawn amount (balance = balance - withdraw_amount), which is the
  same idea as Question 1 from Chapter 1 (reassigning a variable to a
  new computed value).
- If the condition is False (i.e. the user tries to withdraw MORE than
  they have), the else branch runs and denies the transaction with
  "Insufficient Funds", leaving the original balance untouched.
"""
