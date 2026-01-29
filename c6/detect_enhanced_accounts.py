import sys
import pandas as pd

from tdda.constraints import detect
from enhance_accounts import enhance_accounts

def detect_enhanced(inpath, constraints_path, outpath):
    df = pd.read_parquet(inpath)
    enhance_accounts(df)
    validation = detect(df, constraints_path, outpath=outpath)
    print(validation)

if __name__ == '__main__':
    if len(sys.argv) == 4:
        detect_enhanced(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        cmd = 'discover_enhanced_accounts.py'
        print(f'USAGE: python {cmd} IN.parquet CONSTRAINTS.tdda OUT.parquet',
              file=sys.stderr)
        sys.exit(1)
