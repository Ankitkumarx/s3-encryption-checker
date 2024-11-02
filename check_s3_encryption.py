import boto3

# Defining the Required Encryption Algorithm
REQUIRED_ENCRYPTION_ALGORITHM = "aws:kms"

s3_client = boto3.client("s3")

# Function to Check Bucket Encryption

def check_bucket_encryption(bucket_name):
    try:
        encryption = s3_client.get_bucket_encryption(Bucket=bucket_name)
        return encryption['ServerSideEncryptionConfiguration']['Rules'][0]['ApplyServerSideEncryptionByDefault']['SSEAlgorithm'] == REQUIRED_ENCRYPTION_ALGORITHM

    except Exception as e:
        print(f"Error checking encryption for {bucket_name}: {e}")
        return False
    
# Function to Enforce Bucket Encryption    

def enforce_bucket_encryption(bucket_name):
    s3_client.put_bucket_encryption(
        Bucket=bucket_name,
        ServerSideEncryptionConfiguration={
            "Rules": [{
                "ApplyServerSideEncryptionByDefault": {
                    "SSEAlgorithm": REQUIRED_ENCRYPTION_ALGORITHM
                }
            }]
        }
    )
    print(f"Applied encryption to bucket '{bucket_name}'.")

    # Main Function

def main():
    buckets = s3_client.list_buckets()["Buckets"]
    for bucket in buckets:
        bucket_name = bucket["Name"]
        print(f"Checking bucket: {bucket_name}")
        if not check_bucket_encryption(bucket_name):
            enforce_bucket_encryption(bucket_name)

# Run function

if __name__ == "__main__":
    main()
