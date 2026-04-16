class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        self.balance += amount
        self.history.append(f"+{amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.history.append(f"-{amount}")


class Bank:
    def __init__(self):
        self.accounts = {}

    def add(self, account):
        self.accounts[account.owner] = account

    def transfer(self, a, b, amount):
        if self.accounts[a].balance >= amount:
            self.accounts[a].withdraw(amount)
            self.accounts[b].deposit(amount)
