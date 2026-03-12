print('>>>', '''import time''')
import time
print('>>>', '''M, m = (1 << 31) - 1, -(1 << 31)''')
M, m = (1 << 31) - 1, -(1 << 31)
print('>>>', '''time.gmtime(M)''')
print(time.gmtime(M))
print(">>>", """f'{M:,}, {M:X}'""")
print(f'{M:,}, {M:X}')
print('>>>', '''time.gmtime(M)''')
print(time.gmtime(M))
print(">>>", """f'{m:,}, {m:X}'""")
print(f'{m:,}, {m:X}')
print('>>>', '''''')

