import unicodedata

def uc(s, joint=\textquotesingle{} \textquotesingle{}):
    return joint.join(f\textquotesingle{}U+\{ord(c):04X\}\textquotesingle{} for c in s)

def names(s, multiline=False):
    joint = \textquotesingle{}\eol   \textquotesingle{} if multiline else \textquotesingle{}; \textquotesingle{}
    return joint.join(unicodedata.name(c) for c in s)

def print_detail(s, multiline=False):
    print(f\textquotesingle{}\{s\}: \{uc(s):13\} \{names(s, multiline)\} \textquotesingle{})

if __name__ == \textquotesingle{}__main__\textquotesingle{}:
    \'e = \textquotesingle{}\'e\textquotesingle{}
    print_detail(\'e)

    nfd = unicodedata.normalize(\textquotesingle{}NFD\textquotesingle{}, \'e)
    print_detail(nfd)

    nfc = unicodedata.normalize(\textquotesingle{}NFC\textquotesingle{}, nfd)

    if (unicodedata.normalize(\textquotesingle{}NFC\textquotesingle{}, nfc) == nfc == \'e
            and unicodedata.normalize(\textquotesingle{}NFD\textquotesingle{}, nfd) == nfd):
        print(\textquotesingle{}Normalization is idempotent\textquotesingle{})
    print(f\textquotesingle{}nfc is \{"equal" if nfc == nfd else "NOT EQUAL"\} to nfd\textquotesingle{})
    print(f\textquotesingle{}"\{nfd\}" == "\'e": \textquotesingle{}, nfd == "\'e")
