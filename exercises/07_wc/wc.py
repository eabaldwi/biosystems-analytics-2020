#!/usr/bin/env python3
"""
Author : edwin
Date   : 2020-02-20
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
                        metavar='FILE',
                        nargs='*',
                        default=[sys.stdin],
                        type=argparse.FileType('r'),
                        help='Input file(s)')
#order above doesnt matter, except for 'file' because thats the name of the argument
    #for head we just will do one i think
    #will need to do -n and --number as type int for head


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    total_lines, total_words, total_chars = 0, 0, 0
    #needs to be outside the for loop because you want to track ALL the files, not just the one in the for loop
    for fh in args.file:
        num_lines, num_words, num_chars = 0, 0, 0
        for line in fh:
            num_lines += 1
            words = line.split()
            num_words += len(words)
            num_chars += len(line)

        total_lines += num_lines
        total_words += num_words
        total_chars += num_chars

        print(f'{num_lines:8}{num_words:8}{num_chars:8} {fh.name}')
#spaces count in the f string so be sure to remove them
#outside of the loop we need to say if there is more than one file the do the total
    if len(args.file) > 1:
        print(f'{total_lines:8}{total_words:8}{total_chars:8} total')

#f string with formatting information inside, use a colon : then character to tell it how long the field is

#        print(num_lines, num_words, num_chars)

#        print(fh.readline(), end='')

# --------------------------------------------------
if __name__ == '__main__':
    main()
