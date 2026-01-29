print('>>>', '''import polars''')
import polars
print('>>>', '''df = polars.read_parquet('elements3-old.parquet')''')
df = polars.read_parquet('elements3-old.parquet')
print('>>>', '''df''')
print(df)
