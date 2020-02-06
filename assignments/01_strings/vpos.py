#!/usr/bin/env python3
"""
Author : edwin
Date   : 2020-02-05
Purpose: Homework1
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find position of vowel in string',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('vowel',
                        metavar='vowel',
                        help='A vowel to look for',
                        choices = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

    parser.add_argument('text',
                        metavar='text',
                        help='The text to search')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    vowel = args.vowel
    text = args.text
    index = text.find(vowel)

    if vowel in text:
        print(f'Found "{vowel}" in "{text}" at index {index}.')
    else:
        print(f'"{vowel}" is not found in "{text}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
