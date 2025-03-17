#!/usr/bin/env python3
# Author ID: lbrown63

class BankAccount:
    """A class representing a simple bank account."""
    
    def __init__(self, account_holder, balance=0):
        """Constructor to initialize the bank account with a holder name and balance."""
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        """Deposits money into the account and returns the new balance."""
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        return "Deposit amount must be positive."

    def withdraw(self, amount):
        """Withdraws money if sufficient funds exist and returns the new balance."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        return "Insufficient funds or invalid amount."

    def get_balance(self):
        """Returns the current balance of the account."""
        return f"Account holder: {self.account_holder}, Balance: ${self.balance}"

if __name__ == '__main__':
    account1 = BankAccount("Quardeelia Brown", 1000)
    
    print(account1.get_balance())
    print(account1.deposit(500))
    print(account1.withdraw(200))
    print(account1.withdraw(1500))  # Should print an insufficient funds message
