import os
import polars as pl

inpath = '~tdda/BasicCompanyDataAsOneFile-2024-03-01.csv'
outpath = 'ch-defs-pl.tex'

df = pl.read_csv(os.path.expanduser(inpath))
nc = df.shape[0]
n10plus = df.filter(pl.col(' PreviousName_10.CompanyName') != '').shape[0]
pc10plus = 100.0 * n10plus / nc

with open(outpath, 'w') as f:
    f.write('\\def\\chTotalCompanies{%s}\n' % f'{nc:,}')
    f.write('\\def\\chCompaniesTenPlusNames{%s}\n' % f'{n10plus:,}')
    f.write('\\def\\chPropTenPlusNames{%s}\n' % f'{pc10plus:.5f}\\%')
print(f'Written {outpath}.')
