#!/bin/sh
set -x
tdda serial foo-metadata.json foo.serial    # CSVW --> tdda.serial
tdda serial --to csvw a.serial a.json       # tdda.serial --> CSVW
tdda serial --to pd.r a.serial a-pdr.serial # tdda.serial --> Pandas read_csv
tdda serial --to pl.r a.serial a-plr.serial # tdda.serial --> Polars read_csv
tdda serial --to pd.r a.serial pdread.py
tdda serial --to pd.r a.serial pdread.py

