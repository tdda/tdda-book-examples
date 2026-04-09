#!/bin/sh
set -e
python ../replify.py pd-serde.py
python repl_pd-serde.py | fold -s
python ../json-diff-except.py simple3x2.tight.serial simple3x2.serial writer
