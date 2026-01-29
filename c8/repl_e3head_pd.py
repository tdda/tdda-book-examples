print('>>>', '''import pandas''')
import pandas
print('>>>', '''df = pandas.read_parquet('elements3-old.parquet')''')
df = pandas.read_parquet('elements3-old.parquet')
print('>>>', '''df''')
print(df)
print('>>>', '''[str(df[c].dtype) for c in df]''')
print([str(df[c].dtype) for c in df])
