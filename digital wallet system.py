"""
Digital Wallet System (Default Constructor) - SIMPLE

Ek Wallet class banayein. Jab bhi naya wallet object bane, __init__
constructor automatically chalna chahiye aur starting balance 0 set
karna chahiye.
"""

class Wallet:
    def __init__(self):
        self.balance = 0   # every new wallet automatically starts at 0
        print("New wallet created with starting balance: 0")


my_wallet = Wallet()

print("Current balance:", my_wallet.balance)

"""
EXPLANATION:
- __init__ is called the CONSTRUCTOR -- Python runs this method
  AUTOMATICALLY the moment a new object is created (my_wallet =
  Wallet()), without needing to call it manually.
- Since __init__ here takes no extra parameters (besides 'self'),
  every single Wallet object created this way will always start with
  self.balance = 0, no matter how many wallets you create.
- This models a real digital wallet: as soon as an account is opened,
  it automatically starts empty, at zero balance.
"""
