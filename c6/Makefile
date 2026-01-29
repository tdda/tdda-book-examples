.PHONY:
all: clean \
     us-states-count.csv \
     us-states-count.tdda \
     n-records-extract.txt \
     accounts-enhanced.tdda \
     accounts-enhanced-extract.tdda \
     accounts-enhanced-extract-edited.tdda \
     us-area-stats.csv
	echo Done


.PHONY:
clean:
	rm -f us-states-count.csv \
              us-states-count.tdda \
              n-records-extract.txt \
              accounts-enhanced.tdda \
              accounts-enhanced-extract.tdda \
              accounts-enhanced-extract-edited.tdda \
              us-area-stats.csv


us-states-count.csv: test_pqrecords.py us-area-stats.csv
	python test_pqrecords.py

us-states-count.tdda: test_discover_us.py us-area-stats.csv
	python test_discover_us.py

n-records-extract.txt: us-states-count.tdda
	python test_n_records.py

accounts-enhanced.tdda: test_disco_enhanced.py \
                        enhance_accounts.py \
                        accounts1k.parquet
	python test_disco_enhanced.py

accounts-enhanced-extract.tdda: test_enhanced_extract.py \
                                accounts-enhanced.tdda \
                                cut-accounts-enhanced.awk
	python test_enhanced_extract.py

accounts-enhanced-extract-edited.tdda: cut-hand.sh \
                                       cut-hand.awk \
                                       accounts-enhanced-extract.tdda
	python test_cut_hand.py

us-area-stats.csv: grouped.py
	python test_grouped.py
