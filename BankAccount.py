class BankAccount:
    def __init__(self, full_name, account_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited Amount: {amount}.\nNew Balance: {self.balance}.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds.")
            self.balance -= amount + 10
        else:
            self.balance -= amount
            print(f"Withdrawn Amount: {amount}.\nNew Balance: {self.balance}.")
    
    def get_balance(self):
        print(f"Account Balance: {self.balance}.")
        return self.balance

    def add_interests(self):
        interest = self.balance * 0.0083
        self.balance += interest
        print(self.balance)

    def print_statement(self):
        print(f"Name: {self.full_name}\nAccount Number: {self.account_number}\nBalance: {self.balance}")


# # Tests
# # Instantiate (create) an account
# scott_account = BankAccount("Scott Yang", 123456, 200)
# # deposit
# scott_account.deposit(150)
# # withdraw and display new balance
# scott_account.withdraw(100)
# # withdraw and display insufficient funds
# scott_account.withdraw(251)
# # get balance
# scott_account.get_balance()
# # add_interests test
# scott_account.add_interests()
# # print statement
# scott_account.print_statement()