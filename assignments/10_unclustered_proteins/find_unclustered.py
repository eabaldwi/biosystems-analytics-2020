#!/usr/bin/env python3
"""
Author : edwin
Date   : 2020-04-15
Purpose: Rock the Casbah
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-p',
                        '--proteins',
                        metavar='proteins',
                        help='Proteins FASTA',
                        type=argparse.FileType('r'),
                        required=True)

    parser.add_argument('-c',
                        '--cdhit',
                        help='Output file from CD-HIT',
                        metavar='cdhit',
                        type=argparse.FileType('rt'),
                        required=True)

    parser.add_argument('-o',
                        '--outfile',
                        help='output file',
                        metavar='outfile',
                        type=argparse.FileType('wt'),
                        default='unclustered.fa')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    print(args.proteins)



# --------------------------------------------------
if __name__ == '__main__':
    main()
