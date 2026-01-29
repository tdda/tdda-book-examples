import pandas as pd

df = pd.read_parquet('books.parquet')
with open('books.txt', 'w') as f:
    f.write(str(df))


