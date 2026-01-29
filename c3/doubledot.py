from unicodedata import normalize
from eacute import names, uc

def names_codes(s):
    return '\n   '.join(f' {uc(c)} {names(c)}' for c in s)

def print_detail(s, multiline=False):
    print(f'{s}: {names_codes(s)}\n')

qAB = 'q̣̇'  # q + dot Above + dot Below
print_detail(qAB)

qBA = 'q̣̇'  # q + dot Below + dot Above
print_detail(qBA)

print('qAB == qBA:', qAB == qBA, end='\n\n')

qBAC, qBAD = normalize('NFC', qBA), normalize('NFD', qBA)
qABC, qABD = normalize('NFC', qAB), normalize('NFD', qAB)
print_detail(qBAC)

print('qBAC == qBAD == qABC == qABD == qBA:',
      qBAC == qBAD == qABC == qABD == qBA, end='\n\n')

qAB8 = qAB.encode('UTF-8')
print(' '.join(hex(c) for c in qAB8))
assert qAB8.decode('UTF-8') == qAB

qBA8 = qBA.encode('UTF-8')
print(' '.join(hex(c) for c in qBA8))
assert qBA8.decode('UTF-8') == qBA
