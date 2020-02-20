#!/usr/bin/env python3
"""
Author : edwin
Date   : 2020-02-19
Purpose: homework3
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Days of the week',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('days',
                        metavar='str',
                        nargs='+',
                        help='What to do on each day')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    day = args.days
    week = {'Monday':'On Mondays I never go to work',
            'Tuesday':'On Tuesdays I stay at home',
            'Wednesday':'On Wednesdays I never feel inclined',
            'Thursday':"On Thursdays, it's a holiday",
            'Friday':'And Fridays I detest',
            'Saturday':"Oh, it's much too late on a Saturday",
            'Sunday':'And Sunday is the day of rest'}

    for i in day:
        if i in week:
            print(week.get(f'{i}'))
        else:
            print(f"Can't find"+f' "{i}"')




# --------------------------------------------------
if __name__ == '__main__':
    main()
