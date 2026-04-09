from tdda.serial import pandas_to_csv, csv_to_pandas

df = csv_to_pandas('simple3x2.csv:')
pandas_to_csv(df,'simple3x2-pdl.psv', auto_md_outpath=True,
              md_outpath='simple3x2-pdl2.serial', md_inpath='pdl.serial')

info = pandas_to_csv(df, 'simple3x2-inmd.psv',
    md_outpath='simple3x2-pdl+pandas.serial', md_inpath='pdl.serial',
    flavour=['pandas.read_csv', 'tdda.serial', 'pandas.DataFrame.to_csv'])

df2 = csv_to_pandas('simple3x2-inmd.psv:simple3x2-pdl+pandas.serial')

print(df2.info())

