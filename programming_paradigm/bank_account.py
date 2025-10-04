class BankAccount:
    def __init__(self, account_balance=0):
        self.__account_balance = account_balance  # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"${amount} withdrawn successfully.")
        else:
            print("Insufficient funds or invalid amount.")

    def display_balance(self):
        print(f"Current Balance: ${self.__account_balance}")

    def get_balance(self):
        return self.__account_balance
    
    
account =BankAccount(1000)

account.deposit(150)
account.withdraw(100)

account.display_balance()

