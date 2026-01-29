from unicodedata import normalize as norm
from eacute import names, uc

def names_codes(s):
    return '\n   '.join(f' {uc(c)} {names(c)}' for c in s)

def print_detail(s, multiline=False):
    print(f'{s}: {names_codes(s)}\nLength: {len(c)}\n')

smiley = chr(0x1F600)
okA = '\U0001F44C'
okB = '\U0001F44C\U0001F3FB'
okC = '\U0001F44C\U0001F3FC'
okD = '\U0001F44C\N{EMOJI MODIFIER FITZPATRICK TYPE-4}'
okE = '\U0001F44C\U0001F3FE'
okF = '\U0001F44C\U0001F3FF'

mmh = '👨' + chr(0x1F3FB) + chr(0x200D) + '🤝' + chr(0x200D) + '👨' + chr(0x1F3FF)

mmh2 = '\U0001F468\U0001F91D\U0001F468'
mmh3 = '\U0001F468\U0001F3FB\U0001F91D\U0001F468\U0001F3FF'
mmh4 = '\U0001F468\U0001F3FB\u200D\U0001F91D\u200D\U0001F468\U0001F3FF'

thumbsup = '\U0001F44D\uFE0F'
bwthumbsup = '\U0001F44D\uFE0E'

for c in (smiley, okA, okB, okC, okD, okE, okF, mmh4, thumbsup, bwthumbsup):
    print_detail(c)

for c in (okB, thumbsup, bwthumbsup):
    assert (norm('NFC', c) == norm('NFD', c)
            == norm('NFKC', c) == norm('NFKD', c))

