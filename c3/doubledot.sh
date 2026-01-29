#!/bin/sh
python doubledot.py > doubledot-output.txt
python ../texify.py doubledot.py
python ../texify.py doubledot-output.txt
