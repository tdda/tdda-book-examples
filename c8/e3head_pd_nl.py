import pandas
df = pandas.read_parquet('elements3-old.parquet',
                         dtype_backend='numpy_nullable')
print(df)
print([str(df[c].dtype) for c in df])
