#!/usr/bin/env python3
"""
Author : edwin
Date   : 2020-03-19
Purpose: Rock the Casbah
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Codon translation',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('seq',
                        metavar='str',
                        help='Input sequence')


    parser.add_argument('-c',
                        '--codons',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        required=True)

    parser.add_argument('-o',
                        '--outfile',
                        help='output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='out.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    seq = args.seq.upper()

    codons = {}

    for line in args.codons:
        codon, protein = line.upper().split()
        codons[codon] = protein

    k = 3
    proteins = []
    for codon in [seq[i:i + k] for i in range(0, len(seq) - k + 1, k)]:
        proteins.append(codons.get(codon, '-'))

    print(''.join(proteins), file = args.outfile)

    print(f'Output written to "{args.outfile.name}".')



# --------------------------------------------------
if __name__ == '__main__':
    main()
