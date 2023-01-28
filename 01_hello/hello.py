#!/usr/bin/env python3
"""
Author : jporter8 <jporter8@localhost>
Date   : 2023-01-26
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--name',
                        help='Name to greet',
                        metavar='name',
                        type=str,
                        default='World')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Print the written name"""

    args = get_args()
    person = args.name
    print(f'Hello, {person}!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
