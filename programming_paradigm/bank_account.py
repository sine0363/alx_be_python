class BankAccount:
    def __init__(self, account_balance=0):
        self.__account_balance = account_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return amount  # return the deposited amount
        return 0

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        return self.__account_balance

    def get_balance(self):
        return self.__account_balance



    
    
account =BankAccount(1000)

account.deposit(50)
account.withdraw(20)



