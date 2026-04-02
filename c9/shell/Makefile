all:
	sh wc-alice.sh > wc-alice.txt 2>&1
	python ../../texify.py wc-alice.txt

	sh grep-impossible.sh > grep-impossible.txt 2>&1
	python ../../texify.py grep-impossible.txt

	sh greps-wc-l.sh > greps-wc-l.txt 2>&1
	python ../../texify.py greps-wc-l.txt greps-wc-l-tex.txt 80 R

	sh grep-o-alice.sh > grep-o-alice.txt 2>&1
	python ../../texify.py grep-o-alice.txt grep-o-alice-tex.txt 80 R

	sh grep-alice-alice.sh > grep-alice-alice.txt 2>&1
	python ../../texify.py grep-alice-alice.txt

	sh count-occurrences-alice.sh > count-occurrences-alice.txt 2>&1
	python ../../texify.py count-occurrences-alice.txt

