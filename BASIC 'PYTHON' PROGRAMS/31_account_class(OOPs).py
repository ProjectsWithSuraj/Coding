"""Write a Python program to create an Account class with two attributes:
1. balance
2. account_number

Create the following methods:
1. debit() subtract the given amount from the balance.
2. credit() add the given amount to the balance.
3. print_balance() display the current balance.

Create an Account object, perform one debit and one credit operation, and print the final balance.
"""
class account:
    def __init__(self,balance,acc):
        self.balance=balance
        self.account_no=acc
    def debit(self,amount):
        self.balance-=amount
        print("RS.", amount , "is debited.")
        print("Total Balance: ",self.total_balance())
    def credit(self,amount):
        self.balance+=amount
        print("RS.",amount,"is credited.")
        print("Total Balance: ",self.total_balance())
    def total_balance(self):
        return self.balance
acc1=account(1000,12345)
acc1.credit(100)
acc1.debit(50)