import unicodedata
a = '\U0001f469\U0001f3fd\u200d\u2764\ufe0f\u200d\U0001f48b\u200d\U0001f468\U0001f3ff'
print(a)
nfkd = unicodedata.normalize('NFKD', a)
print(a == nfkd)
nfkc = unicodedata.normalize('NFKC', a)
print(a == nfkc)




