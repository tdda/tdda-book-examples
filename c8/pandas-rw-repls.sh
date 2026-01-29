#!/bin/sh

# Check it works!
python pandas_rw.py

# Cut out the lines for the book

awk -f read.awk pandas_rw.py > pdr_syntax.py
awk -f write.awk pandas_rw.py > pdw_syntax.py
awk -f json-read.awk pandas_rw.py > json_pdr_syntax.py





