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
                        nargs="+",
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
   # wanted_kw = set([kw.lower() for kw in args.keyword])
    wanted_kw = set(map(str.lower, args.keyword))
    skip_taxa = set(map(str.lower, args.skiptaxa or []))
    num_taken, num_skipped = 0,0

    for rec in SeqIO.parse(args.file, 'swiss'):
        annots = rec.annotations

        taxa = annots.get('taxonomy')
        if taxa:
            taxa = set(map(str.lower, taxa))
            if skip_taxa.intersection(taxa):
                num_skipped +=1
                continue

        keywords = annots.get('keywords')
        if keywords:
            keywords = set(map(str.lower, keywords))
            if wanted_kw.intersection(keywords):
                num_taken +=1
                SeqIO.write(rec, args.outfile, 'fasta')
            else:
                num_skipped += 1


    print(f'Done, skipped {num_skipped} and took {num_taken}. See output in "{args.outfile.name}".')



    #print(keywords.intersection(set(annots.get('keywords'))))



    # recskipped = 0
    #
    # if args.skiptaxa:
    #     skip = set(map(str.lower, args.skiptaxa))
    #
    # totaltake = 0
    #
    # for rec in SeqIO.parse(args.file, "swiss"):
    #     if 'taxonomy' in rec.annotations:
    #         taxonomy = rec.annotations["taxonomy"]
    #         taxa = set(map(str.lower, taxonomy))
    #         skipped = skip.intersection(taxa)
    #         recskipped += len(skipped)
    #         if skipped == True:
    #             next(rec)
    #     else:
    #         if 'keywords' in rec.annotations:
    #             keywords = rec.annotations["keywords"]
    #             keys = set(map(str.lower, keywords))
    #             totaltake += len(keys)
    #             if keys == True:
    #               SeqIO.write(rec, args.outfile, 'fasta')
    #             else: next()
    #
    # print(f'Done, skipped {recskipped} and took {totaltake}. See output in "{args.outfile.name}".')





# --------------------------------------------------
if __name__ == '__main__':
    main()
