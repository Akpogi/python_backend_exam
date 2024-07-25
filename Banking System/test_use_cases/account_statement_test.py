import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import use_cases.create_account as create_account
import infrastracture.account_repository as account_repository
import use_cases.transaction as transaction
import use_cases.account_statement as account_statement

create_acc = create_account.CreateAccount()
account_repo = account_repository.AccountRepository()
account_stmt = account_statement.AccountStatement()

new_acc = create_acc.create_account('01', 'Juan Dela Cruz', 'jdc@gmail.com', '09123456789')
account_repo.save_account(new_acc)

transact = transaction.Transaction(account_repo, account_stmt)

while True:
    account_id = input('Enter Account ID: ')
    amount_str = input("Enter the amount: ")
    amount = int(amount_str)
    transaction_type = input("Enter 'withdraw' or 'deposit': ")

    transact.make_transaction(account_id, amount, transaction_type)
    
    continue_transaction = input("Do you want to make another transaction? (yes/no): ").strip().lower()
    if continue_transaction != 'yes':
        break

try:
    acc_id = input('Enter Account ID: ')
    account_stmt.generate_account_statement(acc_id)
except ValueError as e:
    print(e)