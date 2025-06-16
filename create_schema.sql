-- Create Databases
CREATE DATABASE IF NOT EXISTS core_banking_db;
CREATE DATABASE IF NOT EXISTS HRMS;

-- Use core_banking_db
USE core_banking_db;

-- Customers Table

DROP TABLE IF EXISTS core_banking_db.customer;

CREATE EXTERNAL TABLE core_banking_db.customer (
  address STRING COMMENT 'Customer address.',
  city STRING COMMENT 'City of residence.',
  country STRING COMMENT 'Country.',
  created_at STRING COMMENT 'Creation timestamp (string format).',
  customer_id INT COMMENT 'Customer ID.',
  customer_status STRING COMMENT 'Customer status.',
  customer_type STRING COMMENT 'Customer type.',
  dob STRING COMMENT 'Date of birth (YYYY-MM-DD as string).',
  email STRING COMMENT 'Email address.',
  first_name STRING COMMENT 'First name.',
  gender STRING COMMENT 'Gender.',
  kyc_status STRING COMMENT 'KYC verification status.',
  last_name STRING COMMENT 'Last name.',
  phone STRING COMMENT 'Phone number.',
  postal_code STRING COMMENT 'Postal code.',
  relationship_manager_id INT COMMENT 'ID of assigned relationship manager.',
  source STRING COMMENT 'Source of onboarding.',
  state STRING COMMENT 'State.',
  updated_at STRING COMMENT 'Last update timestamp (string format).'
)
ROW FORMAT SERDE
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
STORED AS INPUTFORMAT
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION 's3a://${s3_bucket_name}/user/ksahu/CBS/customer/';

SELECT * FROM core_banking_db.customer LIMIT 10;

-- Accounts Table
DROP TABLE IF EXISTS core_banking_db.account;

CREATE EXTERNAL TABLE core_banking_db.account (
    account_id INT COMMENT 'Account ID',
    account_number INT COMMENT 'Account Number',
    account_status STRING COMMENT 'Account Status',
    account_type STRING COMMENT 'Account Type',
    balance DOUBLE COMMENT 'Balance',
    branch_id INT COMMENT 'Branch ID',
    created_at STRING COMMENT 'Created At',
    currency_type STRING COMMENT 'Currency Type',
    customer_id INT COMMENT 'Customer ID',
    interest_rate DOUBLE COMMENT 'Interest Rate',
    last_transaction_date STRING COMMENT 'Last Transaction Date'
)
STORED AS PARQUET
LOCATION 's3a://project-axon-buk-364703ca/user/ksahu/CBS/account/';

SELECT * from core_banking_db.account LIMIT 10;

-- Transactions Table
DROP TABLE IF EXISTS core_banking_db.transaction;

CREATE EXTERNAL TABLE core_banking_db.transaction (
    account_number INT COMMENT 'Account Number',
    amount DOUBLE COMMENT 'Transaction Amount',
    branch_id INT COMMENT 'Branch ID',
    currency_type STRING COMMENT 'Currency Type',
    description STRING COMMENT 'Transaction Description',
    transaction_date STRING COMMENT 'Transaction Date',
    transaction_due_date STRING COMMENT 'Transaction Due Date',
    transaction_id INT COMMENT 'Transaction ID',
    transaction_mode STRING COMMENT 'Transaction Mode',
    transaction_reference_id STRING COMMENT 'Reference ID',
    transaction_status STRING COMMENT 'Transaction Status',
    transaction_type STRING COMMENT 'Transaction Type'
)
STORED AS PARQUET
LOCATION 's3a://${s3_bucket_name}/user/ksahu/CBS/transaction/';

SELECT * FROM core_banking_db.transaction LIMIT 10;

-- Loans Table
DROP TABLE IF EXISTS core_banking_db.loan;

CREATE EXTERNAL TABLE core_banking_db.loan (
  account_number INT COMMENT 'Account number.',
  customer_id INT COMMENT 'Customer ID.',
  emi_amount DOUBLE COMMENT 'EMI amount.',  -- DOUBLE to match 31552.72
  end_date STRING COMMENT 'Loan end date (string format).',
  interest_rate DOUBLE COMMENT 'Interest rate.',
  loan_id INT COMMENT 'Loan ID.',
  loan_status STRING COMMENT 'Loan status.',
  loan_type STRING COMMENT 'Loan type.',
  outstanding_balance DOUBLE COMMENT 'Outstanding balance.',
  principal_amount DOUBLE COMMENT 'Principal amount.',
  start_date STRING COMMENT 'Loan start date (string format).'
)
ROW FORMAT SERDE
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
STORED AS INPUTFORMAT
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION 's3a://${s3_bucket_name}/user/ksahu/CBS/loan/';

SELECT * FROM core_banking_db.loan LIMIT 10;

-- Feedback Table
DROP TABLE IF EXISTS core_banking_db.feedback;

CREATE EXTERNAL TABLE core_banking_db.feedback (
    branch_id INT COMMENT 'Branch ID',
    customer_id INT COMMENT 'Customer ID',
    feedback_comment STRING COMMENT 'Feedback Comment',
    feedback_date STRING COMMENT 'Feedback Date',
    feedback_id INT COMMENT 'Feedback ID',
    feedback_rating INT COMMENT 'Feedback Rating',
    feedback_status STRING COMMENT 'Feedback Status',
    feedback_type STRING COMMENT 'Feedback Type'
)
STORED AS PARQUET
LOCATION 's3a://project-axon-buk-364703ca/user/ksahu/CBS/feedback/';

SELECT * FROM core_banking_db.feedback LIMIT 10;    

-- HRMS Tables
USE HRMS;

-- HRMS Attendance Table
DROP TABLE IF EXISTS hrms.hrms_employee;

CREATE EXTERNAL TABLE hrms.hrms_employee (
    branch_id INT COMMENT 'Branch ID',
    created_at STRING COMMENT 'Created At (Stored as STRING for Hive compatibility)',
    department STRING COMMENT 'Department',
    email STRING COMMENT 'Email',
    employee_id INT COMMENT 'Employee ID',
    employee_status STRING COMMENT 'Status',
    first_name STRING COMMENT 'First Name',
    hire_date STRING COMMENT 'Hire Date (Stored as STRING for Hive compatibility)',
    last_name STRING COMMENT 'Last Name',
    phone STRING COMMENT 'Phone',
    position STRING COMMENT 'Position',
    salary DOUBLE COMMENT 'Salary',
    updated_at STRING COMMENT 'Updated At (Stored as STRING for Hive compatibility)'
)
STORED AS PARQUET
LOCATION 's3a://project-axon-buk-364703ca/user/ksahu/HRMS/employee/';

SELECT * FROM hrms.hrms_employee LIMIT 10;

-- HRMS Attendance Table
DROP TABLE IF EXISTS hrms.hrms_attendance;
CREATE EXTERNAL TABLE hrms.hrms_attendance (
    attendance_date STRING COMMENT 'Attendance Date (Stored as STRING for Hive compatibility)',
    attendance_id INT COMMENT 'Attendance ID',
    attendance_status STRING COMMENT 'Status',
    created_at STRING COMMENT 'Created At (Stored as STRING for Hive compatibility)',
    employee_id INT COMMENT 'Employee ID'
)
ROW FORMAT SERDE
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
STORED AS INPUTFORMAT
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION 's3a://${s3_bucket_name}/user/ksahu/HRMS/attendance/';

SELECT * FROM hrms.hrms_attendance LIMIT 10;

-- HRMS Time Tracking Table
DROP TABLE IF EXISTS hrms.hrms_time_tracking;

CREATE EXTERNAL TABLE hrms.hrms_time_tracking (
    created_at STRING COMMENT 'Created At (Stored as STRING for Hive compatibility)',
    employee_id INT COMMENT 'Employee ID',
    hours_worked DOUBLE COMMENT 'Hours Worked',
    overtime_hours DOUBLE COMMENT 'Overtime Hours',
    time_tracking_id INT COMMENT 'Time Tracking ID',
    tracking_date STRING COMMENT 'Tracking Date (Stored as STRING for Hive compatibility)',
    time_tracking_status STRING COMMENT 'Status'
)
STORED AS PARQUET
LOCATION 's3a://project-axon-buk-364703ca/user/ksahu/HRMS/timetracking/';
SELECT * FROM hrms.hrms_time_tracking LIMIT 10;

-- HRMS Performance Table
DROP TABLE IF EXISTS hrms.hrms_performance;
CREATE EXTERNAL TABLE hrms.hrms_performance (
    comments STRING COMMENT 'Feedback comments',
    created_at STRING COMMENT 'Created At (Stored as STRING for Hive compatibility)',
    employee_id INT COMMENT 'Employee ID',
    performance_id INT COMMENT 'Performance ID',
    performance_rating INT COMMENT 'Performance Rating',
    review_date STRING COMMENT 'Review Period (Stored as STRING for Hive compatibility)'
)
STORED AS PARQUET
LOCATION 's3a://${s3_bucket_name}/user/ksahu/HRMS/performance/';

-- Sample Queries to Test the Tables
-- Select 10 records from each table to verify the schema
USE core_banking_db;
SELECT * FROM customers LIMIT 10;
SELECT * FROM accounts LIMIT 10;
SELECT * FROM transactions LIMIT 10;
SELECT * FROM loans LIMIT 10;               
SELECT * FROM feedback LIMIT 10;
USE HRMS;
SELECT * FROM hrms_employees LIMIT 10;
SELECT * FROM hrms_attendance LIMIT 10;
SELECT * FROM hrms_time_tracking LIMIT 10;
SELECT * FROM hrms_performance LIMIT 10;
-- End of SQL Script

-- Note: Replace `${s3_bucket_name}` with the actual S3 bucket name where the data is stored.
-- The above SQL script creates the necessary tables for a core banking system and HRMS in Hive.
-- It also includes sample queries to test the created tables.
-- Ensure to run this script in an environment where Hive is configured to access the specified S3 bucket.
-- The script uses Hive's external table feature to create tables that point to data stored in S3.
-- The tables are created with appropriate data types and comments for better understanding.
-- The script also includes the necessary DROP TABLE statements to ensure that existing tables are removed before creating new ones.
-- This is important to avoid conflicts and ensure that the latest schema is used.