import polars as pl

df = pl.read_parquet('3numbers.parquet')

# Min Price Delta
deltaMin = df['PriceDelta'].min()
deltaMinStr = f'{round(deltaMin/1_000_000):0,}'
absDeltaMin = abs(deltaMin)
absDeltaMinStr = f'{round(absDeltaMin/1_000_000):0,}'

# Max Price Delta
deltaMax = df['PriceDelta'].max()
deltaMaxMillionsStr = f'{deltaMax/1_000_000:.1f}'

# Number of non-null Price Deltas
dfnn = df.filter(pl.col('PriceDelta').is_not_null())
nNonNullRows = dfnn.shape[0]

# Number of Price Deltas between £-20 and +£60
df2 = dfnn.filter((pl.col('PriceDelta') >= -20) & (pl.col('PriceDelta') <= 60))
nM20To60 = df2.shape[0]

# Fraction of non-nulls in that range:
pcM20To60 = 100 * nM20To60 / nNonNullRows
pcM20To60Str = f'{pcM20To60:.0f}\%'

# Number and proportion in range ±£90k

L = 90_000
dfpm90k = dfnn.filter(
    (pl.col('PriceDelta') >= -L) & (pl.col('PriceDelta') <= L)
)
nPM90k = dfpm90k.shape[0]
pcPM90k = 100 * nPM90k / nNonNullRows
pm90kpcStr = f'{pcPM90k:.2f}\\%'

# Number and proportion in range ±£800

L = 800
dfpm800 = dfnn.filter(
    (pl.col('PriceDelta') >= -L) & (pl.col('PriceDelta') <= L)
)
nPM800 = dfpm800.shape[0]
pcPM800 = 100 * nPM800 / nNonNullRows
pm800pcStr = f'{pcPM800:.2f}\\%'

# Check that under 0.0005% is a reasonable way cap to describe
# proportion the full range represented by ±£800

pcRangePM800 = 100 * (800 * 2) / (deltaMax - deltaMin)
cap800 = 0.0005
if cap800 / 2 < pcRangePM800 < cap800:
    pc800Bound = f'{cap800}\\%'
else:
    raise Exception(f'{cap800}% is not a good cap for the ±£800 range')


# Check that under 0.05% is a reasonable way cap to describe
# proportion the full range represented by ±£800

pcRangePM90k = 100 * (90_000 * 2) / (deltaMax - deltaMin)
cap90k = 0.05
if cap90k / 2 < pcRangePM90k < cap90k:
    pc90kBound = f'{cap90k}\\%'
else:
    raise Exception(f'{cap90k}% is not a good cap for the ±£800 range')



outpath = 'price-delta-defs-pl.tex'
with open(outpath, 'w') as f:
    f.write('\\def\\pdMinMillions{$%s$}\n' % deltaMinStr)
    f.write('\\def\\pdMinMillionPounds{$-\\pounds{}%s$}\n' % absDeltaMinStr)
    f.write('\\def\\pdMaxMillions{%s}\n' % deltaMaxMillionsStr)
    f.write('\\def\\pdpcNinetytoNinety{%s}\n' % pm90kpcStr)
    f.write('\\def\\pdpcInnerRange{%s}\n' % pcM20To60Str)
    f.write('\\def\\pdpcpmEightHundred{%s}\n' % pm800pcStr)
    f.write('\\def\\pdpcRangeEightHundredtoEightHundred{%s}\n' % pc800Bound)
    f.write('\\def\\pdpcRangeNinetytoNinety{%s}\n' % pc90kBound)
print(f'Written {outpath}.')
