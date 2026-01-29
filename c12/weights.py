n_weights = int(1.76e12)
print(f'1.76 trillion = {n_weights:,}')
n_bytes = 2**50
print(f'2^{5} = {n_bytes:,}')

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
