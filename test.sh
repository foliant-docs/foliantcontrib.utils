#!/bin/bash

# Tests for preprocessor_ext require the utils module
# to be installed: pip3 install .

python3 -m doctest docs/*.md &&\
    python3 -m unittest discover -v &&\
    mypy ./foliant/ --ignore-missing-imports &&\
    cd test_pext && python3 -m unittest test_preprocessor_ext.py
