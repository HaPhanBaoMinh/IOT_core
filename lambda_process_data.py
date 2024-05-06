import boto3
import json
import pandas as pd
import ast

def correct_json_format(json_str):
    keys = ['temperature', 'humidity', 'timestamp']
    for key in keys:
        json_str = json_str.replace(f'{key}:', f'"{key}":')
    return json_str

def handle ():
    raw_bucket_name = 'iot-raw-data'
    formatted_bucket_name = 'iot-parquet-data'
    time_stamp_hour = '2024/05/06/10'
    time_stamp_day = time_stamp_hour.split('/')[0] + '/' + time_stamp_hour.split('/')[1] + '/' + time_stamp_hour.split('/')[2]
    s3_prefix = time_stamp_day + '/data_format.parquet'
    
    raw_data_files_in_one_day = []
    raw_data = []
    json_data = []
    nested_json_objects = []


    # Get all the objects in 1 days in the bucket
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(raw_bucket_name)
    for obj in bucket.objects.all():
        if obj.key.startswith('raw-data/' + time_stamp_hour + '/'):
            raw_data_files_in_one_day.append(obj.key)

    # Read the content of files
    s3_client = boto3.client('s3')
    for file in raw_data_files_in_one_day:
        obj = s3_client.get_object(Bucket=raw_bucket_name, Key=file)
        data = obj['Body'].read().decode('utf-8')
        raw_data.append(data)

   

handle()