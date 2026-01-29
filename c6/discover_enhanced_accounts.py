import sys
import pandas as pd

from tdda.constraints import discover
from enhance_accounts import enhance_accounts

def discover_enhanced(inpath, outpath):
    df = pd.read_parquet(inpath)
    enhance_accounts(df)
    constraints = discover(df, verbose=False)
    with open(outpath, 'w') as f:
        f.write(constraints.to_json())
    print(f'Written {outpath}.')

if __name__ == '__main__':
    if len(sys.argv) == 3:
        discover_enhanced(sys.argv[1], sys.argv[2])
    else:
        cmd = 'discover_enhanced_accounts.py'
        print(f'USAGE: python {cmd} INFILE.parquet OUTFILE.tdda',
              file=sys.stderr)
        sys.exit(1)
