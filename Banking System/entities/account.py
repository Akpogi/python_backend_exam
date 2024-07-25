class Account:
    prev_account_id = 0
    prev_account_number = 100

    def __init__(self, customer_id):
        Account.prev_account_id += 1
        Account.prev_account_number += 1 
        self.account_id = str(Account.prev_account_id).zfill(2)
        self.customer_id = customer_id
        self.account_number = str(Account.prev_account_number)
        self.balance = 0.00

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount >= self.balance:
            return False  
        else:
            self.balance -= amount
            return True
       
    def get_balance(self):
        return self.balance
    