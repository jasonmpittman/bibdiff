#!/usr/bin/env python3

import argparse
import os
import sys

sys.path.append('biblib')
import biblib.bib

def main():
    parser = argparse.ArgumentParser(description='Outputs a set of unique citation keys from two or more bibtext files')

    parser.add_argument('files', nargs='+', help='list of bib files', type=open)

    args = parser.parse_args()

    try:
        citeKeys = set()
        
        for f in args.files:
            bib = biblib.bib.Parser().parse(f, log_fp=sys.stderr).get_entries()
            for k in bib.keys():
                citeKeys.add(k)
        
        print(citeKeys)             

    except Exception as e:
        print(str(e))



if __name__ == "__main__":
    main()