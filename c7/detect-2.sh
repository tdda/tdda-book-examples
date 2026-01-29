#!/bin/sh
tdda detect books2.parquet books.tdda bad-books.csv --key Title -r txt
python ../texify.py bad-books.txt
