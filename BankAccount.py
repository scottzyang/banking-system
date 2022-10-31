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
        # check is deposited amount is valid
        if amount <= 0:
            print(f"Unable to complete transaction. Please try again.\n")
        else:
            self.balance += amount
            print(f"Deposited Amount: {amount}\nNew Balance: {self.__round()}\n")

    def withdraw(self, amount):
        # check if overdraft fees are needed
        if amount > self.balance:
            print("Insufficient Funds\n")
            self.balance -= amount + 10
            self.__round()
        else:
            self.balance -= amount
            print(f"Withdrawn Amount: {amount}\nNew Balance: {self.__round()}\n")
    
    def get_balance(self):
        print(f"Account Balance: {self.balance}\n")
        return self.__round()

    def add_interests(self):
        # verify balance to see if interests can be added
        if self.balance < 0:
            print(f"Error: Cannot add interest to a negative balance\n")
        else: 
            interest = self.balance * 0.0083
            self.balance += interest
            self.__round()

    def print_statement(self):
        print(f"Name: {self.full_name}\nAccount Number: {self.account_number}\nBalance: {self.balance}\n")
    
    # private method to round to nearest cent
    def __round(self):
        self.balance = round(self.balance, 2)
        return self.balance




