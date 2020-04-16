#!/usr/bin/env python3
"""
Author : edwin
Date   : 2020-04-15
Purpose: Rock the Casbah
"""

import argparse
import os
import sys
import re
from Bio import SeqIO


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

    clustered_ids = {}

    for line in args.cdhit:
        if line.startswith('>'):
            continue

        #print(f'line "{line}"')


        match = re.search(r'>(\d+)', line)
        if match:
            prot_id = match.group(1)
            clustered_ids.add(prot_id)


  #  print(len(clustered_ids))
    num_total = 0
    num_written = 0

    for rec in SeqIO.parse(args.proteins, 'fasta'):
        num_total += 1
        # match2 = re.search(r'>(\d+)', rec.id)
        # if match2:
        #     prot_id = match2.group(1)
        prot_id = re.sub('\|.*', '', rec.id)

        if prot_id not in clustered_ids:
            num_written += 1
            Seq.IO.write(rec, args.outfile, 'fasta')

       # break

    print(f'Wrote {num_written:,} of {num_total:,} unclustered proteins to "{args.outfile.name}"')





# --------------------------------------------------
if __name__ == '__main__':
    main()
