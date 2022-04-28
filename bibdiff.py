#!/usr/bin/env python3

import argparse
import os
import sys

sys.path.append('biblib')
import biblib.bib


parser = argparse.ArgumentParser(description='Compute the symmetrical difference of two or more bibtext files')

parser.add_argument('files', nargs='+', help='list of bib files', type=open)
parser.add_argument('output', type=str, help='the output file')

args = parser.parse_args()

try:
    citeKeys = set()
    for f in args.files:
        db = biblib.bib.Parser().parse(f, log_fp=sys.stderr).get_entries()
        for k in db.keys():
            citeKeys.add(k)

    print(citeKeys)

except Exception as e:
    print(str(e))

def write_diff(output, bib):
    pass

