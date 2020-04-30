#!/usr/bin/env python3
"""
Author : edwin
Date   : 2020-04-29
Purpose: Rock the Casbah
"""

import argparse
import os
import sys
from Bio import SeqIO
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default=None)

    parser.add_argument('-k',
                        '--keyword',
                        help='Keyword to take',
                        metavar='str',
                        type=str,
                        default=None,
                        required=True)

    parser.add_argument('-s',
                        '--skiptaxa',
                        help='Taxa to skip',
                        nargs='*',
                        metavar='str',
                        type=str,
                        default=None)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='out.fa')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    recskipped = 0

    if args.skiptaxa:
        skip = set(map(str.lower, args.skiptaxa))

    totaltake = 0

    for rec in SeqIO.parse(args.file, "swiss"):
        if 'taxonomy' in rec.annotations:
            taxonomy = rec.annotations["taxonomy"]
            taxa = set(map(str.lower, taxonomy))
            skipped = skip.intersection(taxa)
            recskipped += len(skipped)
            if skipped == True:
                next(rec)
        else:
            if 'keywords' in rec.annotations:
                keywords = rec.annotations["keywords"]
                keys = set(map(str.lower, keywords))
                totaltake += len(keys)
                if keys == True:
                  SeqIO.write(rec, args.outfile, 'fasta')
                else: next()

    print(f'Done, skipped {recskipped} and took {totaltake}. See output in "{args.outfile.name}".')





# --------------------------------------------------
if __name__ == '__main__':
    main()
