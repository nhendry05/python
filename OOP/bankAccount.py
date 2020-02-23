class BankAccount:
    def __init__(self, int_rate, balance=None):
        self.int_rate = int_rate
        if balance is None:
            self.balance = 0
        else:
            self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        print("Balance: $", self.balance, sep = "")
        return self
    def yield_interest(self):
        self.balance += (self.balance*self.int_rate)
        return self

user1 = BankAccount(.01, 100)
user2 = BankAccount(.02)

user1.deposit(100).deposit(200).deposit(300).withdraw(250).yield_interest().display_account_info()
user2.deposit(1000).deposit(50).withdraw(100).withdraw(22).withdraw(33).withdraw(100).yield_interest().display_account_info()



