from codecs import backslashreplace_errors
from random import randint

class BankAccount:
    def __init__(self, full_name, balance = 0, account_number = None):
        self.full_name = full_name
        self.account_number = account_number
        self.balance = balance
        if account_number is None:
            # list comprehension to generate a string of numbers
            # loop 8 times and create a list of numbers between 0 and 9
            # join list together to a string
            self.account_number = ''.join(["{}".format(randint(0, 9)) for num in range(8)])

    def deposit(self, amount):
        # outputs error message if user inputs invalid deposit amount
        if amount <= 0:
            print(f"Unable to complete transaction. Please try again.\n")
        else:
        # outputs correct new balance based on user inputted amount
            amount = self.__round(amount)
            self.balance += amount
            print(f"Deposited Amount: ${amount}\nNew Balance: ${self.__round(self.balance)}\n")

    def withdraw(self, amount):
        # outputs error message if user inputted amount is greater than current balance
        if amount > self.balance:
            print("Insufficient Funds\n")
            self.balance -= amount + 10
        else:
        # outputs correct new balance based on user inputted amount
            amount = self.__round(amount)
            self.balance -= amount
            print(f"Withdrawn Amount: ${amount}\nNew Balance: ${self.balance}\n")
    
    def get_balance(self):
        # outputs current account balance
        print(f"Account Balance: ${self.balance}\n")
        return self.balance

    def add_interests(self):
        # outputs error message if current balance is 0 or less
        if self.balance <= 0:
            print(f"Error: Cannot add interest. Insufficient Funds.\n")
        else: 
        # adds correct interest and rounds to nearest hundredth
            interest = self.balance * 0.0083
            self.balance += interest
            self.balance = self.__round(self.balance)

    def print_statement(self):
        print(f"Name: {self.full_name}\nAccount Number: {self.account_number}\nBalance: ${self.balance}\n")
    
    # private method to round to nearest cent
    def __round(self, amount):
        amount = round(amount, 2)
        return amount




