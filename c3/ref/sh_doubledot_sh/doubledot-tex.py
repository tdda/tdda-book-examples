from unicodedata import normalize
from eacute import names, uc

def names_codes(s):
    return \textquotesingle{}\eol   \textquotesingle{}.join(f\textquotesingle{} \{uc(c)\} \{names(c)\}\textquotesingle{} for c in s)

def print_detail(s, multiline=False):
    print(f\textquotesingle{}\{s\}: \{names_codes(s)\}\eol\textquotesingle{})

qAB = \textquotesingle{}\qBA\textquotesingle{}  # q + dot Above + dot Below
print_detail(qAB)

qBA = \textquotesingle{}\qBA\textquotesingle{}  # q + dot Below + dot Above
print_detail(qBA)

print(\textquotesingle{}qAB == qBA:\textquotesingle{}, qAB == qBA, end=\textquotesingle{}\eol\eol\textquotesingle{})

qBAC, qBAD = normalize(\textquotesingle{}NFC\textquotesingle{}, qBA), normalize(\textquotesingle{}NFD\textquotesingle{}, qBA)
qABC, qABD = normalize(\textquotesingle{}NFC\textquotesingle{}, qAB), normalize(\textquotesingle{}NFD\textquotesingle{}, qAB)
print_detail(qBAC)

print(\textquotesingle{}qBAC == qBAD == qABC == qABD == qBA:\textquotesingle{},
      qBAC == qBAD == qABC == qABD == qBA, end=\textquotesingle{}\eol\eol\textquotesingle{})

qAB8 = qAB.encode(\textquotesingle{}UTF-8\textquotesingle{})
print(\textquotesingle{} \textquotesingle{}.join(hex(c) for c in qAB8))
assert qAB8.decode(\textquotesingle{}UTF-8\textquotesingle{}) == qAB

qBA8 = qBA.encode(\textquotesingle{}UTF-8\textquotesingle{})
print(\textquotesingle{} \textquotesingle{}.join(hex(c) for c in qBA8))
assert qBA8.decode(\textquotesingle{}UTF-8\textquotesingle{}) == qBA
