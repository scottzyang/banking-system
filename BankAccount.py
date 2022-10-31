from random import randint

class BankAccount:
    def __init__(self, full_name, balance = 0):
        self.full_name = full_name
        self.account_number = randint(10000000, 99999999) 
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited Amount: {amount}\nNew Balance: {self.balance}\n")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds")
            self.balance -= amount + 10
        else:
            self.balance -= amount
            print(f"Withdrawn Amount: {amount}\nNew Balance: {self.balance}\n")
    
    def get_balance(self):
        print(f"Account Balance: {self.balance}\n")
        return self.balance

    def add_interests(self):
        interest = self.balance * 0.0083
        self.balance += interest
        self.balance = round(self.balance, 2)

    def print_statement(self):
        print(f"Name: {self.full_name}\nAccount Number: {self.account_number}\nBalance: {self.balance}\n")


# create/instantiate 3 bank account examples
# ---------------------------------------------------------------
alisha_account = BankAccount("Alisha Hwee", 400)
# should output "400"
alisha_account.get_balance()
# should output 150
alisha_account.withdraw(250)
# should output 175
alisha_account.deposit(25)
# add interests
alisha_account.add_interests()
# new balance should be 176.45 & account no.
alisha_account.print_statement()




# Tests
# # Instantiate (create) an account
# scott_account = BankAccount("Scott Yang", 200)
# # deposit
# scott_account.deposit(150)
# # withdraw and display new balance
# scott_account.withdraw(100)
# # withdraw and display insufficient funds
# scott_account.withdraw(10)
# # get balance
# scott_account.get_balance()
# # add_interests test
# scott_account.add_interests()
# # print statement
# scott_account.print_statement()