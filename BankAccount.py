from random import randint

class BankAccount:
    def __init__(self, full_name, balance = 0):
        self.full_name = full_name
        self.account_number = randint(10000000, 99999999) 
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited Amount: {amount}\nNew Balance: {self.__round()}\n")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds")
            self.balance -= amount + 10
            self.__round()
        else:
            self.balance -= amount
            print(f"Withdrawn Amount: {amount}\nNew Balance: {self.__round()}\n")
    
    def get_balance(self):
        print(f"Account Balance: {self.balance}\n")
        return self.__round()

    def add_interests(self):
        interest = self.balance * 0.0083
        self.balance += interest
        self.__round()

    def print_statement(self):
        print(f"Name: {self.full_name}\nAccount Number: {self.account_number}\nBalance: {self.balance}\n")
    
    def __round(self):
        self.balance = round(self.balance, 2)
        return self.balance


# create/instantiate 3 bank account examples
# ---------------------------------------------------------------
alisha_account = BankAccount("Alisha Hwee", 400)
# output "400"
alisha_account.get_balance()
# output 150
alisha_account.withdraw(250)
# output 175
alisha_account.deposit(25)
# add interests
alisha_account.add_interests()
# outputs new balance 176.45 & account no.
alisha_account.print_statement()

# ---------------------------------------------------------------
scott_account = BankAccount("Scott Yang", 5000)
# outputs 5000
scott_account.get_balance()
# rounds to nearest cent and outputs 3999.65
scott_account.withdraw(1000.3543)
# rounds to nearest cent and outputs 4200.19
scott_account.deposit(200.543)
# add interest and rounds to nearest cent
scott_account.add_interests()
# outputs new balance 4235.05 & account no.
scott_account.print_statement()

# ---------------------------------------------------------------

