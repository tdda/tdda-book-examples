# requires Python3.8 or above for := (walrus operator)
import numpy as np
import pandas as pd
from itertools import chain

powers = (7, 8, 15, 16, 31, 32, 63)
ints = list(chain(*[(n := int(pow(2, k)) - 1, -n - 1) for k in powers]))
d = {
   f'i{k}': np.array(ints, dtype=f'int{k}')
   for k in (8, 16, 32, 64)
} | {
   f'u{k}': np.array(ints, dtype=f'uint{k}')
   for k in (8, 16, 32, 64)
}
df = pd.DataFrame(d)
print(df.to_string(index=None), end='\n\n')
df['overflow64'] = df['i64'] + np.where(df['i64'] < 0, -1, 1)
df['no_overflow'] = [f'{v + (-1 if v < 0 else 1):,}' for v in ints]
print(df[['i64', 'overflow64', 'no_overflow']].to_string(index=None))

