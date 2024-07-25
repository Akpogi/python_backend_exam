class AccountRepository:
    def __init__(self):
        self.saved_accounts = {}

    def save_account(self, account):
        self.saved_accounts[account.account_id] = account

    def find_account_by_id(self, account_id):
        account_found = False
        for account in self.saved_accounts.values():
            if account.account_id == account_id:
                print(f"""Account Details
                  Account ID: {account.account_id}
                  Name: {account.name}
                  Phone Number: {account.phone_number}
                  Email: {account.email}
                  Customer ID: {account.customer_id}
                  Account Number: {account.account_number}
                  Balance: {account.balance}\n"""
                )
                account_found = True
        if not account_found:
            raise ValueError("No such account exists.")
        

    def find_accounts_by_customer_id(self, customer_id):
        account_found = False
        for account in self.saved_accounts.values():
            if account.customer_id == customer_id:
                print(f"""Account Details
                  Account ID: {account.account_id}
                  Name: {account.name}
                  Phone Number: {account.phone_number}
                  Email: {account.email}
                  Customer ID: {account.customer_id}
                  Account Number: {account.account_number}
                  Balance: {account.balance}\n"""
                )
                account_found = True
        if not account_found:
            raise ValueError("No such account exists.")
        
    
    def search_account_id(self, account_id):
        for account in self.saved_accounts.values():
            if account.account_id == account_id:
                return account
        return None
