import sys
import unicodedata

def printable(c):
    if c in '\u0307':
        return unicodedata.lookup('DOT ABOVE')
    elif c == '\u0323':
        return unicodedata.lookup('ONE DOT LEADER')
    elif c == ' ':
        return unicodedata.lookup('OPEN BOX')
    return c

i = 1
while c := sys.stdin.read(1):  # Python 3.8+
    print(f"{ord(c):04x} {printable(c):3}", end='' if i % 10 else '\n')
    i += 1

