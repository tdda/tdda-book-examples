from tdda.serial import csv_to_polars
df = csv_to_polars('elements3-old.csv', 'elements3-old.serial')
print(df)
