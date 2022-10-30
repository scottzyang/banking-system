class BankAccount:
    def __init__(self, full_name, account_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited Amount: {amount}.\nNew Balance: {self.balance}.")



# scott_account = BankAccount("Scott Yang", 123456, 200)
# scott_account.deposit(150)