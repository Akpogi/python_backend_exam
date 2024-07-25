import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import use_cases.create_account as create_account
import infrastracture.account_repository as account_repository

create_acc = create_account.CreateAccount()
account_repo = account_repository.AccountRepository()
# Input Details
new_customer_id, name, email, phone_number = create_acc.collect_inputs()

# To save the account
user_acc = create_acc.create_account(new_customer_id, name, email, phone_number)

account_repo.save_account(user_acc)
print(f"Account created successfully!")
print(f"""Account Details
      Account ID: {user_acc.account_id}
      Name: {user_acc.name}
      Customer ID: {user_acc.customer_id}
      Email: {user_acc.email}
      Phone Number: {user_acc.phone_number}
      Account Number: {user_acc.account_number}
      Balance: {user_acc.get_balance()}""")
