import boto3
import json

s3_resource = boto3.resource('s3')
s3_client = boto3.client('s3')

def put_obj_to_s3(s3_resource, bucket_name, bucket_key, file_content):
    s3_resource.Object(bucket_name, bucket_key).put(Body=json.dumps(file_content))

def put_obj_s3_client(s3_client, bucket_name, bucket_key, file_content):
    s3_client.put_object(Bucket=bucket_name, Key=bucket_key, Body=json.dumps(file_content))

def lambda_handler():
    json_content = {'1': '2'}
    put_obj_to_s3(s3_resource, 'app-bucket', 'obj-key', json_content)
    put_obj_s3_client(s3_client, 'app-bucket', 'obj-key', json_content)
