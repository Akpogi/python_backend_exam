import entities.account as accountEntity
import infrastracture.account_repository as account_repository

class CreateAccount:
    def __init__(self):
        self.account_repo = account_repository.AccountRepository()

    def collect_inputs(self):
        customer_id = input("Enter Customer ID: ")
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        phone_number = input("Enter Phone Number: ")
        
        # To check if some values are blank
        if not customer_id:
            raise ValueError("Error: Customer ID cannot be blank.")
        if not name:
            raise ValueError("Error: Name cannot be blank.")
        if not email:
            raise ValueError("Error: Email cannot be blank.")
        if not phone_number:
            raise ValueError("Error: Phone Number cannot be blank.")
        
        return customer_id, name, email, phone_number
    

    def create_account(self, customer_id, name, email, phone_number):
        account = accountEntity.Account(customer_id)
        account.name = name
        account.email = email
        account.phone_number = phone_number

        return account
