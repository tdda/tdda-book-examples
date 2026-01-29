from unicodedata import lookup

print(lookup('HEAVY BLACK HEART'),
      lookup('HEAVY BLACK HEART') + lookup('VARIATION SELECTOR-16'),
      lookup('HEAVY BLACK HEART') + lookup('VARIATION SELECTOR-15'),
      lookup('BLACK HEART'))
