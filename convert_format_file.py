import pandas as pd
import json

# List of data strings
data_strings = [
    '{"Data": "{\\"Data\\": {\\"temperature\\": 25, \\"humidity\\": 50, \\"timestamp\\": 1645}}"}',
    # Add more data strings here if you have multiple data points
]

# Parse each data string, extract the nested JSON object, and store it in a list
nested_json_objects = []
for data_str in data_strings:
    data = json.loads(data_str)
    print(data)
    print(type(data))
    nested_json = json.loads(data["Data"])
    nested_json_objects.append(nested_json)

# Create a DataFrame from the list of nested JSON objects
df = pd.DataFrame(nested_json_objects)

# Save the DataFrame as a Parquet file
df.to_parquet('data.parquet', index=False)