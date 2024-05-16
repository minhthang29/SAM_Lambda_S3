import json
import boto3

def lambda_handler(event, context):
    bucket_name = 'stephen-test-bucket2'
    file_name = 'person1.txt'
    file_content = b'Hello, world!'
    
    s3 = boto3.client('s3')

    try:
        response = s3.put_object(Bucket=bucket_name, Key=file_name, Body=file_content)
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "File uploaded successfully!",
                "file_name": file_name,
                "bucket_name": bucket_name
            })
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": "File upload failed",
                "error": str(e)
            })
        }
