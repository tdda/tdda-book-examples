#!/bin/sh
set -e
sh nfkc.sh
python test_sh_nfkc_sh.py
