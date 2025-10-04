class BankAccount ():
    def __init__(self, account_balance=0):
        self.__account_balance = account_balance
        


    
    def deposit(self,amount):
        if amount>0:
            self.__account_balance +=amount
        return self.__account_balance
    
    def withdraw(self,amount):
        if 0<amount <= self.__account_balance:
            self.__account_balance-=amount
            return True
        return False
    def display_balance(self):
        print(f"Current Balance: {self.__account_balance}")
    

    def get_balance(self):
        return self.__account_balance
    
account = BankAccount(1000)
account.deposit(110)
account.withdraw(50)
account.get_balance()

print("Current balance via getter:", account.get_balance())





    


    


    


    



        

        




        

           
        