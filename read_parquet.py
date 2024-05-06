import pandas as pd

def read_parquet_file(file_path):
    # Read the Parquet file
    df = pd.read_parquet(file_path, engine='pyarrow')
    
    return df

# Example usage
file_path = 'data.parquet'
df = read_parquet_file(file_path)
print(df)