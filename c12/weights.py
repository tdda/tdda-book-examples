import json

from tdda.utils import dict_to_tex_macros

n_weights = int(1.76e12)
print(f'1.76 trillion = {n_weights:,}')

n_bytes = 2**50
k = int(pow(2, 10))
assert k == 1024
M = k * k
G = k * M
T = k * G
P = k * T
assert n_bytes == P


print(f'2^{50} = {n_bytes:,}')
lower_bound = pow(10, 15)
print(f'2^50 ({n_bytes:,}) > 10^15 {lower_bound:,}.')
assert n_bytes > lower_bound

book_words = 90_000
word_len = 6

n_books = int(n_bytes / book_words / word_len)

n_books_round = n_books - n_books % 1_000_000_000
print(
    f'{n_bytes:,} bytes '
    f'/ {book_words:,} '
    f'words per book '
    f'/ {word_len} chars per word\n'
    f'= {n_books:,.0f}.'
)

print(f'Rounds down to: {n_books_round:,}')

years = 50
days_per_year = 365
days = years * days_per_year
ratio = round(n_books / days)
ratio_floor = ratio - ratio % 100_000


print(f'Books read at 1/day for 50 years: {days:,}')

print(f'Ratio: {n_books:,} / {days:,} = {ratio:,}')
print(f'Ratio floor: {ratio_floor:,}')


d = {
    'trillion-1-point-76': f'{n_weights:,}',
    'two-to-power-fifty': f'{n_bytes:,}',
    'petabyte': f'{P:,}',
    'ratio': f'{ratio:,}',
    'ratio-floor': f'{ratio_floor:,}',
    'n-books-round': f'{n_books_round:,}',
}

with open('weights.json', 'w') as f:
    json.dump(d, f)
dict_to_tex_macros(d, 'weights-defs.tex', verbose=True)
