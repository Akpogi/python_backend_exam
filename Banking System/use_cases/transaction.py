class Transaction:
    def __init__(self, account_repository, account_statement):
        self.account_repository = account_repository
        self.account_statement = account_statement

    def make_transaction(self, account_id, amount, transaction_type):
        account = self.account_repository.search_account_id(account_id)
        if not account:
            raise ValueError("Error: Account not found")

        if transaction_type == 'deposit':
            account.deposit(amount)
            self.account_statement.record_transaction(account_id, 'deposit', amount, account.balance)
            print(f"Amount Deposited: {amount}, Updated Balance: {account.get_balance()}\n")      
        elif transaction_type == 'withdraw':
            success = account.withdraw(amount)
            if success:
                self.account_statement.record_transaction(account_id, 'withdraw', amount, account.balance)
                print(f"Amount Withdrawn: {amount}, Updated Balance: {account.get_balance()}\n")
            else:
                raise ValueError("Error: Insufficient Balance!")
        else:
            raise ValueError("Error: Invalid transaction type")
