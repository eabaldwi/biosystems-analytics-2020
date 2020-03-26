#!/usr/bin/env python3
"""
Author : edwin
Date   : 2020-03-25
Purpose: Rock the Casbah
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Transcribe sequences',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='+',
                        help='Readable file(s)',
                        type=argparse.FileType('r'),
                        default=[sys.stdin])

    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory',
                        metavar='DIR',
                        default='out')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    out_dir = args.outdir

    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)


    files = 0
    tot_seq = 0

    for fh in args.file:
        files += 1
        out_file = os.path.join(out_dir, os.path.basename(fh.name))
        out_fh = open(out_file, 'wt')
        sequences = 0

        for line in fh:
            sequences += 1
            transcript = []
            for char in line.strip():
                if char in 'T':
                    transcript.append('U')
                else:
                    transcript.append(char)
            print(''.join(transcript), file=out_fh)
        tot_seq += sequences

    if sequences > 1 and files > 1:
        print(f'Done, wrote {tot_seq} sequences in {files} files to directory "{args.outdir}".')
    elif sequences > 1 and files == 1:
        print(f'Done, wrote {sequences} sequences in {files} file to directory "{args.outdir}".')
    else:
        print(f'Done, wrote {sequences} sequence in {files} file to directory "{args.outdir}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
