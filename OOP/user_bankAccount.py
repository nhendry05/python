class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.2, balance = 0)
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    def make_withdrawl(self, amount):
        self.account.withdraw(amount)
        return self
    def display_user_balance(self):
        self.account.display_account_info()
        return self


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

nicole = User("Nicole", "nicole@email.com")

nicole.make_deposit(100)
nicole.make_withdrawl(50)
nicole.display_user_balance()