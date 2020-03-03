#!/usr/bin/env python3
"""
Author : edwin
Date   : 2020-02-18
Purpose: Rock the Casbah
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text or file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')

    args = parser.parse_args()

#if the args.text is a file name (checks using os.path.isfile)
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()
#then open args.text, read its name and strip the whitespace out

    return args
#then return the arguments

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout
    out_fh.write(args.text.upper() + '\n')
#    print(args.text.upper(), file = out_fh, end='') #the end will take away print's last line
    #print('OHNOES', file = sys.stderr)
    out_fh.close()

#technically dont have to close the file handle but it is good practice to do so

#print(args.text.upper()) use the variable in here in the write function instead


# --------------------------------------------------
if __name__ == '__main__':
    main()
