import unicodedata

def uc(s, joint=' '):
    return joint.join(f'U+{ord(c):04X}' for c in s)

def names(s, multiline=False):
    joint = '\n   ' if multiline else '; '
    return joint.join(unicodedata.name(c) for c in s)

def print_detail(s, multiline=False):
    print(f'{s}: {uc(s):13} {names(s, multiline)} ')

if __name__ == '__main__':
    é = 'é'
    print_detail(é)

    nfd = unicodedata.normalize('NFD', é)
    print_detail(nfd)

    nfc = unicodedata.normalize('NFC', nfd)

    if (unicodedata.normalize('NFC', nfc) == nfc == é
            and unicodedata.normalize('NFD', nfd) == nfd):
        print('Normalization is idempotent')
    print(f'nfc is {"equal" if nfc == nfd else "NOT EQUAL"} to nfd')
    print(f'"{nfd}" == "é": ', nfd == "é")
