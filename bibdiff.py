#!/usr/bin/env python3

import biblib
import argparse

parser = argparse.ArgumentParser(description='Compute the symmetrical difference of two or more bibtext files')

parser.add_argument('files', type=str, help='comma separated list of files')
parser.add_argument('output', type=str, help='the output file')

args = parser.parse_args()

if args.files:
    bibs = args.files.split(',')
    for bib in bibs:
        print(bib)


def compute_diff(bibs):
    tex = []
    for bib in bibs:
       tex.append(biblib.FileBibDB(bib, mode='r')) 
    

def write_diff(output, bib):
    pass