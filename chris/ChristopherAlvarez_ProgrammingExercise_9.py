"""
Bank Account Program - Christopher Alvarez

This program defines a BankAcct class that represents a bank account.
It allows deposits, withdrawals, interest rate adjustments, and
calculates interest based on a number of days.

A test function is included to demonstrate all class methods.
"""


# This class represents a bank account
class BankAcct:

    # Sets up account details
    def __init__(self, name, account_number, amount, interest_rate):
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate

    # Deposits money into the account
    def deposit(self, value):
        self.amount += value
        print(f"Deposited ${value:.2f}")

    # Withdraws money from the account
    def withdraw(self, value):
        self.amount -= value
        print(f"Withdrew ${value:.2f}")

    # Updates the interest rate
    def adjust_interest_rate(self, new_rate):
        self.interest_rate = new_rate
        print(f"Interest rate updated to {new_rate * 100:.2f}%")

    # Returns the current balance
    def get_balance(self):
        return self.amount

    # Calculates interest based on number of days
    def calculate_interest(self, days):
        interest = self.amount * self.interest_rate * (days / 365)
        return interest

    # Return account information as a string
    def __str__(self):
        return (f"Account Holder: {self.name}\n"
                f"Account Number: {self.account_number}\n"
                f"Balance: ${self.amount:.2f}\n"
                f"Interest Rate: {self.interest_rate * 100:.2f}%")


# This function tests the BankAcct class
def test_bank_account():

    print("=== Creating Account ===")

    acct = BankAcct("John Doe", "123456", 1000.00, 0.05)
    print(acct)

    print("\n=== Deposit ===")

    acct.deposit(500)
    print(f"Balance: ${acct.get_balance():.2f}")

    print("\n=== Withdraw ===")

    acct.withdraw(200)
    print(f"Balance: ${acct.get_balance():.2f}")

    print("\n=== Adjust Interest Rate ===")

    acct.adjust_interest_rate(0.03)

    print("\n=== Calculate Interest (30 days) ===")

    interest = acct.calculate_interest(30)
    print(f"Interest: ${interest:.2f}")

    print("\n=== Final Account Info ===")

    print(acct)


# Run the test function
test_bank_account()