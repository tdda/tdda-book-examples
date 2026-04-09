from tdda.serial import pandas_to_csv, csv_to_pandas
from tdda.referencetest.checkpandas import diff_dataframes

df2 = csv_to_pandas('simple3x2.csv', find_md=True)
print(pandas_to_csv(df2,'simple3x2-pdl.psv', auto_md_outpath=True, sep='|', na_rep=';', encoding='latin-1'))

df3 = csv_to_pandas('simple3x2-pdl.psv:')

d = diff_dataframes(df2, df3, type_matching='strict')
print(d)
