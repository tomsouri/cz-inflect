#!/bin/bash

mkdir -p .venv
python3 -m venv .venv
.venv/bin/pip install --no-cache-dir --upgrade pip setuptools
.venv/bin/pip3 install --no-cache-dir -r requirements.txt

echo "Succesfully installed all requirements for the library."
echo "You can run the inflection script from this directory by running .venv/bin/python3 inflect.py."
echo "Then enter one lemma per line and the script outputs tab-separated inflected forms."