#!/usr/bin/env python3
"""
Author : edwin
Date   : 2020-04-08
Purpose: Rock the Casbah
"""

import argparse
import os
import sys
#import Bio
#from Bio import Seq
#from Bio import SeqIO



# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Probabistically subset FASTA files',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='+',
                        help='Readable file(s)',
                        type=argparse.FileType('r'))

    parser.add_argument('-p',
                        '--pct',
                        help='Percent of reads',
                        metavar='reads',
                        type=float,
                        default=0.1)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed value',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory',
                        metavar='DIR',
                        default='out')


    args = parser.parse_args()

    if not 0 < args.pct < 1:
        parser.error(f'--pct "{args.pct}" must be between 0 and 1')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    print(args)


# --------------------------------------------------
if __name__ == '__main__':
    main()
