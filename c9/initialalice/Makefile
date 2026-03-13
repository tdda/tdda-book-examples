test:
	./count-occurrences.sh Alice alice.txt > actual-alice-alice.txt
	diff actual-alice-alice.txt expected-alice-alice.txt
	echo "PASS: count correct for Alice"
	./count-occurrences.sh impossible alice.txt \
                > actual-impossible-alice.txt
	diff actual-impossible-alice.txt expected-impossible-alice.txt
	echo "PASS: count correct for impossible"

clean:
	rm actual-*.txt
