import json
import pandas as pd

path = 'accounts1k.csv'
# read
df = pd.read_csv(path, sep=',', na_values='', header=0,
                 keep_default_na=False, encoding='utf-8',
                 date_format={'open_date': 'ISO8601',
                              'close_date': 'ISO8601'},
                 parse_dates=['open_date', 'close_date'],
                 quotechar='"', escapechar=None)
# end-read
print(df.info())

path = 'accounts1k-out.csv'
# write
df.to_csv(path, sep=',', na_rep='',
          quotechar='"', escapechar=None, encoding='utf-8',
          header=True, index=False)
# end-write

df2 = pd.read_csv(path, sep=',', na_values='', header=0,
                 keep_default_na=False, encoding='utf-8',
                 date_format={'open_date': 'ISO8601',
                              'close_date': 'ISO8601'},
                 parse_dates=['open_date', 'close_date'],
                 quotechar='"', escapechar=None)

print('Round-tripped OK' if df2.equals(df) else 'Round-trip failed')


path = 'accounts1k.csv'

df_orig = df

# json-read
with open('format.json') as f:
    params = json.load(f)
df = pd.read_csv(path, **params)
# end-json-read


print('JSON worked OK' if df.equals(df_orig) else 'JSON failed')
