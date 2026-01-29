import sys
import pandas as pd

def count_records(inpath, outpath):
    """
    Write CSV file outpath with single field, n_records, containing
    the number of records in the parquet file inpath.
    """
    df = pd.read_parquet(inpath)
    odf = pd.DataFrame({'n_records': [df.shape[0]]})
    odf.to_csv(outpath, index=False)

if __name__ == '__main__':
    if len(sys.argv) == 3:
        count_records(sys.argv[1], sys.argv[2])
    else:
        print('Usage: python countpqrecords.py IN.parquet OUT.csv')
        sys.exit(1)
