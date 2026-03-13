#!/bin/sh
set -e
cp simple3x2.csv foo.csv
tdda serial --generate foo.csv foo.serial


