class Account:

    def __init__(self, name):
        self.name = name
        self.balance = 0

    def deposit(self, amount):
        self.amount = amount
        if self.balance >= 0:
            self.amount += 1
            return True
        else:
             return False

    def withdraw(self, amount):
        self.amount = amount
        if self.balance >= 0:
            self.amount -= 1
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def get_name(self):
        return self.name






















