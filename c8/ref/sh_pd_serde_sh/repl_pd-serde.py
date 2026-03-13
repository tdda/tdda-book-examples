print('>>>', '''import pandas as pd''')
import pandas as pd
print('>>>', '''from tdda.serial import csv_to_pandas, pandas_to_csv''')
from tdda.serial import csv_to_pandas, pandas_to_csv
print('>>>', '''df = pd.DataFrame({'n': [1, 2],'f': [1.5, None],'s': ['à', 'é']})''')
df = pd.DataFrame({'n': [1, 2],'f': [1.5, None],'s': ['à', 'é']})
print('>>>', '''df''')
print(df)
print('>>>', '''pandas_to_csv(df,'simple3x2.csv', md_outpath='simple3x2.serial')''')
print(pandas_to_csv(df,'simple3x2.csv', md_outpath='simple3x2.serial'))
