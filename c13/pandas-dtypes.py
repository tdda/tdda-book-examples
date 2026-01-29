import pandas as pd
import numpy as np
from datetime import datetime

df = pd.DataFrame({
     'b': [False, True, None],
     'i': [2, 3, None],
     'f': [0.0, 1.1, None],
     's': ['One', 'Two', None],
     'd': [
        datetime(2000, 1, 2, 12, 34, 56),
        datetime(2000, 1, 2, 12, 34, 57),
        None
     ],
     'B': pd.Series([False, True, None], dtype='boolean'),
     'I': pd.Series([2, 3, None], dtype='Int64'),
     'S': pd.Series(['One', 'Two', None], dtype='string')
})
print('INFO:\n=====')
df.info()
print(f'\nDATAFRAME:\n==========\n{df}')
print('\nDTYPES:\n======')
for c in (df):
    print(f'{c}: {(df[c].dtype.__class__.__name__)}')
print(f'\nNULL TYPES:\n===========')
for i, c in enumerate(list(df)):
    print((c, type(df.iat[2,i]), df.iat[2,i]))
