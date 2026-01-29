#!/bin/sh
set -e
sh dump-doubledot.sh
python test_sh_dump_doubledot_sh.py
