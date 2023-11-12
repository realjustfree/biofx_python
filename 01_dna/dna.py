#!/usr/bin/env python3
"""
Author : lhs <lhs@localhost>
Date   : 2023-11-12
Purpose: Tetranucleotide frequency
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Tetranucleotide frequency',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('dna',
                        metavar='DNA',
                        help='Input DNA sequence')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    print(args.dna)


# --------------------------------------------------
if __name__ == '__main__':
    main()
