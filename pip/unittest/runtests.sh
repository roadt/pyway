#!/bin/bash

#module
python -m unittest test_basic
#file/path
python -m unittest test_basic.py
#print more/details
python -m unittest -v test_basic
#discover
python -m unittest
python -m unittest discover
python -m unittest discover -p test*.py  
python -m unittest discover -p test*.py  -s . -t .
#help 
python -m unittest -h


#Options
# fail-fast
python -m unittest -f
# show localvars
python -m unittest --locals
# filter-by-name
python -m unittest --locals -k basic



