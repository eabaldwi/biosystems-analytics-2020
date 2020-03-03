#!/usr/bin/env python3
"""
Author : edwin
Date   : 2020-02-06
Purpose: Chapter 4 picnic
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Picnic',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items',
                        metavar='str',
                        help='Things to bring to a picnic',
                        nargs= '+')

    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items alphabetically',
                        action= 'store_true')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.items

    #print(f'sorted = "{args.sorted}"')
    if args.sorted:
#        items = sorted(items)
        items.sort()

    if len(items) == 1:
        print(f'You are bringing {args.items[0]}.')
    elif len(items) == 2:
        print(f'You are bringing {items[0]} and {items[1]}.')
        #print(f'You are bringing {}'.format(' and '.join(items)))
    else:
        print('You are bringing {}, and {}.'.format(','.join(items[:-1]),items[-1]))
#        print(f'You are bringing {items[0]}, {items[1]}, and ')
#        print(f'You are bringing {}, ')
        items[-1] = 'and ' + items[0]
        print('You are bringing {}.'.format(', ',join(items)))


# --------------------------------------------------
if __name__ == '__main__':
    main()
