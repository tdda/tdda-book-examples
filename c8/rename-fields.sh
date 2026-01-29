#!/bin/sh
head -1 accounts1k.csv | sed s/_//g > accounts1k_clean.csv
tail +2 accounts1k.csv >> accounts1k_clean.csv
