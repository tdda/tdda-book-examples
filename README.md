# tdda-book-examples: Examples from the TDDA Book

This repo contains all the example code and output from the book.

**Test-Driven Data Analysis**  
Nicholas J. Radcliffe  
CRC Press/Chapman and Hall/Taylor & Francis  
2026


# Organization

The examples are organized by chapter in directories `c2` to `c17`,
for those chapters that include examples.


# Test-Driven Document Development (TDDD) and Extra Files

Many of the examples in the book, particularly from the early chapters,
were verified/product using test-driven document development (TDDD).
This is described briefly in the book in section 9.8 in Chapter 9,
which can be read online
[here](https://book.tdda.info/book/chapter9.html#testdriven-document-development-tddd).

The `Makefile` in this directory allows most of the TDDD tests to be run
and has some documentation at the top explaining a little more about
how it all works.




## Cross-Platform validations

Currently just the IEEE754 float64 code in `ieee64.py` and associated tests.

Tested on:
  - MacBook Pro, 2.3 GHz 8-Core Intel Core i9, running MacOS Sonoma 14.7
     - Python 3.12.4, numpy 1.26.4
     - Python 3.11.2, numpy 1.26.4
     - Python 3.10.10, numpy 1.23.2
     - Python 3.9.16, numpy 1.25.2

  - Mac Studio Ultra, M1 Ultra processor, running MacOS Sonoma 14.7
    - Python 3.12.6, numpy 2.1.3
    - Python 3.11.0, numpy 1.23.5
    - Python 3.10.4, numpy 1.25.2
    - Python 3.7, numpy 1.12.4

  - Linux 6.2.9-x86_64-linode160 on x86-64 (Linode)
    CentOS 7, Kernel 6.2.9-x86_64-linode160
    - Python 3.11.5, numpy 1.25.2
    - Python 3.6.8, numpy 1.19.5

  - Mac M3 Pro
    - Python 3.11.9, numpy 2.1.3

