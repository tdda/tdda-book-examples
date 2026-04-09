python ../replify.py csv_pdl_roundtrip_pandas.py
python ../replify.py read_pdl_polars.py
python repl_csv_pdl_roundtrip_pandas.py | fold -s > csv_pdl_roundtrip.txt
python repl_read_pdl_polars.py | fold -s > read_pdl_polars.txt
sed -n 4p csv_pdl_roundtrip.txt > repl_df2.txt
sed -n 5,9p csv_pdl_roundtrip.txt > repl_pd2csv.txt
sed -n 2,3p read_pdl_polars.txt > repl_pl_pdl.txt
