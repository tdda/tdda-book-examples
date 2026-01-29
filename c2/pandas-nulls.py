# pandas-nulls.py
#
# USAGE: python pandas-nulls.py [t]    (t for tex output)
import sys
import numpy as np
import pandas as pd

from rich.table import Table
from rich import print as rprint

nulls = {
     'None': None,
     'np.nan': np.nan,
     'pd.NaT': pd.NaT,
     'numpy NaT': np.datetime64('NaT'),
     'IEEE nan': float('nan'),
     'pd.NA': pd.NA,
}

null_values = [
     None,
     np.nan,
     pd.NaT,
     np.datetime64('NaT'),
     float('nan'),
     pd.NA,
]


def show_table(comparison, tex=False):
    if tex:
        return show_tex_table(comparison)
    assert comparison in ('==', 'is')
    t = Table()
    t.add_column(comparison, justify='left', style='bold')
    f = lambda x: (
        '✔︎' if str(x) == 'True' else '✗' if str(x) == 'False' else str(x)
    )
    for v in nulls:
        t.add_column(v, justify='center')
    for k, L in nulls.items():
        if comparison == '==':
            t.add_row(*([k] + [f(L == R) for R in null_values]))
        else:
            t.add_row(*([k] + [f(L is R) for R in null_values]))
    rprint(t)


def show_table(comparison, tex=False):
    if tex:
        return show_tex_table(comparison)
    assert comparison in ('==', 'is')
    table = [
        r'\begin{tabular}{lcccccc}',
        r'\aboveline',
        f'{comparison:10} & ' + ' & '.join(nulls),
        r'\midline'
    ]
    f = lambda x: (
        r'\cmark' if str(x) == 'True'
        else r'\xmark' if str(x) == 'False'
        else r'\NA   ' if str(x) == '<NA>'
        else None  # should generate error
    )
    rows = []
    for k, L in nulls.items():
        if comparison == '==':
            rows.append(' & '.join(
                [f'{k:10}']
                + [f(L == R) for R in null_values]
            ))
        else:
            rows.append(' & '.join(
                [f'{k:10}']
                + [f(L is R) for R in null_values]
            ))
    table.append(' \\\\\n'.join(rows))
    table.extend([r'\belowline', r'\end{tabular}', ''])
    kind = 'eq' if comparison == '==' else 'is'
    filename = f'pandas-comparison-{kind}.tex'
    with open(filename, 'w') as f:
        f.write('\n'.join(table))


def gen_df():
    return pd.DataFrame({
       'i': [1, None],
       'f': [1.0, None],
       'o': ['a', None],
       'I': pd.Series([1, None], dtype='Int64'),
       'S': pd.Series(['a', None], dtype='string'),
    })


def df_eq(tex=False):
    df1 = gen_df()
    df2 = gen_df()

    if tex:
        with open('pd-nulls-df1.txt', 'w') as f:
            f.write(f'{df1}\n')
        with open('pd-nulls-df1==df1.txt', 'w') as f:
            f.write(f'{df1 == df1}\n')
        with open('pd-nulls-df1==df2.txt', 'w') as f:
            f.write(f'{df1 == df2}\n')
        with open('pd-nulls-df1-comparisons.txt', 'w') as f:
            f.write(f'df1.equals(df1): {df1.equals(df1)}\n')
            f.write(f'df1.equals(df2): {df1.equals(df2)}\n')
            f.write('all(df1[c].equals(df2[c]) for c in df1): '
                    + str(all(df1[c].equals(df2[c]) for c in df1))
                    + '\n')
    else:
        print(f'\ndf1 (and df2):\n{df1}\n')
        print(f'df1 == df1:\n{df1 == df1}\n')
        print(f'df1 == df2:\n{df1 == df2}\n')
        print('df1.equals(df1):', df1.equals(df1))
        print('df1.equals(df2):', df1.equals(df2))
        print('all(df1[c].equals(df2[c]) for c in df1):',
              all(df1[c].equals(df2[c]) for c in df1))


if __name__ == '__main__':
    tex = len(sys.argv) > 1 and sys.argv[1] == 't'
    show_table('==')
    show_table('is')
    df_eq(tex)
