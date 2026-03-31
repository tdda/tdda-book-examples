print('>>>', '''from tdda.serial import csv_to_polars''')
from tdda.serial import csv_to_polars
print('>>>', '''df = csv_to_polars('elements3-old.csv', 'elements3-old.serial')''')
df = csv_to_polars('elements3-old.csv', 'elements3-old.serial')
print('>>>', '''df''')
print(df)
