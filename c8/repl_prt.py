print('>>>', '''import pandas as pd''')
import pandas as pd
print('>>>', '''df = pd.DataFrame({'a': pd.Series([1, None], dtype='Int64')})''')
df = pd.DataFrame({'a': pd.Series([1, None], dtype='Int64')})
print('>>>', '''df''')
print(df)
print('>>>', '''df.to_csv('/tmp/a.csv')''')
df.to_csv('/tmp/a.csv')
print('>>>', '''df2 = pd.read_csv('/tmp/a.csv')''')
df2 = pd.read_csv('/tmp/a.csv')
print('>>>', '''df2''')
print(df2)
print('>>>', '''''')

