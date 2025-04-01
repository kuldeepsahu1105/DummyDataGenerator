-- Create Databases
CREATE DATABASE core_banking_db;
CREATE DATABASE HRMS;

-- Use core_banking_db
USE core_banking_db;

-- Customers Table
DROP TABLE IF EXISTS customers;
CREATE EXTERNAL TABLE customers (
    customer_id INT,
    customer_fname STRING,
    customer_lname STRING,
    gender STRING,
    kyc_status STRING,
    customer_type STRING,
    relationship_manager_id INT,
    email STRING,
    phone STRING,
    address STRING,
    city STRING,
    state STRING,
    postal_code STRING,
    country STRING,
    status STRING,
    source STRING,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    date_of_birth DATE,
    account_open_date DATE
) STORED BY ICEBERG
LOCATION 's3://${s3_bucket_name}/core_banking/customers/';
