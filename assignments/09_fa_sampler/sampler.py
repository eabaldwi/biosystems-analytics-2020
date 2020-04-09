#!/usr/bin/env python3
"""
Author : edwin
Date   : 2020-04-08
Purpose: Rock the Casbah
"""

import argparse
import os
import sys
import random
#import Bio
#from Bio import Seq

from Bio import SeqIO
# import biopython
# from biopython import Seq
# from biopython import SeqIO



# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Probabistically subset FASTA files',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='+',
                        help='Input FASTA file(s)',
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
    random.seed(args.seed)

    out_dir = args.outdir

    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)

    num_seqs = 0
    num_files = 0
    sequences = 0

    for fh in args.file:
        num_files +=1
        basename = os.path.basename(fh.name)
        out_file = os.path.join(args.outdir, basename)
        print(f'{num_files:3}: {basename}')
        out_fh = open(out_file, 'wt')

        for rec in SeqIO.parse(fh, 'fasta'):
            if random.random() <= args.pct:
                SeqIO.write(rec, out_fh, 'fasta')
                sequences += 1
            num_seqs += sequences

        out_fh.close()

    if num_seqs > 1 and num_files > 1:
        print(f'Wrote {num_seqs} sequences in {num_files} files to directory "{args.outdir}"')
    elif sequences > 1 and num_files == 1:
        print(f'Wrote {num_seqs} sequences in {num_files} file to directory "{args.outdir}"')
    else:
        print(f'Wrote {num_seqs} sequence in {num_files} file to directory "{args.outdir}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
