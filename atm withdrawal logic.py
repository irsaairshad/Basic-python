"""
ATM Withdrawal Logic - HARD

Ek balance = 10000 set karein. Ek while loop banayein jo user se baar
baar withdrawal amount pooche. Agar amount balance se zyada hai,
"Insufficient" print karein. Agar amount balance ke barabar ho jaye,
balance 0 kar dein aur break statement ka istemal kar ke loop foran
rok dein.
"""

balance = 10000

while True:   # loop keeps going until we explicitly 'break' out of it
    amount = float(input("Enter amount to withdraw: "))

    if amount > balance:
        print("Insufficient")
    elif amount == balance:
        balance = 0
        print("Withdrawal successful. Balance is now 0.")
        break   # exit the loop immediately, since the account is now empty
    else:
        balance -= amount
        print(f"Withdrawal successful. Remaining balance: {balance}")

print("Final balance:", balance)

"""
EXPLANATION:
- while True: creates a loop that would normally run FOREVER, since
  its condition (True) never becomes False on its own -- the only way
  out is an explicit 'break' statement somewhere inside it.
- Each pass asks the user for a withdrawal amount and checks three
  cases:
    1. amount > balance -> not enough money, print "Insufficient" and
       loop again (no change to balance).
    2. amount == balance -> withdrawing EXACTLY what's left, so we set
       balance = 0 and then 'break' to stop the loop right away, since
       there's nothing left to withdraw.
    3. otherwise (amount < balance) -> a normal partial withdrawal,
       balance -= amount deducts it, and the loop continues asking for
       more withdrawals.
- 'break' immediately exits the ENTIRE while loop, skipping any
  remaining code inside it and jumping to the first line after the
  loop.
"""
