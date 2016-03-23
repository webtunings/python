class BankAccount:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance
    

class MinimumBalanceAccount(BankAccount):
    def __init__(self, minimum_balance):
        BankAccount.__init__(self)
        self.minimum_balance = minimum_balance

    def withdrawal(self, amount):
        if self.balance - amount < self.minimum_balance:
            print('Sorry, minimum balance must be maintained.')
        else:
            self.withdraw(amount)

a = MinimumBalanceAccount(100)
print(a.deposit(100))
print(a.withdrawal(40))

b = MinimumBalanceAccount(100)
print(b.deposit(1000))
print(b.withdrawal(30))
print(b.balance)
