#!/bin/sh

# Generate the script
python pandera_books_infer.py

# Fix the import
sed 's/from pandera/from pandera.pandas/g' < pandera_books_schema.py > pandera_books_schema_fixed.py
mv pandera_books_schema_fixed.py pandera_books_schema.py

# copy the tight version in the books
rm -f pandera_books_infer_expanded.py
cp pandera_books_schema_tight.py pandera_books_schema_expanded.py

# reformat the right version with black
black pandera_books_schema_expanded.py

# should be the same as the modified generated version
diff pandera_books_schema_expanded.py pandera_books_schema.py


