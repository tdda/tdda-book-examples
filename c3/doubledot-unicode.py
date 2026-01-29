from eacute import uc

qAB = 'q̣̇'  # q + dot Above + dot Below
uAB = uc(qAB).replace(' ', '').replace('U+', r'\u')
print(f"    qAB = '{uAB}'")

qBA = 'q̣̇'  # q + dot Below + dot Above
uBA = uc(qBA).replace(' ', '').replace('U+', r'\u')
print(f"    qBA = '{uBA}'")
