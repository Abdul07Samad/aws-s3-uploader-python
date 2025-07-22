# 🗂️ AWS S3 Uploader with Python (Boto3)

This is a simple Python script to upload local files to an AWS S3 bucket using the Boto3 library.

## ✅ Features

- Upload any local file to AWS S3
- Uses AWS CLI credentials (already configured)
- Command-line and Python script both supported
- Clean error handling (missing file, credentials, permission errors)

## 🛠️ Requirements

- Python 3.x
- Boto3 (`pip install boto3`)
- AWS credentials configured via `aws configure`

## 📁 File Structure

aws-s3-uploader-python/
│
├── s3_checker.py # Main Python script to upload a file
├── requirements.txt # Python dependencies
└── README.md # This file
