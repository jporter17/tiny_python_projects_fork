#!/usr/bin/env python3
"""
Author : jporter8 <jporter8@localhost>
Date   : 2023-02-10
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('item',
                        metavar='str',
                        nargs='+',
                        help='Things to bring')

    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.item
    num = len(items)

    if args.sorted:
        items.sort()

    bringing = ''
    if num == 1:
        bringing = items[0]
    elif num == 2:
        bringing = ' and '.join(items)
    else:
        items[-1] = 'and ' + items[-1]
        bringing = ', '.join(items)

    print(f'You are bringing {bringing}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
