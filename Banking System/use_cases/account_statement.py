class AccountStatement:
    def __init__(self):
        self.account_statements = {}

    def record_transaction(self, account_id, transaction_type, amount, balance):
        if account_id not in self.account_statements:
            self.account_statements[account_id] = []

        transaction = {
            'transaction_type': transaction_type,
            'amount': amount,
            'balance': balance
        }
        self.account_statements[account_id].append(transaction)

    def generate_account_statement(self, account_id):
        if account_id not in self.account_statements:
            raise ValueError(f"No transactions found for account ID: {account_id}")    
        else:
            print(f"Account Statements for Account ID '{account_id}'")
            for transaction in self.account_statements[account_id]:
                print(f"{transaction['transaction_type']}: {transaction['amount']}, Balance: {transaction['balance']}")
