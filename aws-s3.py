# S3 try-out. Print all buckets in an S3 account. 
import boto3 

# Initialize Boto3 for AWS S3 
client = boto3.client('s3') 

# Define S3 Bucket name as variable 
bucket = 'test-bucket-name-json-dump-chargebee.src' 
# To use Boto 3, you must first import it and tell it what service you are going to use
s3 = boto3.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)