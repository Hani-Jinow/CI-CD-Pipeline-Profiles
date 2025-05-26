import pandas as pd
import sys

df = pd.read_csv('profiles1.csv')

df.to_json('data.json', orient='records', indent=2)

print('CSV-file has converted to JSON')