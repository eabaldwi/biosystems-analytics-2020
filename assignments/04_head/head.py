#!/usr/bin/env python3
"""
Author : edwin
Date   : 2020-02-25
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

    parser.add_argument('FILE',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default=None)

    parser.add_argument('-n',
                        '--number',
                        help='Number of lines (default: 10)',
                        metavar='int',
                        type=int,
                        default=10)


    args = parser.parse_args()
    if args.number <= 0:
        parser.error(f'--num "{args.number}" must be greater than 0')
    elif args.number is None:
        args.number = 10

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    num_lines = 0

    for line in args.FILE:
        num_lines += 1
        if num_lines <= args.number:
            print(line.strip())

# --------------------------------------------------
if __name__ == '__main__':
    main()
