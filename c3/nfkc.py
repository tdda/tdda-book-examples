import unicodedata
from eacute import uc

def display(c, canonical):
    nfkc = unicodedata.normalize('NFKC', c)
    nfkd = unicodedata.normalize('NFKD', c)
    is_canonical = '✔' if nfkc == canonical else '✘'
    try:
        name = unicodedata.name(c)
    except ValueError:
        name = 'TAB' if c == '\t' else 'Unknown Name'
    print(f'{is_canonical} {name:27} {c:}:  '
          f'{uc(c)}  NFKC: {nfkc} {uc(nfkc)}  NFKD: {nfkd} {uc(nfkd)}')

def display_all(name, s, canonical):
    print(f'{name:8} {s}')
    for c in s:
        display(c, canonical)
    print()

display_all('Dashes', '-\u2013\u2014\u2212', '-')
display_all('Single Quotes', "'\u2018\u2019\u02BC`", "'")
display_all('Double Quotes','"\uFF02\u201C\u201D', '"')
display_all('Spaces', ' \u00A0\u2002\u2003\u2007\u2008\u0009', ' ')
display_all('Ones', f'1\u00B9\u2081\u2460\U0001D7D9\u2474\u2488', '1')
display_all('Letter e', 'eéè', 'e')
display_all('Letter A', 'A\u0391', 'A')
display_all('Omega', '\u03A9\u2126', 'Ω')
display_all('A Ring Accent', '\u00C5\u212B', 'Å')
display_all('Ligature', '\uFB01', 'fi')
display_all('Ellipsis', '\u2026\u22EF\uFE19\u22F1', '...')
