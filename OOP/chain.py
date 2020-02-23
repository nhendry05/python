class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print('User: ', self.name, ', Balance: $', self.account_balance, sep="")
        return self
    def transfer_money(self, transfer_to, money):
        self.make_withdrawl(money)
        transfer_to.make_deposit(money)
        print('User: ', self.name, ', Balance: $', self.account_balance, sep="")
        print('User: ', transfer_to.name, ', Balance: $', transfer_to.account_balance, sep="")
        return self
nicole = User("Nicole", "email@email.com")
maxwell = User("Max", "maxwell@email.com")
gus = User("Gus", "gus@email.com")

nicole.make_deposit(200).make_deposit(73).make_deposit(180).make_withdrawl(112).display_user_balance()

print(" ")

maxwell.make_deposit(133).make_deposit(512).make_withdrawl(105).make_withdrawl(38).display_user_balance()

print(" ")

gus.make_deposit(200).make_withdrawl(54).make_withdrawl(110).make_withdrawl(53).display_user_balance()

print(" ")

nicole.transfer_money(gus, 100)