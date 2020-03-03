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

    # parser.add_argument('file',
    #                     metavar='FILE',
    #                     nargs='*',
    #                     default=[sys.stdin],
    #                     type=argparse.FileType('r'),
    #                     help='Input file(s)')

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
    fh = args.FILE

    # num = int(args.number)
    #
    # if num:
    #     print(f'"{num}"')
    num_lines = 0

#     if int(args.number) == 0:
#         sys.stderr.write(f'--num "{args.number}" must be greater than 0 \n')
#         sys.exit(2)
# #        sys.exit(f'{args.FILE}-n "{args.number}" must be greater than 0')
# #        print(f'--num "{args.number}" must be greater than 0')
#     elif int(args.number) < 0:
#         print(f'--num "{args.number}" must be greater than 0....')
#     else:
#         for line in args.FILE:
#             print(line)

    for line in args.FILE:
        num_lines += 1
        if num_lines <= args.number:
            print(line.strip())
        # else:
        #     sys.exit(0)




   # num_lines = args.number

    # if args.number:
    #  #   sys.stderr.write(f'--num "{args.number}" must be greater than 0')
    #     print(f'--num "{args.number}" must be greater than 0')
    #  #   sys.stderr(f'--num "{args.number}" must be greater than 0')
    # else:
    #     print('try again')

    # for line in args.FILE:
    #     if num == 0:
    #         print(sys.stderr(f'--num "{args.number}" must be greater than 0'))
    #     else:
    #         print(line)


    # print(fh)
    #
    # if args.number == 0:
    #     var = sys.stderr(f'--num "{args.number}" must be greater than 0')
    # else:
    #     print(args.number)


# --------------------------------------------------
if __name__ == '__main__':
    main()
