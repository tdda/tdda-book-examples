from datetime import date
from pydantic import BaseModel

class Book(BaseModel):
    title: str
    author: str
    publication_date: date|None = None
    own: bool = False

if __name__ == '__main__':
    print(repr(Book(title='1984', author='George Orwell',
                    publication_date=date(1984, 6, 8), own=True)))
    print(repr(Book(title=1984, author='George Orwell')))

