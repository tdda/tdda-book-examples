a = 1 << 60
b = a + 1
print(f'({a:,}; {b:,})')
print(a == b)

import pandas as pd
df = pd.DataFrame({'x': [a, b], 'y': [b, a]})  # n.b. reversed!
print(df.x == df.y)  # Compare int64 columns x and y

df = pd.DataFrame({'x': [a, b, None], 'y': [b, a, None]})
print(df)

print(df.x == df.y)  # Compare float64 columns x and y
