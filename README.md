# S3 Encryption Checker

**S3 Encryption Checker** is a Python script designed to scan all Amazon S3 buckets within your AWS account and verify their compliance with organizational encryption policies. This tool helps ensure that sensitive data stored in S3 is adequately protected by checking whether server-side encryption is enabled for each bucket.

## Table of Contents

- [Description](#description)
- [Prerequisites](#prerequisites)
- [Setup AWS Credentials](#setup-aws-credentials)
- [Installation](#installation)
- [Usage](#usage)
- [Output](#output)
- [License](#license)
- [Contributing](#contributing)
- [Author](#author)

## Description

This Python script scans all S3 buckets in your AWS account to ensure they comply with your organization's encryption policies. It provides a quick and efficient way to identify unencrypted buckets and maintain security standards.

### Features:

- **Automated Scanning**: Quickly scans all S3 buckets in your AWS account.
- **Encryption Status Reporting**: Provides clear output on whether each bucket is encrypted or not.
- **Error Handling**: Gracefully handles errors, such as permissions issues or missing encryption configurations.
- **Easy Setup**: Simple installation and configuration process, leveraging the `boto3` library for AWS interactions.

### Use Cases:

- Ensure compliance with internal security policies and regulations.
- Identify unencrypted S3 buckets that may pose a security risk.
- Automate the auditing process for AWS S3 bucket encryption.

## Prerequisites

- Python 3.x
- `boto3` library

## Setup AWS Credentials

Before running the script, you need to configure your AWS credentials. You can do this in one of the following ways:

1. Using AWS CLI:
   - Install the AWS CLI and configure your credentials by running:
     ```
     aws configure
     ```
   This will prompt you for your AWS Access Key ID, Secret Access Key, region, and output format.

2. Using Environment Variables:
   - Set the following environment variables in your shell:
     ```
     export AWS_ACCESS_KEY_ID=your_access_key
     export AWS_SECRET_ACCESS_KEY=your_secret_key
     export AWS_DEFAULT_REGION=your_region  # optional
     ```

## Installation

1. Clone the repository or download the script:

   ```
   git clone https://github.com/Ankitkumarx/s3-encryption-checker.git
   cd s3-encryption-checker
