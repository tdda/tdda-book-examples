all:
	tdda examples referencetest
	mv referencetest_examples/dataframes.py .
        rm -rf referencetest_examples
	awk -f cut-generate_dataframe.awk dataframes-extract.py
        rm dataframes.py
