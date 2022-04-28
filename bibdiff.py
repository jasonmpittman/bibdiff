#!/usr/bin/env python3

__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2022"
__credits__ = ["Jason M. Pittman"]
__license__ = "GPLv3"
__version__ = "0.1.0"
__maintainer__ = "Jason M. Pittman"
__email__ = "jason@jasonmpittman.com"
__status__ = "Beta"

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
        
        for k in citeKeys:
            print(k)             

    except Exception as e:
        print(str(e))



if __name__ == "__main__":
    main()