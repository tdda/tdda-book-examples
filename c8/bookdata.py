from datetime import date
from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    publication_date: date|None = None
    own: bool = False

if __name__ == '__main__':
    print(Book('1984', 'George Orwell', date(1984, 6, 8), True))
    print(Book(1984, 'George Orwell'))
