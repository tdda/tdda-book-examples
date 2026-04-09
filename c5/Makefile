all: time_struct-output-folded.txt \
     disco \
     verify

time_struct-output-folded.txt: time_struct-output.txt
	fold -s time_struct-output.txt > time_struct-output-folded.txt


.PHONY:
disco:
	python test_discover_bookex12.py

.PHONY:
verify:
	python test_verify_book_ex13.py
	python ../texify.py ref/verify_book_ex13/STDOUT accounts-verification1.txt.tex 1000

.PHONY:
detect:
	python test_detect_book_ex17.py


