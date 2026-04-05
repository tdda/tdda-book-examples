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
     e3head-pd.txt \
     repl_pd-serde.py \
     repl_load_e3old_pl.py \
     repl_load_e3old_pd.py \
     rest
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
	python ../simcmd.py 'head -1 accounts1k.csv | sed s/_//g > accounts1k_clean.csv' c1.txt
	python ../simcmd.py 'tail +2 accounts1k.csv >> accounts1k_clean.csv' c2.txt
	cat c1.txt.tex c2.txt.tex > rename-fields-tex.txt

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

repl_pd-serde.py: pd-serde.py pd-serde.sh
	sh pd-serde.sh

repl_load_e3old_pl.py: load_e3old_pl.py
	sh load_e3old_pl.sh

repl_load_e3old_pd.py: load_e3old_pd.py
	sh load_e3old_pd.sh


.PHONY:
rest:
	python test_e3head_pd_nl.py
	python test_e3head_pd.py
	python test_e3head_pl.py
	python test_gen_foo_serial.py
	python test_pandas_rw_repls.py
	python test_prt.py
	python test_python_bookdata_py.py
	python test_python_pandas_rw_py.py
	python test_python_pydantic_bookdata_json_py.py
	python test_python_pydantic_bookdata_py.py
	python test_rename_fields.py
	python test_sh_csvw_validate_ddd_sh.py
	python test_sh_fless_describe_json_sh.py
	python test_sh_fless_describe_yaml_sh.py
	python test_sh_fless_package_to_serial_sh.py
	python test_sh_fless_resource_to_serial_sh.py
	python test_sh_gen_fless_3x2_package_sh.py
	python test_sh_gen_fless_3x2_resource_sh.py
	python test_sh_gen_foo_serial_sh.py
	python test_sh_simple3x2_to_pdr_serial_sh.py
	python test_sh_tddadiff1_sh.py
	python test_sh_pd_serde_sh.py
	python test_sh_load_e3old_pl_sh.py
	python test_sh_load_e3old_pd_sh.py

