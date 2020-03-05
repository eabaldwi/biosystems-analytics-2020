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

    if args.min:
        smallest = args.min


    for line in args.file:
        word1, word2 = line.split()
        distance = abs(len(word1) - len(word2))

#        print(distance)

    # if len(word1) == len(word2):
    #     paired = list(zip(word1, word2))
    #     for i in paired:
    #         if paired[i][0] == paired[i][1]:
    #             print(f'{distance}:{word1}       {word2}')
    #         else:
    #             print('try again')
    # else:
    #     print('try again 2')


#end of class extras
#    for x in zip(word1, word2):
#        print(f'{distance}}') #gives a list of tuples
    count = 0

    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            count +=1
            tot = distance + count
 #       print(f'{distance}:{word1}    {word2}'.order(distance))
 #       print(c1, c2, c1 == c2) #prints the characters, then checks if their distance is the same
            print(f'{tot:8}:{word1:20}{word2}')

        # if distance == 0:
        #     print(f'{distance}:{word1}    {word2}')
        # elif distance == 2:
        #     print(f'{distance}:{word1}  2  {word2}')
        # else:
        #     print(f'{distance}:{word1}  3  {word2}')


#zip() takes two lists and pairs the index of each, if there are different lengths its just the number of the shortest

# --------------------------------------------------
if __name__ == '__main__':
    main()
