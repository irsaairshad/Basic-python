class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if not isinstance(amount, (int, float)) or isinstance(amount, bool):
            raise TypeError("Balance must be a numeric value (int or float).")
        if amount < 0:
            raise ValueError("Balance cannot be negative.")
        self.__balance = amount


if __name__ == "__main__":
    account = BankAccount()
    account.set_balance(15000)
    print(account.get_balance())

    try:
        account.set_balance("ten thousand")
    except TypeError as e:
        print(e)

    try:
        account.set_balance(-500)
    except ValueError as e:
        print(e)
