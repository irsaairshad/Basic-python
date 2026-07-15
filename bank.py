"""
BANK MANAGEMENT SYSTEM
-----------------------
A complete console-based Bank Management System built WITHOUT using OOP
(no classes, no objects). Everything is implemented using plain functions
and built-in data structures (dictionaries, lists), with data persisted
to a JSON file so records survive between runs.

Run with:  python bank.py
"""

import json
import os
import random
import datetime

# ---------------------------------------------------------------------------
# CONFIGURATION / GLOBAL CONSTANTS
# ---------------------------------------------------------------------------

DATA_FILE = "accounts.json"
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"          # change this for real-world use
MIN_OPENING_BALANCE = 500


# ---------------------------------------------------------------------------
# DATA HANDLING FUNCTIONS  (read/write JSON "database")
# ---------------------------------------------------------------------------

def load_data():
    """Load all accounts from the JSON file. Returns a dict keyed by account number."""
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, "r") as f:
            content = f.read().strip()
            if not content:
                return {}
            return json.loads(content)
    except (json.JSONDecodeError, IOError):
        print("Warning: data file was corrupted or unreadable. Starting fresh.")
        return {}


def save_data(accounts):
    """Persist the accounts dictionary back to the JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(accounts, f, indent=4)


def generate_account_number(accounts):
    """Generate a unique 6-digit account number that isn't already in use."""
    while True:
        acc_no = str(random.randint(100000, 999999))
        if acc_no not in accounts:
            return acc_no


def get_timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# ---------------------------------------------------------------------------
# UTILITY / VALIDATION FUNCTIONS
# ---------------------------------------------------------------------------

def press_enter_to_continue():
    input("\nPress Enter to continue...")


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def get_valid_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive amount.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def get_valid_name(prompt):
    while True:
        name = input(prompt).strip()
        if name.replace(" ", "").isalpha() and len(name) > 0:
            return name.title()
        print("Please enter a valid name (letters only).")


def get_valid_phone(prompt):
    while True:
        phone = input(prompt).strip()
        if phone.isdigit() and 7 <= len(phone) <= 15:
            return phone
        print("Please enter a valid phone number (digits only).")


def find_account(accounts, acc_no):
    return accounts.get(acc_no)


def authenticate(accounts, acc_no, pin):
    account = find_account(accounts, acc_no)
    if account and account["pin"] == pin:
        return account
    return None


def add_transaction(account, txn_type, amount, balance_after, note=""):
    account.setdefault("transactions", []).append({
        "type": txn_type,
        "amount": amount,
        "balance_after": balance_after,
        "timestamp": get_timestamp(),
        "note": note
    })


# ---------------------------------------------------------------------------
# CORE BANKING OPERATIONS
# ---------------------------------------------------------------------------

def create_account(accounts):
    clear_screen()
    print("=" * 50)
    print(" " * 15 + "OPEN NEW ACCOUNT")
    print("=" * 50)

    name = get_valid_name("Enter full name: ")
    phone = get_valid_phone("Enter phone number: ")
    address = input("Enter address: ").strip()

    while True:
        acc_type = input("Account type (Savings/Current): ").strip().capitalize()
        if acc_type in ("Savings", "Current"):
            break
        print("Please choose either 'Savings' or 'Current'.")

    while True:
        pin = input("Set a 4-digit PIN: ").strip()
        if pin.isdigit() and len(pin) == 4:
            break
        print("PIN must be exactly 4 digits.")

    print(f"Minimum opening balance is {MIN_OPENING_BALANCE}.")
    balance = get_valid_float("Enter opening deposit amount: ")
    while balance < MIN_OPENING_BALANCE:
        print(f"Amount must be at least {MIN_OPENING_BALANCE}.")
        balance = get_valid_float("Enter opening deposit amount: ")

    acc_no = generate_account_number(accounts)

    account = {
        "account_no": acc_no,
        "name": name,
        "phone": phone,
        "address": address,
        "type": acc_type,
        "pin": pin,
        "balance": balance,
        "status": "active",
        "created_on": get_timestamp(),
        "transactions": []
    }
    add_transaction(account, "Opening Deposit", balance, balance)

    accounts[acc_no] = account
    save_data(accounts)

    print("\nAccount created successfully!")
    print(f"Your Account Number is: {acc_no}")
    print("Please keep this number safe -- you'll need it to log in.")
    press_enter_to_continue()


def deposit_money(accounts):
    clear_screen()
    print("=" * 50)
    print(" " * 15 + "DEPOSIT MONEY")
    print("=" * 50)
    acc_no = input("Enter account number: ").strip()
    pin = input("Enter PIN: ").strip()

    account = authenticate(accounts, acc_no, pin)
    if not account:
        print("Authentication failed. Invalid account number or PIN.")
        press_enter_to_continue()
        return

    if account["status"] == "frozen":
        print("This account is frozen. Contact bank administration.")
        press_enter_to_continue()
        return

    amount = get_valid_float("Enter amount to deposit: ")
    account["balance"] += amount
    add_transaction(account, "Deposit", amount, account["balance"])
    save_data(accounts)

    print(f"\nDeposit successful! New balance: {account['balance']:.2f}")
    press_enter_to_continue()


def withdraw_money(accounts):
    clear_screen()
    print("=" * 50)
    print(" " * 15 + "WITHDRAW MONEY")
    print("=" * 50)
    acc_no = input("Enter account number: ").strip()
    pin = input("Enter PIN: ").strip()

    account = authenticate(accounts, acc_no, pin)
    if not account:
        print("Authentication failed. Invalid account number or PIN.")
        press_enter_to_continue()
        return

    if account["status"] == "frozen":
        print("This account is frozen. Contact bank administration.")
        press_enter_to_continue()
        return

    amount = get_valid_float("Enter amount to withdraw: ")
    if amount > account["balance"]:
        print("Insufficient balance!")
        press_enter_to_continue()
        return

    account["balance"] -= amount
    add_transaction(account, "Withdrawal", amount, account["balance"])
    save_data(accounts)

    print(f"\nWithdrawal successful! New balance: {account['balance']:.2f}")
    press_enter_to_continue()


def transfer_money(accounts):
    clear_screen()
    print("=" * 50)
    print(" " * 14 + "TRANSFER MONEY")
    print("=" * 50)
    from_acc = input("Enter your account number: ").strip()
    pin = input("Enter PIN: ").strip()

    sender = authenticate(accounts, from_acc, pin)
    if not sender:
        print("Authentication failed. Invalid account number or PIN.")
        press_enter_to_continue()
        return

    if sender["status"] == "frozen":
        print("This account is frozen. Contact bank administration.")
        press_enter_to_continue()
        return

    to_acc = input("Enter recipient account number: ").strip()
    receiver = find_account(accounts, to_acc)

    if not receiver:
        print("Recipient account does not exist.")
        press_enter_to_continue()
        return

    if to_acc == from_acc:
        print("Cannot transfer to your own account.")
        press_enter_to_continue()
        return

    amount = get_valid_float("Enter amount to transfer: ")
    if amount > sender["balance"]:
        print("Insufficient balance!")
        press_enter_to_continue()
        return

    sender["balance"] -= amount
    receiver["balance"] += amount

    add_transaction(sender, "Transfer Sent", amount, sender["balance"], note=f"To {to_acc}")
    add_transaction(receiver, "Transfer Received", amount, receiver["balance"], note=f"From {from_acc}")

    save_data(accounts)
    print(f"\nTransfer successful! New balance: {sender['balance']:.2f}")
    press_enter_to_continue()


def check_balance(accounts):
    clear_screen()
    print("=" * 50)
    print(" " * 15 + "CHECK BALANCE")
    print("=" * 50)
    acc_no = input("Enter account number: ").strip()
    pin = input("Enter PIN: ").strip()

    account = authenticate(accounts, acc_no, pin)
    if not account:
        print("Authentication failed. Invalid account number or PIN.")
        press_enter_to_continue()
        return

    print(f"\nAccount Holder: {account['name']}")
    print(f"Current Balance: {account['balance']:.2f}")
    press_enter_to_continue()


def view_account_details(accounts):
    clear_screen()
    print("=" * 50)
    print(" " * 13 + "ACCOUNT DETAILS")
    print("=" * 50)
    acc_no = input("Enter account number: ").strip()
    pin = input("Enter PIN: ").strip()

    account = authenticate(accounts, acc_no, pin)
    if not account:
        print("Authentication failed. Invalid account number or PIN.")
        press_enter_to_continue()
        return

    print(f"\nAccount Number : {account['account_no']}")
    print(f"Name           : {account['name']}")
    print(f"Phone          : {account['phone']}")
    print(f"Address        : {account['address']}")
    print(f"Account Type   : {account['type']}")
    print(f"Status         : {account['status']}")
    print(f"Balance        : {account['balance']:.2f}")
    print(f"Opened On      : {account['created_on']}")
    press_enter_to_continue()


def transaction_history(accounts):
    clear_screen()
    print("=" * 50)
    print(" " * 12 + "TRANSACTION HISTORY")
    print("=" * 50)
    acc_no = input("Enter account number: ").strip()
    pin = input("Enter PIN: ").strip()

    account = authenticate(accounts, acc_no, pin)
    if not account:
        print("Authentication failed. Invalid account number or PIN.")
        press_enter_to_continue()
        return

    txns = account.get("transactions", [])
    if not txns:
        print("No transactions found.")
    else:
        print(f"\n{'Date/Time':<20}{'Type':<20}{'Amount':<12}{'Balance':<12}{'Note'}")
        print("-" * 80)
        for t in txns:
            print(f"{t['timestamp']:<20}{t['type']:<20}{t['amount']:<12.2f}{t['balance_after']:<12.2f}{t.get('note','')}")
    press_enter_to_continue()


def update_account(accounts):
    clear_screen()
    print("=" * 50)
    print(" " * 14 + "UPDATE ACCOUNT")
    print("=" * 50)
    acc_no = input("Enter account number: ").strip()
    pin = input("Enter PIN: ").strip()

    account = authenticate(accounts, acc_no, pin)
    if not account:
        print("Authentication failed. Invalid account number or PIN.")
        press_enter_to_continue()
        return

    print("What would you like to update?")
    print("1. Phone Number")
    print("2. Address")
    print("3. PIN")
    choice = input("Enter choice: ").strip()

    if choice == "1":
        account["phone"] = get_valid_phone("Enter new phone number: ")
        print("Phone number updated.")
    elif choice == "2":
        account["address"] = input("Enter new address: ").strip()
        print("Address updated.")
    elif choice == "3":
        while True:
            new_pin = input("Enter new 4-digit PIN: ").strip()
            if new_pin.isdigit() and len(new_pin) == 4:
                account["pin"] = new_pin
                print("PIN updated.")
                break
            print("PIN must be exactly 4 digits.")
    else:
        print("Invalid choice.")
        press_enter_to_continue()
        return

    save_data(accounts)
    press_enter_to_continue()


def close_account(accounts):
    clear_screen()
    print("=" * 50)
    print(" " * 15 + "CLOSE ACCOUNT")
    print("=" * 50)
    acc_no = input("Enter account number: ").strip()
    pin = input("Enter PIN: ").strip()

    account = authenticate(accounts, acc_no, pin)
    if not account:
        print("Authentication failed. Invalid account number or PIN.")
        press_enter_to_continue()
        return

    if account["balance"] > 0:
        print(f"Please withdraw your remaining balance ({account['balance']:.2f}) before closing.")
        press_enter_to_continue()
        return

    confirm = input("Are you sure you want to close this account? (yes/no): ").strip().lower()
    if confirm == "yes":
        del accounts[acc_no]
        save_data(accounts)
        print("Account closed successfully.")
    else:
        print("Account closure cancelled.")
    press_enter_to_continue()


# ---------------------------------------------------------------------------
# ADMIN OPERATIONS
# ---------------------------------------------------------------------------

def admin_login():
    print("=" * 50)
    print(" " * 17 + "ADMIN LOGIN")
    print("=" * 50)
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    return username == ADMIN_USERNAME and password == ADMIN_PASSWORD


def admin_view_all_accounts(accounts):
    clear_screen()
    print("=" * 80)
    print(" " * 25 + "ALL BANK ACCOUNTS")
    print("=" * 80)
    if not accounts:
        print("No accounts found.")
    else:
        print(f"{'Acc No':<10}{'Name':<20}{'Type':<12}{'Balance':<12}{'Status'}")
        print("-" * 80)
        for acc in accounts.values():
            print(f"{acc['account_no']:<10}{acc['name']:<20}{acc['type']:<12}{acc['balance']:<12.2f}{acc['status']}")
    press_enter_to_continue()


def admin_freeze_unfreeze(accounts):
    clear_screen()
    print("=" * 50)
    print(" " * 10 + "FREEZE / UNFREEZE ACCOUNT")
    print("=" * 50)
    acc_no = input("Enter account number: ").strip()
    account = find_account(accounts, acc_no)
    if not account:
        print("Account not found.")
        press_enter_to_continue()
        return

    if account["status"] == "active":
        account["status"] = "frozen"
        print("Account has been frozen.")
    else:
        account["status"] = "active"
        print("Account has been unfrozen.")

    save_data(accounts)
    press_enter_to_continue()


def admin_search_account(accounts):
    clear_screen()
    print("=" * 50)
    print(" " * 14 + "SEARCH ACCOUNT")
    print("=" * 50)
    acc_no = input("Enter account number: ").strip()
    account = find_account(accounts, acc_no)
    if not account:
        print("Account not found.")
    else:
        print(f"\nAccount Number : {account['account_no']}")
        print(f"Name           : {account['name']}")
        print(f"Phone          : {account['phone']}")
        print(f"Type           : {account['type']}")
        print(f"Balance        : {account['balance']:.2f}")
        print(f"Status         : {account['status']}")
    press_enter_to_continue()


def admin_bank_statistics(accounts):
    clear_screen()
    print("=" * 50)
    print(" " * 14 + "BANK STATISTICS")
    print("=" * 50)
    total_accounts = len(accounts)
    total_balance = sum(acc["balance"] for acc in accounts.values())
    active = sum(1 for acc in accounts.values() if acc["status"] == "active")
    frozen = sum(1 for acc in accounts.values() if acc["status"] == "frozen")

    print(f"Total Accounts   : {total_accounts}")
    print(f"Active Accounts  : {active}")
    print(f"Frozen Accounts  : {frozen}")
    print(f"Total Bank Funds : {total_balance:.2f}")
    press_enter_to_continue()


def admin_menu(accounts):
    if not admin_login():
        print("Invalid admin credentials.")
        press_enter_to_continue()
        return

    while True:
        clear_screen()
        print("=" * 50)
        print(" " * 15 + "ADMIN DASHBOARD")
        print("=" * 50)
        print("1. View All Accounts")
        print("2. Search Account")
        print("3. Freeze/Unfreeze Account")
        print("4. Bank Statistics")
        print("5. Logout")
        print("=" * 50)
        choice = input("Enter choice: ").strip()

        if choice == "1":
            admin_view_all_accounts(accounts)
        elif choice == "2":
            admin_search_account(accounts)
        elif choice == "3":
            admin_freeze_unfreeze(accounts)
        elif choice == "4":
            admin_bank_statistics(accounts)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")
            press_enter_to_continue()


# ---------------------------------------------------------------------------
# MAIN MENU / PROGRAM ENTRY POINT
# ---------------------------------------------------------------------------

def customer_menu(accounts):
    while True:
        clear_screen()
        print("=" * 50)
        print(" " * 10 + "BANK MANAGEMENT SYSTEM")
        print("=" * 50)
        print("1. Open New Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. Check Balance")
        print("6. View Account Details")
        print("7. Transaction History")
        print("8. Update Account Info")
        print("9. Close Account")
        print("10. Admin Panel")
        print("0. Exit")
        print("=" * 50)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            create_account(accounts)
        elif choice == "2":
            deposit_money(accounts)
        elif choice == "3":
            withdraw_money(accounts)
        elif choice == "4":
            transfer_money(accounts)
        elif choice == "5":
            check_balance(accounts)
        elif choice == "6":
            view_account_details(accounts)
        elif choice == "7":
            transaction_history(accounts)
        elif choice == "8":
            update_account(accounts)
        elif choice == "9":
            close_account(accounts)
        elif choice == "10":
            admin_menu(accounts)
        elif choice == "0":
            print("\nThank you for using our Bank Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            press_enter_to_continue()


def main():
    accounts = load_data()
    customer_menu(accounts)


if __name__ == "__main__":
    main()
