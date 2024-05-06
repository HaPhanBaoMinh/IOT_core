# Run clouformation script
awslocal cloudformation create-stack --stack-name iot-firehose --template-body file://kinesis.yaml
awslocal cloudformation create-stack --stack-name iot-core --template-body file://iot_core.yaml

# Check the status of the stack
awslocal cloudformation describe-stacks --stack-name iot-firehose
awslocal cloudformation describe-stacks --stack-name iot-core

# Delete the stack
awslocal cloudformation delete-stack --stack-name iot-firehose
awslocal cloudformation delete-stack --stack-name iot-core

# put records in the stream
awslocal firehose put-record --delivery-stream-name iot-delivery-stream --record '{"Data":"{\"temperature\": 25, \"humidity\": 50, \"timestamp\": 1645}"}'

# List object in the bucket CLi v2
awslocal s3api list-objects --bucket iot-raw-data

# Remove object from the bucket
awslocal s3api delete-object --bucket iot-raw-data --key 'key'

# Get iot endpoint
awslocal iot describe-endpoint

# List Delivery Stream
awslocal firehose list-delivery-streams

# Send data to the delivery stream
mosquitto_pub --host 000000000000.iot.us-east-1.localhost.localstack.cloud --port 4510 --topic iot-delivery-stream -m '{"Data":"{"temperature": 25, "humidity": 50, "timestamp": 1645}"}'

# List topics rules
awslocal iot list-topic-rules

# Detail of the topic rule
awslocal iot get-topic-rule --rule-name iot-to-firehose-rule

# Start IOT endpoint
awslocal iot describe-endpoint

# Create S3 bucket
awslocal s3api create-bucket --bucket iot-parquet-data