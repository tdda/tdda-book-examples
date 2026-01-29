#!/bin/sh
tdda detect accounts25k.parquet accountsv2.tdda a25k-bads-v2c.csv \
     --report txt --key account_number
head -2 a25k-bads-v2c.csv > a25k-bads-v2c-head-2-raw.csv
python wrap.py a25k-bads-v2c-head-2-raw.csv 72 > a25k-bads-v2c-head-2.csv

