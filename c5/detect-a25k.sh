#!/bin/sh
tdda detect accounts25k.parquet accountsv2.tdda a25k-bads-v2c.csv \
     --report txt --key account_number
