import unicodedata
from eacute import names, uc


def uc(s, joint=' '):
    return joint.join(f'U+{ord(c):04X}' for c in s)


def names(s, multiline=False):
    joint = '\n   ' if multiline else '; '
    return joint.join(unicodedata.name(c) for c in s)


def names_codes(s):
    return '\n   '.join(f' {uc(c)} {names(c)}' for c in s)


def print_detail(s, multiline=False):
    print(f'{s}: {names_codes(s)}\n')


qAB = '\u0071\u0307\u0323'  # q with dot Above and Below
qBA = '\u0071\u0323\u0307'  # q with dot Below and Above
print_detail(qAB)
print_detail(qBA)


qAB2 = 'q̣̇'  # q with dot Above and Below
qBA2 = 'q̣̇'  # q with dot Below and Above
print_detail(qAB2)
print_detail(qBA2)
