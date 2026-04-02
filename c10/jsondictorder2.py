import json
a = json.dumps({'one': 1, 'two': 2})
print(a)
b = json.dumps({'two': 2, 'one': 1})
print(b)
print(f'{repr(a)} == {repr(b)}: {a == b}')
A = json.loads(a)
B = json.loads(b)
print(f'{A} == {B}: {A == B}')
