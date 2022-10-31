from BankAccount import BankAccount

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