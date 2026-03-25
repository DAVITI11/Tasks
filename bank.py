import random

def log_transaction(func):
    def wrapper(opnm,amount,balance,owner,account_id):
        print(f"operation name = {opnm}  amount = {amount}  balance = {balance}  owner = {owner}   account_id = {account_id}")
        return func(opnm,amount,balance,owner,account_id)
    return wrapper

class BankAccount:

    def __init__(self,owner,account_id,_balance):
        self.owner = owner
        self.account_id = account_id
        self._balance = _balance
    
    def deposit(self,amount):
        if amount > 100:
            self._balance += amount + (amount * 5 // 100)
        elif amount <=0 :
            print('❌ Warning')
        else:
            self._balance += amount
        @log_transaction
        def mktr(opnm,amount,balance,owner,account_id):
            print("Transaction completed")
        mktr('თანხის შეტანა',amount,self._balance,self.owner,self.account_id)

    def withdraw(self,amount):
        if amount <= 0:
            print('❌ Amount must be positive')
        else:
            self._balance -= amount
        if self._balance < 0:
            self._balance -= 10    
        @log_transaction
        def mktr(opnm,amount,balance,owner,account_id):
            print("Transaction completed")
        mktr('თანხის გატანა',amount,self._balance,self.owner,self.account_id)
    
    def show_balance(self):
        print(f"{self.owner} {self.account_id} {self._balance}")

def account_generator():
    owners = ['Dato', 'Tamuna','Ana']
    for i in range(3):
        owner = owners[i]
        account_id = i + 1
        balance = random.randint(50,200)
        yield BankAccount(owner,account_id,balance)

accounts = list(account_generator())

for acc in accounts:
    acc.show_balance()
    acc.deposit(50)
    acc.show_balance()
    acc.withdraw(40)
    acc.show_balance()
    print()