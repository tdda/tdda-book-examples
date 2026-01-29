.PHONY:
all: clean \
     books.txt \
     pandera_books_schema.py \
     pandera_books_results.json \
     books.tdda \
     bad-books.csv
	echo Done


.PHONY:
clean:
	rm -f books.txt \
              pandera_books_schema.py \
              pandera_books_results.json \
              books.tdda \
              bad-books.csv

books.txt: test_show_books.py books.parquet
	python test_show_books.py

pandera_books_schema.py: pandera_books_infer.py books.parquet
	python test_pandera_infer.py

pandera_books_results.json: pandera_books_schema.py
	python test_pandera_validate.py

books.tdda: disco-books.sh
	python test_disco_books.py

bad-books.csv: books.tdda detect-2.sh
	python test_detect_books2.py
