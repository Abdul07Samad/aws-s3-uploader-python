import boto3
from botocore.exceptions import ClientError
import os

def check_or_create_bucket(bucket_name, region="ap-south-1"):
    s3 = boto3.client('s3', region_name=region)
    try:
        s3.head_bucket(Bucket=bucket_name)
        print(f"ℹ️ Bucket '{bucket_name}' already exists.")
    except ClientError as e:
        error_code = int(e.response['Error']['Code'])
        if error_code == 404:
            try:
                s3.create_bucket(
                    Bucket=bucket_name,
                    CreateBucketConfiguration={'LocationConstraint': region}
                )
                print(f"✅ Bucket '{bucket_name}' created.")
            except ClientError as ce:
                print(f"❌ Error creating bucket: {ce}")
        else:
            print(f"❌ Unexpected error checking bucket: {e}")

def upload_file(file_path, bucket_name, object_name=None):
    s3 = boto3.client('s3')
    if object_name is None:
        object_name = os.path.basename(file_path)

    try:
        s3.upload_file(file_path, bucket_name, object_name)
        print(f"✅ File '{file_path}' uploaded to '{bucket_name}/{object_name}'")
    except ClientError as e:
        print(f"❌ Upload failed: {e}")

if __name__ == "__main__":
    bucket = "my-upload-test-123"
    folder_path = "C:/Users/Administrator/OneDrive/Desktop/aws-s3-uploader-python/upload aws files"

    check_or_create_bucket(bucket)

    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)
        if os.path.isfile(full_path):
            upload_file(full_path, bucket)

