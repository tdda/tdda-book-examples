import pandas as pd

df = pd.read_parquet('us-states.parquet')
with open('us-states-head.txt', 'w') as f:
    f.write(str(df.head()))


