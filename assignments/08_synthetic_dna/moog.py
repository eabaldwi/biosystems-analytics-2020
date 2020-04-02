#!/usr/bin/env python3
"""
Author : edwin
Date   : 2020-04-01
Purpose: Rock the Casbah
"""

import argparse
import os
import sys

# import Bio
# import re
# import string
# from subprocess import getstatusoutput
# from Bio import SeqIO
# from Bio.SeqUtils import GC
# from numpy import mean
# from itertools import chain


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default='out.fa')

    parser.add_argument('-t',
                        '--seqtype',
                        help='The sequence type, either dna or rna',
                        metavar='str',
                        type=str,
                        default='dna',
                        choices=['dna','rna'])

    parser.add_argument('-n',
                        '--numseqs',
                        help='The number of sequences to generate',
                        metavar='int',
                        type=int,
                        default=10)

    parser.add_argument('-m',
                        '--minlen',
                        help='The minimum length for any sequence',
                        metavar='int',
                        type=int,
                        default=50)

    parser.add_argument('-x',
                        '--maxlen',
                        help='The maximum length for any sequence',
                        metavar='int',
                        type=int,
                        default=75)

    parser.add_argument('-p',
                        '--pctgc',
                        help='The average percentage og GC content for a sequence',
                        metavar='float',
                        type=float,
                        default=0.5)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    print(args)



# --------------------------------------------------
if __name__ == '__main__':
    main()
