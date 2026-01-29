from pydantic_bookdata import Book, date

json1 = Book(title='Fugitive Pieces', author='Anne Michaels',
             publication_date=date(1996, 5, 11), own=True).model_dump_json()
print(repr(Book.model_validate_json(json1)))
json2 = '{"title": 2666, "author": "Roberto Bolaño", "owns": true}'
print(repr(Book.model_validate_json(json2)))
