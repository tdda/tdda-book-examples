print('>>>', '''import polars''')
import polars
print('>>>', '''df = polars.read_csv('elements3-old.csv')''')
df = polars.read_csv('elements3-old.csv')
print('>>>', '''df''')
print(df)
