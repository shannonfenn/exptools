#! /usr/bin/env python

import argparse
import lzma
import exptools.singlefile as sf


def main():
    parser = argparse.ArgumentParser(
        description='Check experiment (.json) files')

    parser.add_argument('inputfile', type=str)

    args = parser.parse_args()

    if args.inputfile.endswith('.xz'):
        with lzma.open(args.inputfile, 'rt') as f:
            sf.summary(f, True)
    else:
        with open(args.inputfile) as f:
            sf.summary(f, True)


if __name__ == '__main__':
    main()
