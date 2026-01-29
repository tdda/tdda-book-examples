#!/bin/sh
grep -o "$1" "$2" | wc -l
