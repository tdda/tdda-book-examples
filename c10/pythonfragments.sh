set -x
#!/bin/sh

python ../replify.py 123.py
python ../replify.py dictorder.py
python ../replify.py jsondictorder.py
python ../replify.py jsondictorder2.py
python ../replify.py indentedjson.py

python repl_123.py > 123.txt
python repl_dictorder.py > dictorder.txt
python repl_jsondictorder.py > jsondictorder.txt
python repl_indentedjson.py > indentedjson.txt
python repl_jsondictorder2.py | tail -4 > jsondictorder2.txt
