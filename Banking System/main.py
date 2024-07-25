import infrastracture.account_repository as account_repository
import use_cases.transaction as transaction
import use_cases.account_statement as account_statement
import use_cases.create_account as create_account

# Create Instances
create_acc = create_account.CreateAccount()
account_repo = account_repository.AccountRepository()
account_stmt = account_statement.AccountStatement()
transact = transaction.Transaction(account_repo, account_stmt)

# Sample Accounts 
sample_acc1 = create_acc.create_account('01', 'Juan Dela Cruz', 'jdc@gmail.com', '09123456789')
sample_acc2 = create_acc.create_account('02', 'John Doe', 'jd@gmail.com', '09223456789')
account_repo.save_account(sample_acc1)
account_repo.save_account(sample_acc2)


# CREATING ACCOUNT
# Input Details
print('--Create an Account--')
try:
    customer_id, name, email, phone_number = create_acc.collect_inputs()
    user_acc = create_acc.create_account(customer_id, name, email, phone_number)

    account_repo.save_account(user_acc)
    print(f"Account created successfully!")
except ValueError as e:
    print(e)

print(f"""Account Details
      Account ID: {user_acc.account_id}
      Name: {user_acc.name}
      Customer ID: {user_acc.customer_id}
      Email: {user_acc.email}
      Phone Number: {user_acc.phone_number}
      Account Number: {user_acc.account_number}
      Balance: {user_acc.get_balance()}
    """)

# TRANSACTION
print("--TRANSACTION--")
transact = transaction.Transaction(account_repo, account_stmt)

# Loop for multiple transactions
while True:
    try:
        account_id = input('Enter Account ID: ')
        amount_str = input("Enter the amount: ")
        amount = int(amount_str)
        transaction_type = input("Enter 'withdraw' or 'deposit': ")

        transact.make_transaction(account_id, amount, transaction_type)
    except ValueError as e:
        print(e)

    continue_transaction = input("Do you want to make another transaction? (yes/no): ").strip().lower()
    if continue_transaction != 'yes':
        break

# Generate and print account statement
print('--Generate Account Statement--')
try:
    acc_id_for_statement = input('Enter Account ID: ')
    account_stmt.generate_account_statement(acc_id_for_statement)
except ValueError as e:
    print(e)

# Find account using account_id
print("--Find Account with Account ID--")
try:
    acc_id_to_find = input("Enter Account ID to find: ")
    account_repo.find_account_by_id(acc_id_to_find)
except ValueError as e:
    print(e)

# Find account using customer_id
print("--Find Account with Customer ID--")
try:
    cus_id_to_find = input("Enter Customer ID to find: ")
    account_repo.find_accounts_by_customer_id(cus_id_to_find)
except ValueError as e:
    print(e)







