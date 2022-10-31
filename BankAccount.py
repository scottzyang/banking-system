from random import randint

class BankAccount:
    def __init__(self, full_name, balance = 0):
        self.full_name = full_name
        self.account_number = randint(10000000, 99999999) 
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print(f"Unable to complete transaction. Please try again.\n")
        else:
            self.balance += amount
            print(f"Deposited Amount: {amount}\nNew Balance: {self.__round()}\n")

    def withdraw(self, amount):
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
        if self.balance < 0:
            print(f"Error: Cannot add interest to a negative balance\n")
        else: 
            interest = self.balance * 0.0083
            self.balance += interest
            self.__round()

    def print_statement(self):
        print(f"Name: {self.full_name}\nAccount Number: {self.account_number}\nBalance: {self.balance}\n")
    
    def __round(self):
        self.balance = round(self.balance, 2)
        return self.balance




