import base64
import json

data = {
    "YYYY": "2021",
    "MM": "01",
    "DD": "01",
    "HH": "01",
    "client_id": "123456"
}

# Convert the data to a JSON string
data_str = json.dumps(data)

# Encode the JSON string to Base64
data_bytes = data_str.encode('utf-8')
base64_bytes = base64.b64encode(data_bytes)
base64_str = base64_bytes.decode('utf-8')

print(base64_str)