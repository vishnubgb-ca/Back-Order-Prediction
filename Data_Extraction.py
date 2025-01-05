
import os
import boto3
import pandas as pd
from io import StringIO

# Get AWS credentials from environment variables
aws_access_key_id = os.environ.get("aws_access_key_id")
aws_secret_access_key = os.environ.get("aws_secret_access_key")
bucket = os.environ.get("bucket")
region = os.environ.get("region")

# Check if all the credentials are available
if not all([aws_access_key_id, aws_secret_access_key, bucket, region]):
    print("Please set all the environment variables: aws_access_key_id, aws_secret_access_key, bucket, region")
    exit(1)

# Create a session using your credentials
session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region
)

# Create an S3 resource object using the session
s3 = session.resource("s3")

# Get the bucket object
bucket_obj = s3.Bucket(bucket)

# Assume that the file is a CSV file
for obj in bucket_obj.objects.all():
    if obj.key.endswith(".csv"):
        csv_obj = s3.Object(bucket, obj.key)
        csv_data = csv_obj.get().get("Body").read().decode("utf-8")
        data = pd.read_csv(StringIO(csv_data))
        break

# Save the data to a CSV file
data.to_csv("data.csv", index=False)

# Display the top 5 rows
print(data.head())


