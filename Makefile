# Makefile for some examples and TDDD aspects of the book
#
# Two tests are have been commented out because the require the Miró system which
# is not widely available. All other tests should be capable of running
#
# Generally speaking, the 'tests' target runs code to generate test output used
# in the book, some of which result in TeX macro definitions in results-defs.tex.
#
# The 'tex' target converts text files into a safe form for processing
# with \VerbatimInput and similar macros, (though depend on some other macros
# used in the book).
#
# Use:
#
#    make               to run the 'tests' targets then the 'tex' targets
#    make tests         to run all the tests
#    make tex           to convert all the outputs for (La)TeX



.PHONY:
all: tests tex


.PHONY:
tex:  clean \
      c3/eacute-tex.py \
      c3/doubledot-tex.py \
      c3/nfkc-tex.py \
      c3/byteseq-tex.py \
      c3/doubledot-hexdump-tex.txt \
      c5/a25k-bads-v2c-tex.txt \
      c5/a25k-bads-v2c-dates-tex.txt \
      c5/a25k-bads-v2c-address-tex.txt \
      c5/a25k-bads-v2c-tel-email-tex.txt \
      c5/a25k-bads-v2c-account-type-card-number-tex.txt \
      c6/detect-enhanced-output-tex.txt \
      c7/bad-books-tex.txt \
      c14/ieee64-tex.py


.PHONY:
tests:
	# (cd c2; sh gentestgen-ch-company-names.sh)  # requires Miró
	(cd c2; sh gentestgen-empty.sh)
	(cd c2; sh gentestgen-pandas-nulls.sh)
	(cd c3; sh gentestgen-codings1.sh)
	(cd c3; sh gentestgen-codings2.sh)
	(cd c3; sh gentestgen-hearts.sh)
	(cd c3; sh gentestgen-hearts.sh)
	# (cd c4; sh gentestgen-price-delta.sh)       # requires Miró
	(cd c5; sh gentestgen-email-regex.sh)
	(cd c5; sh gentestgen-n-plausible-postcodes.sh)
	cat c[1-9]/ref/*/*-defs.tex c[1-9][0-9]/ref/*/*-defs.tex > results-defs.tex



.PHONY:
clean:
	rm -f *-tex.* c*/*-tex.*

c3/eacute-tex.py: c3/eacute.py c3/gentestgen-eacute.sh
	(cd c3; sh gentestgen-eacute.sh)

c3/doubledot-tex.py: c3/doubledot.py
	(cd c3; sh gentestgen-doubledot.sh)

c6/detect-enhanced-output-tex.txt: c6/detect-enhanced-output.txt
	python texify.py c6/detect-enhanced-output.txt


c7/bad-books-tex.txt: c7/bad-books.txt
	python texify.py c7/bad-books.txt

c3/nfkc-tex.py: c3/nfkc.py c3/gentestgen-nfkc.sh
	(cd c3; sh gentestgen-nfkc.sh)

c3/doubledot-hexdump-tex.txt: c3/doubledot.py c3/gentestgen-dump-doubledot.sh
	(cd c3; sh gentestgen-dump-doubledot.sh)

c3/byteseq-tex.py: c3/byteseq.py
	python texify.py c3/byteseq.py

c5/a25k-bads-v2c-tex.txt: c5/a25k-bads-v2c.txt
	python texify-nl.py c5/a25k-bads-v2c.txt

c5/a25k-bads-v2c-dates-tex.txt: c5/a25k-bads-v2c-dates.txt
	python texify-nl.py c5/a25k-bads-v2c-dates.txt

c5/a25k-bads-v2c-address-tex.txt: c5/a25k-bads-v2c-address.txt
	python texify-nl.py c5/a25k-bads-v2c-address.txt

c5/a25k-bads-v2c-tel-email-tex.txt: c5/a25k-bads-v2c-tel-email.txt
	python texify-nl.py c5/a25k-bads-v2c-tel-email.txt

c5/a25k-bads-v2c-account-type-card-number-tex.txt: c5/a25k-bads-v2c-account-type-card-number.txt
	python texify-nl.py c5/a25k-bads-v2c-account-type-card-number.txt

c9/Makefile-Alice1-tex: c9/alice/Makefile
	python texify.py c9/alice/Makefile \
               Makefile-Alice1-tex

c14/ieee64-tex.py: c14/ieee64.py
	python texify.py c14/ieee64.py

