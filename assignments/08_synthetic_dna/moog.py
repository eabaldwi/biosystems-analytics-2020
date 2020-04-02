#!/usr/bin/env python3
"""
Author : edwin
Date   : 2020-04-01
Purpose: Rock the Casbah
"""

import argparse
import os
import sys
import random

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
                        type=argparse.FileType('wt'),
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

    args = parser.parse_args()
    if not 0 < args.pctgc < 1:
        parser.error(f'--pctgc "{args.pctgc}" must be between 0 and 1')


    return parser.parse_args()

#--------------------------------------------
def create_pool(pctgc, max_len, seq_type):
    """ Create the pool of bases """

    t_or_u = 'T' if seq_type == 'dna' else 'U'
    num_gc = int((pctgc / 2) * max_len)
    num_at = int(((1 - pctgc) / 2) * max_len)
    pool = 'A' * num_at + 'C' * num_gc + 'G' * num_gc + t_or_u * num_at

    for _ in range(max_len - len(pool)):
        pool += random.choice(pool)

    return ''.join(sorted(pool))

# --------------------------------------------------
#  def test_create_pool():
#     """ Test create_pool """
#
#     state = random.getstate()
#     random.seed(1)
#     assert create_pool(.5, 10, 'dna') == 'AAACCCGGTT'
#     assert create_pool(.6, 11, 'rna') == 'AACCCCGGGUU'
#     assert create_pool(.7, 12, 'dna') == 'ACCCCCGGGGGT'
#     assert create_pool(.7, 20, 'rna') == 'AAACCCCCCCGGGGGGGUUU'
#     assert create_pool(.4, 15, 'dna') == 'AAAACCCGGGTTTTT'
#     random.setstate(state)

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    pool = create_pool(args.pctgc, args.maxlen, args.seqtype)

    for i in range(args.numseqs):
        seq_len = random.randint(args.minlen, args.maxlen)
        seq = ''.join(random.sample(pool, seq_len))
        args.outfile.write(f'>{i+1} \n'
                           f'{seq} \n')


    print(f'Done, wrote {args.numseqs} {args.seqtype.upper()} '
          f'sequences to "{args.outfile.name}".')




# --------------------------------------------------
if __name__ == '__main__':
    main()
