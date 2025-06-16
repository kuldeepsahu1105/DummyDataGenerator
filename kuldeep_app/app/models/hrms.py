from faker import Faker
import random
from datetime import datetime

fake = Faker()

# --- HRMS Tables ---

# 18. hrms_employees
class HRMSEmployee:
    def __init__(self):
        self.employee_id = fake.random_int(min=1, max=99)
        self.first_name = fake.first_name()
        self.last_name = fake.last_name()
        self.email = fake.email()
        self.phone = fake.phone_number()
        self.department = random.choice(['Sales', 'Operations', 'IT', 'Finance', 'HR'])
        self.position = random.choice(['Manager', 'Associate', 'Director', 'Executive', 'Teller', 'Customer Service'])
        self.hire_date = fake.date_this_decade().strftime("%Y-%m-%d")  # Keep as DATE format
        self.salary = round(random.uniform(25000, 120000), 2)
        self.employee_status = random.choice(['Active', 'Inactive'])
        self.branch_id = fake.random_int(min=1, max=99)
        self.created_at = fake.date_time_this_decade().strftime("%Y-%m-%d %H:%M:%S")  # Formatted timestamp
        self.updated_at = fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S")  # Formatted timestamp

    def to_dict(self) -> dict:
        return self.__dict__

# 19. hrms_attendance
class HRMSAttendance:
    def __init__(self):
        self.attendance_id = fake.random_int(min=1, max=99)
        self.employee_id = fake.random_int(min=1, max=99)
        self.attendance_date = fake.date_this_month().strftime("%Y-%m-%d")  # Keep as DATE format
        self.attendance_status = random.choice(['Present', 'Absent'])
        self.created_at = fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S")  # Formatted timestamp

    def to_dict(self) -> dict:
        return self.__dict__
    
# 27. hrms_time_tracking
class HRMSTimeTracking:
    def __init__(self):
        self.time_tracking_id = fake.random_int(min=1, max=99)
        self.employee_id = fake.random_int(min=1, max=99)
        self.tracking_date = fake.date_this_month().strftime("%Y-%m-%d")  # Keep as DATE format
        self.hours_worked = round(random.uniform(4, 10), 2)
        self.overtime_hours = round(random.uniform(0, 3), 2)
        self.time_tracking_status = random.choice(['Approved', 'Pending', 'Rejected'])
        self.created_at = fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S")  # Formatted timestamp

    def to_dict(self) -> dict:
        return self.__dict__

# 21. hrms_performance
class HRMSPerformance:
    def __init__(self):
        self.performance_id = fake.random_int(min=1, max=99)
        self.employee_id = fake.random_int(min=1, max=99)
        self.performance_rating = random.choice([1, 2, 3, 4, 5])
        self.review_date = fake.date_this_year().strftime("%Y-%m-%d")  # Keep as DATE format
        self.comments = fake.text(max_nb_chars=150)
        self.created_at = fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S")  # Formatted timestamp

    def to_dict(self) -> dict:
        return self.__dict__