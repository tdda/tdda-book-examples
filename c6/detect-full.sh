#!/bin/sh
python detect_enhanced_accounts.py accounts25k.parquet \
       accounts-enhanced.tdda a25k-enhanced-bads.csv
