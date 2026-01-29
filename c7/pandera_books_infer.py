import pandas as pd
import pandera.pandas as pa

df = pd.read_parquet('books.parquet', dtype_backend='numpy_nullable')
schema = pa.infer_schema(df)
with open('pandera_books_schema.py', 'w') as f:
    f.write(schema.to_script())
