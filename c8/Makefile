.PHONY:
all: clean \
     prt-output.sh \
     accounts1k_clean.csv \
     pdr_syntax.py \
     pdw_syntax.py \
     json_pdr_syntax.py \
     repl_e3head_pl.py \
     e3head-pl.txt \
     repl_e3head_pd.py \
     e3head-pd.txt \
     repl_e3head_pd.py \
     e3head-pd.txt
	echo Done


.PHONY:
clean:
	rm -f prt-output.sh \
              accounts1k_clean.csv \
     pdr_syntax.py \
     pdw_syntax.py \
     json_pdr_syntax.py \
     repl_e3head_pl.py \
     e3head-pl.txt \
     repl_e3head_pd.py \
     e3head-pd.txt \
     repl_e3head_pd.py \
     e3head-pd.txt


prt-output.sh: prt.sh ../replify.py
	python test_prt.py


accounts1k_clean.csv: rename-fields.sh accounts1k.csv
	python test_rename_fields.py


pdr_syntax.py:
pdw_syntax.py:
json_pdr_syntax.py: test_pandas_rw_repls.py pandas_rw.py read.awk write.awk
	python test_pandas_rw_repls.py

repl_e3head_pl.py:
repl_e3head-pl.txt:
e3head-pl.txt: e3head_pl.py e3head-pl.sh elements3-old.parquet
	python test_e3head_pl.py

repl_e3head_pd.py:
repl_e3head-pd.txt:
e3head-pd.txt: e3head_pd.py e3head-pd.sh elements3-old.parquet
	python test_e3head_pd.py

repl_e3head_pd_nl.py:
repl_e3head-pd-nl.txt:
e3head-pd-nl.txt: e3head_pd_nl.py e3head-pd-nl.sh elements3-old.parquet
	python test_e3head_pd_nl.py

