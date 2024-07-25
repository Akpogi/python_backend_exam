import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import use_cases.create_account as create_account
import infrastracture.account_repository as account_repository

create_acc = create_account.CreateAccount()
account_repo = account_repository.AccountRepository()

sample_acc1 = create_acc.create_account('01', 'Juan Dela Cruz', 'jdc@gmail.com', '09123456789')
sample_acc2 = create_acc.create_account('02', 'John Doe', 'jd@gmail.com', '09223456789')
account_repo.save_account(sample_acc1)
account_repo.save_account(sample_acc2)

print("Find Account with Account ID")
try:
    acc_id_to_find = input("Enter Account ID to find: ")
    account_repo.find_account_by_id(acc_id_to_find)
except ValueError as e:
    print(e)