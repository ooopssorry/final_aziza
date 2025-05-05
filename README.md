# final_aziza
1. Database Setup (RDS - PostgreSQL)

Dataset Source: Custom-created CSV dataset (Aziza's revenue by region and quarter)

RDS Setup:

Engine: PostgreSQL

DB Instance Identifier: db_aziza

Master Username: postgres

Master Password: postgres

VPC: Default

Public Access: Enabled

Security Group: Same as EC2 security group (allows port 5432 access from EC2)

Database Name: postgresTable Name: tbl_aziza_data

Table Schema:

CREATE TABLE tbl_aziza_data (
  id SERIAL PRIMARY KEY,
  area VARCHAR(100),
  years VARCHAR(50),
  revenue BIGINT
);

Sample Data:

Asia, Q1-2023, 200000000

Europe, Q2-2023, 250000000

North America, Q3-2023, 300000000

South America, Q4-2023, 150000000

Africa, Q1-2024, 100000000

Imported using DBeaver.

2. S3 Static Hosting

S3 Bucket: webaziza3t

Static Website Settings:

Index Document: index_aziza.html

Permissions (Bucket Policy):

{
  "Version":"2012-10-17",
  "Statement":[{
    "Effect":"Allow",
    "Principal":"*",
    "Action":"s3:GetObject",
    "Resource":"arn:aws:s3:::webaziza3t/*"
  }]
}

Frontend Functionality:

Loads and displays all records from the database

Adds dummy data

Deletes the last row

HTML File: index_aziza.html

S3 Site URL: http://webaziza3t.s3-website-ap-southeast-1.amazonaws.com/index_aziza.html

3. EC2 Deployment (Flask Backend)

Instance Details:

Name: webapp_aziza

OS: Ubuntu 22.04

Type: t2.micro

Key Pair: webapp_aziza.pem

Security Group Inbound Rules:

SSH (22): 0.0.0.0/0

HTTP (80): 0.0.0.0/0

TCP (5000): 0.0.0.0/0

PostgreSQL (5432): EC2 security group

Project Folder: /home/ubuntu/webapp_aziza

Backend Code (app.py):

Connects to RDS instance via psycopg2

Flask endpoints: /data, /add, /delete

JSON API to serve data and allow modification

Run Command:

python3 app.py

URL: http://<47.129.34.34P>:5000

4. GitHub Repository

Repository URL: [https://github.com/ooopssorry/final_aziza]

Includes:

README.md with setup instructions

index_aziza.html

app.py

Dataset import SQL file

5. Application Verification Checklist



6. Naming Convention (As Required)

Database Name: db_aziza

Table Name: tbl_aziza_data

HTML File: index_aziza.html

Project Folder: webapp_aziza

Ready for Final Defense
