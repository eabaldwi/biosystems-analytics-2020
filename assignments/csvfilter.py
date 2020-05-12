#!/usr/bin/env python3
"""
Author : Edwin
Date   : 2020-05-11
Purpose: Final
"""

import argparse
import os
import sys
import csv
import re
#from Bio import SeqIO



# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Filter delimited records',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default=None,
                        required=True)

    parser.add_argument('-v',
                        '--val',
                        help='Value for filter',
                        metavar='val',
                        type=str,
                        default=None,
                        required=True)

    parser.add_argument('-c',
                        '--col',
                        help='column for filter',
                        metavar='val',
                        type=str,
                        default='')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='OUTFILE',
                        type=argparse.FileType('wt'),
                        default='out.csv')

    parser.add_argument('-delim',
                        '--delimiter',
                        help='Input delimiter',
                        metavar='delim',
                        type=str,
                        default=',')

    args = parser.parse_args()

    reader = csv.DictReader(args.file, delimiter=args.delimiter)

    if not args.col in reader.fieldnames:
        parser.error(f'--col "{args.col}" is not a valid column!')

    return args

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    search_for = args.val
    search_col = args.col

    reader = csv.DictReader(args.file, delimiter=args.delimiter)

    if search_col not in reader.fieldnames:
        sys.stderr.write(f'--col "{args.col}" is not a valid column!')

    writer = csv.DictWriter(args.outfile, fieldnames=reader.fieldnames)
    writer.writeheader()

    num_written = 0


    for rec in reader:
        print(type(rec))

        # searched = text.get(value)
        #
        # if column == True:
        #     re.search(args.val, column, re.IGNORECASE)
        #     writer.writerows(rec)
        # else:
        #     if re.search(args.val, column, re.IGNORECASE):
        #         num_written += 1
        #         writer.writerows(rec)
        # print(rec)

        # if num_taken == 5:
        #     break
        # else:
        #     next


    print(f'Done, wrote {num_written} to {args.outfile.name}.')


    # wanted_kw = set([kw.lower() for kw in args.keyword])
    # wanted_kw = set(map(str.lower, args.keyword))
    # skip_taxa = set(map(str.lower, args.skiptaxa or []))
    # num_taken, num_skipped = 0, 0
    #
    # for rec in SeqIO.parse(args.file, 'swiss'):
    #     annots = rec.annotations
    #
    #     taxa = annots.get('taxonomy')
    #     if taxa:
    #         taxa = set(map(str.lower, taxa))
    #         if skip_taxa.intersection(taxa):
    #             num_skipped += 1
    #             continue
    #
    #     keywords = annots.get('keywords')
    #     if keywords:
    #         keywords = set(map(str.lower, keywords))
    #         if wanted_kw.intersection(keywords):
    #             num_taken += 1
    #             SeqIO.write(rec, args.outfile, 'fasta')
    #         else:
    #             num_skipped += 1



# --------------------------------------------------
if __name__ == '__main__':
    main()