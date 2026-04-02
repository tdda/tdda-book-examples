#!/bin/sh
set -x
grep impossible alice.txt | wc -l
grep Alice alice.txt | wc -l


