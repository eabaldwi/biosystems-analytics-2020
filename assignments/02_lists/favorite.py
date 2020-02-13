#!/usr/bin/env python3
"""
Author : edwin
Date   : 2020-02-12
Purpose: Rock the Casbah
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='A few of my favorite things',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('thing',
                        metavar='str',
                        nargs='+',
                        help='Some of my favorite things')

    parser.add_argument('-s',
                        '--sep',
                        help='A separator ',
                        metavar='str',
                        type=str,
                        default=', ')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Add args, assign variables"""

    args = get_args()
    things = args.thing
    num = len(things)
    items = ''

    if args.sep:
        items = ''.format(things)

    if num == 1:
        items = things[0]
        print(items)
        print('This is one of my favorite things.')

    else:
        items = f'{args.sep}'.join(things)
        print(items)
        print('These are a few of my favorite things.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
