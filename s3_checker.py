import boto3
from botocore.exceptions import NoCredentialsError, ClientError

def upload_file_to_s3(file_path, bucket_name, object_name=None):
    s3 = boto3.client('s3')

    if object_name is None:
        object_name = file_path.split("/")[-1]

    try:
        s3.upload_file(file_path, bucket_name, object_name)
        print(f"✅ File '{file_path}' uploaded to '{bucket_name}/{object_name}' successfully.")
    except FileNotFoundError:
        print("❌ File not found.")
    except NoCredentialsError:
        print("❌ AWS credentials not found.")
    except ClientError as e:
        print(f"❌ Upload failed: {e}")

if __name__ == "__main__":
    # ✅ Customize your file path and bucket here
    upload_file_to_s3(
        file_path="C:/Users/Administrator/OneDrive/Desktop/test.txt",
        bucket_name="mera-pehla-bucket-2025"
    )
