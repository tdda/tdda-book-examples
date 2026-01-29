import pandas
df = pandas.read_parquet('elements3-old.parquet')
print(df)
print([str(df[c].dtype) for c in df])
