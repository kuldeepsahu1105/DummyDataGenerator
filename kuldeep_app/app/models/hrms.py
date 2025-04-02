from faker import Faker
import random
from datetime import datetime

fake = Faker()

# --- HRMS Tables ---

# 18. hrms_employees
class HRMSEmployee:
    def __init__(self):
        self.employee_id = fake.random_int(min=1, max=99999)
        self.first_name = fake.first_name()
        self.last_name = fake.last_name()
        self.email = fake.email()
        self.phone = fake.phone_number()
        self.department = random.choice(['Sales', 'Operations', 'IT', 'Finance', 'HR'])
        self.position = random.choice(['Manager', 'Associate', 'Director', 'Executive', 'Teller', 'Customer Service'])
        self.hire_date = fake.date_this_decade().isoformat()  # Should be a datetime object in actual DB
        self.salary = round(random.uniform(25000, 120000), 2)
        self.status = random.choice(['Active', 'Inactive'])
        self.branch_id = fake.random_int(min=1000, max=9999)

    def to_dict(self) -> dict:
        return {
            'employee_id': self.employee_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'phone': self.phone,
            'department': self.department,
            'position': self.position,
            'hire_date': self.hire_date,  # Use datetime here for precision
            'salary': self.salary,
            'status': self.status,
            'branch_id': self.branch_id,
        }

# 19. hrms_attendance
class HRMSAttendance:
    def __init__(self):
        self.attendance_id = fake.random_int(min=1000, max=99999)
        self.employee_id = fake.random_int(min=1, max=99999)
        self.date = fake.date_this_month().isoformat()  # Should be a datetime object
        self.status = random.choice(['Present', 'Absent'])

    def to_dict(self) -> dict:
        return {
            'attendance_id': self.attendance_id,
            'employee_id': self.employee_id,
            'date': self.date,  # Keep as datetime object for consistency
            'status': self.status
        }
    
# 27. hrms_time_tracking
class HRMSTimeTracking:
    def __init__(self):
        self.time_tracking_id = fake.random_int(min=1000, max=99999)
        self.employee_id = fake.random_int(min=1, max=99999)
        self.date = fake.date_this_month().isoformat()  # Should be a datetime object
        self.hours_worked = round(random.uniform(4, 10), 2)
        self.overtime_hours = round(random.uniform(0, 3), 2)
        self.status = random.choice(['Approved', 'Pending', 'Rejected'])

    def to_dict(self) -> dict:
        return {
            'time_tracking_id': self.time_tracking_id,
            'employee_id': self.employee_id,
            'date': self.date,  # Keep as datetime object
            'hours_worked': self.hours_worked,
            'overtime_hours': self.overtime_hours,
            'status': self.status
        }

#21. hrms_performance
class HRMSPerformance:
    def __init__(self):
        self.performance_id = fake.random_int(min=1000, max=99999)
        self.employee_id = fake.random_int(min=1, max=99999)
        self.performance_rating = random.choice([1, 2, 3, 4, 5])
        self.review_date = fake.date_this_year().isoformat()  # Should be a datetime object
        self.comments = fake.text(max_nb_chars=150)

    def to_dict(self) -> dict:
        return {
            'performance_id': self.performance_id,
            'employee_id': self.employee_id,
            'performance_rating': self.performance_rating,
            'review_date': self.review_date,  # Keep as datetime object
            'comments': self.comments
        }
