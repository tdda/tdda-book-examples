import pandas as pd

def read_data(inpath):
    return pd.read_csv(
        inpath,
        sep=',',
        encoding='utf-8',
        quotechar='"',
        dtype=None,
        na_values='',
        keep_default_na=False
    )

