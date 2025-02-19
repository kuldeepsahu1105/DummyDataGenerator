from faker import Faker
import random

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
            'dob': str(self.dob),
            'address': self.address,
            'city': self.city,
            'state': self.state,
            'postal_code': self.postal_code,
            'country': self.country,
            'status': self.status,
            'source': self.source,
            'created_at': str(self.created_at),
            'updated_at': str(self.updated_at),
            'kyc_status': self.kyc_status,
            'customer_type': self.customer_type,
            'relationship_manager_id': self.relationship_manager_id
        }
    
# --- CBS Tables ---

# 9. cbs_accounts
class CBSAccount:
    def __init__(self):
        self.account_number = fake.unique.random_int(min=100000000, max=999999999)  # Added AccountNumber
        self.customer_id = fake.random_int(min=1, max=99999)
        self.account_type = random.choice(['Checking', 'Savings', 'Loan', 'Credit'])
        self.current_balance = round(random.uniform(500, 50000), 2)
        self.account_status = random.choice(['Active', 'Dormant', 'Closed'])
        self.opening_date = fake.date_this_decade()
        self.branch_code = fake.random_int(min=1000, max=9999)  # Added BranchCode
        self.currency_type = random.choice(['USD', 'EUR', 'INR', 'GBP'])  # Added CurrencyType
        self.interest_rate = round(random.uniform(0.5, 5.0), 2)  # Added InterestRate
        self.last_transaction_date = fake.date_this_month()  # Added LastTransactionDate

    def to_dict(self) -> dict:
        return {
            'account_number': self.account_number,
            'customer_id': self.customer_id,
            'account_type': self.account_type,
            'current_balance': self.current_balance,
            'opening_date': str(self.opening_date),
            'branch_code': self.branch_code,
            'currency_type': self.currency_type,
            'account_status': self.account_status,
            'interest_rate': self.interest_rate,
            'last_transaction_date': str(self.last_transaction_date)
        }
    

# 7. crm_feedback
class CBSFeedback:
    def __init__(self):
        self.feedback_id = fake.random_int(min=1000, max=9999)
        self.customer_id = fake.random_int(min=1, max=99999)
        self.rating = random.choice([1, 2, 3, 4, 5])
        self.comments = fake.text(max_nb_chars=200)
        self.submitted_at = fake.date_this_month()

    def to_dict(self) -> dict:
        return {
            'feedback_id': self.feedback_id,
            'customer_id': self.customer_id,
            'rating': self.rating,
            'comments': self.comments,
            'submitted_at': str(self.submitted_at)
        }

# 8. crm_transactions
class CBSTransaction:
    def __init__(self):
        self.transaction_id = fake.random_int(min=1000, max=9999)
        self.customer_id = fake.random_int(min=1, max=99999)
        self.transaction_type = random.choice(['Deposit', 'Withdrawal', 'Transfer'])
        self.amount = round(random.uniform(10, 5000), 2)
        self.transaction_date = fake.date_this_month()
        self.status = random.choice(['Success', 'Failed'])

    def to_dict(self) -> dict:
        return {
            'transaction_id': self.transaction_id,
            'customer_id': self.customer_id,
            'transaction_type': self.transaction_type,
            'amount': self.amount,
            'transaction_date': str(self.transaction_date),
            'status': self.status
        }
    
# 15. erp_loans
class CBSLoan:
    def __init__(self):
        self.loan_id = fake.random_int(min=1000, max=9999)
        self.customer_id = fake.random_int(min=1, max=99999)
        self.loan_type = random.choice(['Personal', 'Business', 'Mortgage'])
        self.amount = round(random.uniform(1000, 50000), 2)
        self.status = random.choice(['Approved', 'Rejected', 'Pending'])

    def to_dict(self) -> dict:
        return {
            'loan_id': self.loan_id,
            'customer_id': self.customer_id,
            'loan_type': self.loan_type,
            'amount': self.amount,
            'status': self.status
        }
