import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):

    bucket = '<bucket>'
    key = 'test1.json'

    try:
        data = s3.get_object(Bucket=bucket, Key=key)
        json_data = data['Body'].read()

        return json_data

    except Exception as e:
        print(e)
        raise e
