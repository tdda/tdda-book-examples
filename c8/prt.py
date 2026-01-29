import pandas as pd
df = pd.DataFrame({'a': pd.Series([1, None], dtype='Int64')})
print(df)
df.to_csv('/tmp/a.csv')
df2 = pd.read_csv('/tmp/a.csv')
print(df2)

