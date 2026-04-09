print('>>>', '''from tdda.referencetest.checkpolars import diff_dataframes''')
from tdda.referencetest.checkpolars import diff_dataframes
print('>>>', '''from tdda.serial import csv_to_polars''')
from tdda.serial import csv_to_polars
print('>>>', '''df2 = csv_to_polars('simple3x2-pdl.psv:')''')
df2 = csv_to_polars('simple3x2-pdl.psv:')
print('>>>', '''df = csv_to_polars('simple3x2.csv:')''')
df = csv_to_polars('simple3x2.csv:')
print('>>>', '''d = diff_dataframes(df, df2, type_matching='strict')''')
d = diff_dataframes(df, df2, type_matching='strict')
print('>>>', '''d''')
print(d)
print('>>>', '''''')

print('>>>', '''''')

