#!/bin/sh
grep 'Above +' doubledot.py | python byteseq.py | head -1
grep 'Below +' doubledot.py | python byteseq.py | head -1
