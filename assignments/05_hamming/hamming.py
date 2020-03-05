#!/usr/bin/env python3
"""
Author : edwin
Date   : 2020-03-02
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




    parser.add_argument('file',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default=None)

    parser.add_argument('-m',
                        '--min',
                        help='A named integer argument',
                        metavar='int',
                        type=int,
                        default=0)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

#given two strings are they even the same length

    args = get_args()


    count = 0
    tot = 0
    words = {}

    for line in args.file:

        word1, word2 = line.split()
        count = abs(len(word1) - len(word2))

        for c1, c2 in zip(word1, word2):
            if c1 == c2:
                count += 0
            elif c1 != c2:
                count += 1
        if count >= args.min:
            print(f'{count:8}:{word1:20}{word2:20}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
