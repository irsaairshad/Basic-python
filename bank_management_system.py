class BankAccount:
    __total_accounts = 0

    def __init__(self, owner, initial_deposit):
        self.owner = owner
        self.__balance = 0
        self.__account_no = f"ACC-{1000 + BankAccount.__total_accounts + 1}"
        BankAccount.__total_accounts += 1
        self.set_deposit(initial_deposit)

    def get_balance(self):
        return self.__balance

    def get_account_no(self):
        return self.__account_no

    def set_deposit(self, amount):
        if not isinstance(amount, (int, float)) or isinstance(amount, bool) or amount <= 0:
            print("Invalid Transaction Type")
            return
        self.__balance += amount

    def deposit(self, amount):
        self.set_deposit(amount)

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)) or isinstance(amount, bool) or amount <= 0:
            print("Invalid Transaction Type")
            return
        if amount > self.__balance:
            print("Transaction Declined")
            return
        self.__balance -= amount

    @classmethod
    def get_total_accounts(cls):
        return cls.__total_accounts


if __name__ == "__main__":
    acc1 = BankAccount("Irsa", 5000)
    acc2 = BankAccount("Ahmad", 2000)

    acc1.deposit(1000)
    acc1.set_deposit(-500)
    acc1.set_deposit("cash")

    acc1.withdraw(2000)
    acc1.withdraw(100000)

    print("Balance:", acc1.get_balance())
    print("Account No:", acc1.get_account_no())
    print("Total accounts:", BankAccount.get_total_accounts())
