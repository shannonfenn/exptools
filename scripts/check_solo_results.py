#! /usr/bin/env python

import argparse
import lzma
import exptools.singlefile as sf


def main():
    parser = argparse.ArgumentParser(
        description='Check experiment (.json) file')
    parser.add_argument('inputfile', type=str)
    parser.add_argument('--verbose', '-v', action='store_true',
                        help='verbose json errors.')

    args = parser.parse_args()

    if args.inputfile.endswith('.xz'):
        with lzma.open(args.inputfile, 'rt') as f:
            n_succ, n_fail, n_err = sf.summary(f, not args.verbose)
    else:
        with open(args.inputfile) as f:
            n_succ, n_fail, n_err = sf.summary(f, not args.verbose)

    print(f'mem: {n_succ} not-mem: {n_fail} json-err: {n_err}')


if __name__ == '__main__':
    main()
