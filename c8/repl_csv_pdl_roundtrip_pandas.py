print('>>>', '''from tdda.serial import pandas_to_csv, csv_to_pandas''')
from tdda.serial import pandas_to_csv, csv_to_pandas
print('>>>', '''from tdda.referencetest.checkpandas import diff_dataframes''')
from tdda.referencetest.checkpandas import diff_dataframes
print('>>>', '''''')

print('>>>', '''df2 = csv_to_pandas('simple3x2.csv', find_md=True)''')
df2 = csv_to_pandas('simple3x2.csv', find_md=True)
print('>>>', '''pandas_to_csv(df2,'simple3x2-pdl.psv', auto_md_outpath=True, sep='|', na_rep=';', encoding='latin-1')''')
print(pandas_to_csv(df2,'simple3x2-pdl.psv', auto_md_outpath=True, sep='|', na_rep=';', encoding='latin-1'))
print('>>>', '''''')

print('>>>', '''df3 = csv_to_pandas('simple3x2-pdl.psv:')''')
df3 = csv_to_pandas('simple3x2-pdl.psv:')
print('>>>', '''''')

print('>>>', '''d = diff_dataframes(df2, df3, type_matching='strict')''')
d = diff_dataframes(df2, df3, type_matching='strict')
print('>>>', '''d''')
print(d)
