#!/usr/bin/env python3
"""
Author : edwin
Date   : 2020-01-30
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='str',
                        help='A word')

    return parser.parse_args()
#gives us additional documentation, and helps with whether or not we received exactly what we want from the user

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    article = ""
    if word[0] in 'aeiouAEIOU':
        article = "an"
    else:
        article = "a"

    #article = 'an' if word[0] = in 'aeiouAEIOU' else 'a'
    #article = 'an' if word[0].lower() = in 'aeiou' else 'a'
    print(f'Ahoy, Captain, {article} {word} off the larboard bow')



# --------------------------------------------------
if __name__ == '__main__':
    main()
