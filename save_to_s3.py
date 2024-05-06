
import boto3

# Your timestamp string
timestamp = "2024-05-06-09-10-01"
file = "data.parquet"

# Parse the timestamp string into its individual components
year, month, day, hour, minute, second = timestamp.split("-")

# Construct the S3 key with the desired prefix
s3_prefix = f"{year}/{month}/{day}/data.parquet"

# Instantiate the S3 client
s3_client = boto3.client('s3')

# Upload the file to S3 with the constructed key
s3_client.upload_file('./data.parquet', 'iot-parquet-data', s3_prefix)