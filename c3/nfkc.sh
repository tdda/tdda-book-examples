#!/bin/sh
python nfkc.py > nfkc-output.txt
python ../texify.py nfkc.py
python ../texify.py nfkc-output.txt
# Not actually the output directly used.
# But this is what is tested.
# If the test fails, the included output might be outdated.