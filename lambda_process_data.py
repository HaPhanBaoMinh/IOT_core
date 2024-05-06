import boto3
import json
import pandas as pd

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

    # Process the raw data
    for data in raw_data:
        parsed_json = json.loads(data)
        nested_json_str = "".join(parsed_json.values())
        desired_json_str = json.dumps(nested_json_str)
        json_data.append(desired_json_str)

    for json_str in json_data:
        # Remove surrounding quotes and braces, then parse the inner JSON string
        inner_json_str = json_str.strip('"').split(':', 1)[1].strip()
        print(json_str)
        json_data = correct_json_format(inner_json_str)
        # print(json_data)
        


    # df = pd.DataFrame(nested_json_objects)
    # df.to_parquet('data.parquet', index=False)

    # # Upload the file to S3 with the constructed key
    # s3_client.upload_file('./data.parquet', formatted_bucket_name, s3_prefix)

handle()