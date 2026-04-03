#!/bin/sh
tdda examples referencetest
awk -f cut-generate_dataframe.awk referencetest_examples/dataframes.py > dataframes-extract.py
rm -rf referencetest_examples
