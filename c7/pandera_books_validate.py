import pandas as pd
import pandera as pa
from pandera_books_schema import schema

for path in ('books.parquet', 'books2.parquet'):
    df = pd.read_parquet(path, dtype_backend='numpy_nullable')
    try:
        vdf = schema.validate(df, lazy=True)
        print(f'{path} OK')
    except pa.errors.SchemaErrors as error:
        print(f'{path} Errors:\n{error}')

