import os
import shutil
import tempfile

from codings1 import read, table, write

def compare(path):
    from_latin1 = read(path, 'iso-8859-1')
    from_latin9 = read(path, 'iso-8859-15')
    from_cp1252 = read(path, 'cp1252')
    from_utf8 = read(path, 'UTF-8')
    print(table(from_latin1, 0x80, 'iso-8859-1'))
    print(table(from_latin9, 0x80, 'iso-8859-15'))
    print(table(from_cp1252, 0x80, 'cp1252'))
    print(table(from_utf8, 0x80, 'UTF-8'))
    print()
    for i, (L1, L9, c) in enumerate(zip(from_latin1,
                                        from_latin9,
                                        from_cp1252), 0x80):
        if not (L1 == L9 == c):
            n1, n9, nc = ord(L1), ord(L9), ord(c)
            print(f'{i:02X}:  {L1}  {L9}  {c}  {n1:04X}  {n9:04X}  {nc:04X}')


if __name__ == '__main__':
    DIR = tempfile.mkdtemp()
    path = os.path.join(DIR, 'chars.txt')
    write(path, 0x80, 0x100)
    compare(path)
    shutil.rmtree(DIR)
