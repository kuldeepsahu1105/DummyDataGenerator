from faker import Faker
import random
from datetime import datetime

fake = Faker()

class CBSCustomer:
    def __init__(self):
        self.customer_id = fake.random_int(min=1, max=99999)
        self.first_name = fake.first_name()
        self.last_name = fake.last_name()
        self.email = fake.email()
        self.phone = fake.phone_number()
        self.dob = fake.date_of_birth()
        self.address = fake.address()
        self.city = fake.city()
        self.state = fake.state()
        self.postal_code = fake.zipcode()
        self.country = fake.country()
        self.gender = random.choice(['Male', 'Female', 'Other'])
        self.kyc_status = random.choice(['Verified', 'Pending', 'Rejected'])
        self.customer_type = random.choice(['Individual', 'Corporate'])
        self.relationship_manager_id = fake.random_int(min=1, max=1000)
        self.status = random.choice(['Active', 'Inactive', 'Lead', 'Prospect'])
        self.source = random.choice(['Website', 'Referral', 'Campaign', 'Social Media'])
        self.created_at = fake.date_this_decade()
        self.updated_at = fake.date_this_year()

    def to_dict(self) -> dict:
        return {
            'customer_id': self.customer_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'gender': self.gender,
            'email': self.email,
            'phone': self.phone,
            'dob': self.dob,  # Keeping as datetime object
            'address': self.address,
            'city': self.city,
            'state': self.state,
            'postal_code': self.postal_code,
            'country': self.country,
            'status': self.status,
            'source': self.source,
            'created_at': self.created_at,  # Keeping as datetime object
            'updated_at': self.updated_at,  # Keeping as datetime object
            'kyc_status': self.kyc_status,
            'customer_type': self.customer_type,
            'relationship_manager_id': self.relationship_manager_id
        }

class CBSAccount:
    def __init__(self, customer_id):
        self.account_number = fake.unique.random_int(min=100000000, max=999999999)
        self.customer_id = customer_id
        self.account_type = random.choice(['Checking', 'Savings', 'Loan', 'Credit'])
        self.current_balance = round(random.uniform(500, 50000), 2)
        self.account_status = random.choice(['Active', 'Dormant', 'Closed'])
        self.opening_date = fake.date_this_decade()
        self.branch_code = fake.random_int(min=1000, max=9999)
        self.currency_type = random.choice(['USD', 'EUR', 'INR', 'GBP'])
        self.interest_rate = round(random.uniform(0.5, 5.0), 2)
        self.last_transaction_date = fake.date_this_month()

    def to_dict(self) -> dict:
        return {
            'account_number': self.account_number,
            'customer_id': self.customer_id,
            'account_type': self.account_type,
            'current_balance': self.current_balance,
            'opening_date': self.opening_date,  # Keeping as datetime object
            'branch_code': self.branch_code,
            'currency_type': self.currency_type,
            'account_status': self.account_status,
            'interest_rate': self.interest_rate,
            'last_transaction_date': self.last_transaction_date  # Keeping as datetime object
        }

class CBSFeedback:
    def __init__(self, customer_id):
        self.feedback_id = fake.random_int(min=1000, max=999999)
        self.customer_id = customer_id
        self.rating = random.choice([1, 2, 3, 4, 5])
        self.comments = fake.text(max_nb_chars=200)
        self.submitted_at = fake.date_this_month()

    def to_dict(self) -> dict:
        return {
            'feedback_id': self.feedback_id,
            'customer_id': self.customer_id,
            'rating': self.rating,
            'comments': self.comments,
            'submitted_at': self.submitted_at  # Keeping as datetime object
        }

class CBSTransaction:
    def __init__(self, customer_id):
        self.transaction_id = fake.random_int(min=1000, max=999999)
        self.customer_id = customer_id
        self.transaction_type = random.choice(['Deposit', 'Withdrawal', 'Transfer', 'UPI', 'Cheque', 'ATM', 'RTGS', 'NEFT'])
        self.amount = round(random.uniform(10, 500000000), 2)
        self.transaction_date = fake.date_this_month()
        self.status = random.choice(['Success', 'Failed'])

    def to_dict(self) -> dict:
        return {
            'transaction_id': self.transaction_id,
            'customer_id': self.customer_id,
            'transaction_type': self.transaction_type,
            'amount': self.amount,
            'transaction_date': self.transaction_date,  # Keeping as datetime object
            'status': self.status
        }

class CBSLoan:
    def __init__(self, customer_id):
        self.loan_id = fake.random_int(min=1000, max=99999)
        self.customer_id = customer_id
        self.loan_type = random.choice(['Personal', 'Business', 'Mortgage'])
        self.amount = round(random.uniform(1000, 50000000), 2)
        self.status = random.choice(['Approved', 'Rejected', 'Pending'])

    def to_dict(self) -> dict:
        return {
            'loan_id': self.loan_id,
            'customer_id': self.customer_id,
            'loan_type': self.loan_type,
            'amount': self.amount,
            'status': self.status
        }
