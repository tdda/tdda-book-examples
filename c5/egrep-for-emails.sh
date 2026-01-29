#!/bin/sh
egrep '(flily|damber|ylucas)' accounts25k.csv | cut -f 5,7-10,13 -d,
