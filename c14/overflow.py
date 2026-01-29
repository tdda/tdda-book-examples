import numpy as np
import pandas as pd

np.seterr(over='warn')

dtypes = (
      [f'int{k}'  for k in (16, 32, 64)]
    + [f'uint{k}' for k in (16, 32, 64)]
)
powers = [7, 8, 15, 16, 31, 32, 63, 64]
df = pd.DataFrame({'k': powers})

for d in dtypes:
    df[d] = np.array(np.power(2, df['k']).astype(d))
print(df.to_string(index=None, line_width=90), end='\n\n')

df['overflow64'] = df['int64'] + np.where(df['int64'] < 0, -1, 1)
ints = [2**k for k in powers]
df['no_overflow'] = [f'{v + (-1 if v < 0 else 1):,}' for v in ints]
print(df[['int64', 'overflow64', 'no_overflow']]
      .to_string(index=None, line_width=90),
      end='\n\n')

v = np.int64((2 ** 63) - 1) + 1
