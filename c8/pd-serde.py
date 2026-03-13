import pandas as pd
from tdda.serial import csv_to_pandas, pandas_to_csv
df = pd.DataFrame({'n': [1, 2],'f': [1.5, None],'s': ['à', 'é']})
print(df)
print(pandas_to_csv(df,'simple3x2.csv', md_outpath='simple3x2.serial'))
