#! /usr/bin/env python

import argparse
import exptools.utils as utils
import exptools.singlerun as singlerun


def __remaining(args):
    return '\n'.join(singlerun.remaining_experiments(args.dir))


def __non_memorised(args):
    return '\n'.join(singlerun.non_memorised_experiments(args.dir))


def __summary(args):
    n_rem, n_suc, n_fail, n_err = singlerun.summary(args.dir, args.verbose)
    return (f'rem: {n_rem} mem: {n_suc} not-mem: {n_fail} json-err: {n_err}')


def main():
    parser = argparse.ArgumentParser(
        description='Tools for filtering experiment (.exp/.json) files')

    subparsers = parser.add_subparsers(help='commands', dest='command')

    parser_remaining = subparsers.add_parser('rem')
    parser_remaining.add_argument('dir', type=utils.directory_type)
    parser_remaining.set_defaults(func=__remaining)

    parser_failed = subparsers.add_parser('not')
    parser_failed.add_argument('dir', type=utils.directory_type)
    parser_failed.set_defaults(func=__non_memorised)

    parser_summary = subparsers.add_parser('sum')
    parser_summary.add_argument('dir', type=utils.directory_type)
    parser_summary.add_argument('--verbose', '-v', action='store_true',
                                help='verbose json errors.')
    parser_summary.set_defaults(func=__summary)

    args = parser.parse_args()

    print(args.func(args))


if __name__ == '__main__':
    main()
