#!/usr/bin/env python3
"""
Author : jporter8 <jporter8@localhost>
Date   : 2023-02-24
Purpose: Howler Project
"""

import argparse
import os
import io
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Create Howler',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        type=str,
                        help='Input a string or a file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output a file name',
                        metavar='str',
                        type=str,
                        default='')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text: open(args.text, encoding="utf8")
    else:
        args.text: io.StringIO(args.text + '\n')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    out_fh = open(args.outfile, 'wt',
                  encoding="utf8") if args.outfile else sys.stdout
    for line in args.text:
        out_fh.write(line.upper())
    out_fh.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()
