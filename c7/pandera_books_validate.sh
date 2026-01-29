#!/bin/sh
python pandera_books_validate.py | tail +3 > pandera_books_results.json
python unwrap.py pandera_books_results-tight.json pbr-actual-expanded.json
python unwrap.py pandera_books_results.json pbr-ref-expanded.json
diff pbr-actual-expanded.json pbr-ref-expanded.json
