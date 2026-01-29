import pandas as pd
from tdda.serial.io import pandas_read_df, pandas_write_df

def group_areas(inpath, outpath):
    df = pandas_read_df(inpath)
    dfg = (
        df.groupby('Kind', observed=True)
          .agg({
              'Name': 'count',
              'Population': ['min', 'max', 'sum'],
              'Seats': ['count', 'sum'],
           })
          .reset_index()
    )
    dfg.columns = [f'{c[1]}{c[0]}' for c in dfg.columns]
    pandas_write_df(dfg, outpath)

if __name__ == '__main__':
    group_areas('us-states.parquet', 'us-area-stats.csv')
