import os
import tempfile
import shutil

def write(path, start=0x20, stop=0x7f):
    s = bytes(range(start, stop))
    with open(path, 'wb') as f:
        f.write(s)

def read(path, encoding):
    with open(path, 'rb') as f:
        s = f.read()
    return s.decode(encoding, 'replace')

def table(s, n, encoding):
    return (f'\n{encoding}\n    0123456789ABCDEF\n'
            + '\n'.join(f'{n + i:02x}: {s[i:i+0x10]}'
                        for i in range(0, len(s), 0x10)))

def compare(path):
    from_ascii = read(path, 'ascii')
    from_latin1 = read(path, 'iso-8859-1')
    from_latin9 = read(path, 'iso-8859-15')
    from_cp1252 = read(path, 'cp1252')
    from_utf8 = read(path, 'UTF-8')
    print(table(from_ascii, 0x20, 'ascii'))
    print(table(from_latin1, 0x20, 'iso-8859-1'))
    # print(table(from_latin9, 0x20, 'iso-8859-15'))
    # print(table(from_cp1252, 0x20, 'cp1252'))
    # print(table(from_utf8, 0x20, 'UTF-8'))
    if from_ascii == from_latin1 == from_latin9 == from_cp1252 == from_utf8:
        print('\nThey are all the same from 20 to 7E!')
    else:
        print('\nThey are NOT all the same from 20 to 7E!')

if __name__ == '__main__':
    DIR = tempfile.mkdtemp()
    path = os.path.join(DIR, 'chars.txt')
    write(path)
    compare(path)
    shutil.rmtree(DIR)
