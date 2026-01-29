import unicodedata
from eacute import uc

def display(c, canonical):
    nfkc = unicodedata.normalize(\textquotesingle{}NFKC\textquotesingle{}, c)
    nfkd = unicodedata.normalize(\textquotesingle{}NFKD\textquotesingle{}, c)
    is_canonical = \textquotesingle{}\cmark\textquotesingle{} if nfkc == canonical else \textquotesingle{}\xmark\textquotesingle{}
    try:
        name = unicodedata.name(c)
    except ValueError:
        name = \textquotesingle{}TAB\textquotesingle{} if c == \textquotesingle{}\textbackslash{t}\textquotesingle{} else \textquotesingle{}Unknown Name\textquotesingle{}
    print(f\textquotesingle{}\{is_canonical\} \{name:27\} \{c:\}:  \textquotesingle{}
          f\textquotesingle{}\{uc(c)\}  NFKC: \{nfkc\} \{uc(nfkc)\}  NFKD: \{nfkd\} \{uc(nfkd)\}\textquotesingle{})

def display_all(name, s, canonical):
    print(f\textquotesingle{}\{name:8\} \{s\}\textquotesingle{})
    for c in s:
        display(c, canonical)
    print()

display_all(\textquotesingle{}Dashes\textquotesingle{}, \textquotesingle{}-\u{}2013\u{}2014\u{}2212\textquotesingle{}, \textquotesingle{}-\textquotesingle{})
display_all(\textquotesingle{}Single Quotes\textquotesingle{}, "\textquotesingle{}\u{}2018\u{}2019\u{}02BC`", "\textquotesingle{}")
display_all(\textquotesingle{}Double Quotes\textquotesingle{},\textquotesingle{}"\u{}FF02\u{}201C\u{}201D\textquotesingle{}, \textquotesingle{}"\textquotesingle{})
display_all(\textquotesingle{}Spaces\textquotesingle{}, \textquotesingle{} \u{}00A0\u{}2002\u{}2003\u{}2007\u{}2008\u{}0009\textquotesingle{}, \textquotesingle{} \textquotesingle{})
display_all(\textquotesingle{}Ones\textquotesingle{}, f\textquotesingle{}1\u{}00B9\u{}2081\u{}2460\U{}0001D7D9\u{}2474\u{}2488\textquotesingle{}, \textquotesingle{}1\textquotesingle{})
display_all(\textquotesingle{}Letter e\textquotesingle{}, \textquotesingle{}e\'eè\textquotesingle{}, \textquotesingle{}e\textquotesingle{})
display_all(\textquotesingle{}Letter A\textquotesingle{}, \textquotesingle{}A\u{}0391\textquotesingle{}, \textquotesingle{}A\textquotesingle{})
display_all(\textquotesingle{}Omega\textquotesingle{}, \textquotesingle{}\u{}03A9\u{}2126\textquotesingle{}, \textquotesingle{}Ω\textquotesingle{})
display_all(\textquotesingle{}A Ring Accent\textquotesingle{}, \textquotesingle{}\u{}00C5\u{}212B\textquotesingle{}, \textquotesingle{}Å\textquotesingle{})
display_all(\textquotesingle{}Ligature\textquotesingle{}, \textquotesingle{}\u{}FB01\textquotesingle{}, \textquotesingle{}fi\textquotesingle{})
display_all(\textquotesingle{}Ellipsis\textquotesingle{}, \textquotesingle{}\u{}2026\u{}22EF\u{}FE19\u{}22F1\textquotesingle{}, \textquotesingle{}...\textquotesingle{})
