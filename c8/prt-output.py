>>> import pandas as pd
>>> df = pd.DataFrame({'a': pd.Series([1, None], dtype='Int64')})
>>> df
      a
0     1
1  <NA>
>>> df.to_csv('/tmp/a.csv')
>>> df2 = pd.read_csv('/tmp/a.csv')
>>> df2
   Unnamed: 0    a
0           0  1.0
1           1  NaN
>>> 
