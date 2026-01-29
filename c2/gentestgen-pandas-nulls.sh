#!/bin/sh
set -e
python pandas-nulls.py t
python test_python_pandas_nulls_py_t.py
