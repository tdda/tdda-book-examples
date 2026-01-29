import sys
import unicodedata

def printable(c):
    if c in \textquotesingle{}\u{}0307\textquotesingle{}:
        return unicodedata.lookup(\textquotesingle{}DOT ABOVE\textquotesingle{})
    elif c == \textquotesingle{}\u{}0323\textquotesingle{}:
        return unicodedata.lookup(\textquotesingle{}ONE DOT LEADER\textquotesingle{})
    elif c == \textquotesingle{} \textquotesingle{}:
        return unicodedata.lookup(\textquotesingle{}OPEN BOX\textquotesingle{})
    return c

i = 1
while c := sys.stdin.read(1):  # Python 3.8+
    print(f"\{ord(c):04x\} \{printable(c):3\}", end=\textquotesingle{}\textquotesingle{} if i % 10 else \textquotesingle{}\eol\textquotesingle{})
    i += 1
