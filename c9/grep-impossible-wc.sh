#!/bin/sh
set -e
(cd alice; grep impossible alice.txt | wc -l)
(cd alice; grep Alice alice.txt | wc -l)
