#!/bin/sh
python codings2.py > codings2-out.txt
python 2col.py codings2-out.txt 44
# Note, was is checked is codings2-out-2-col.svg
# This is not quite what's used in the book, which is a PDF image
# straight from the terminal.
# But converting to PDF reliably with weird characters is too hard.
# If the test fails, the codings2.pdf image might be out of date.



