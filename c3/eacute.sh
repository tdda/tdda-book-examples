#!/bin/sh
python eacute.py > eacute-output.txt
python ../texify.py eacute.py
python ../texify.py eacute-output.txt
