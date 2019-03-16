#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import exptools.utils as utils
import exptools.multiexp as multiexp


def main():
    parser = argparse.ArgumentParser(description='summarise latest results')
    parser.add_argument('dir', type=utils.directory_type)
    parser.add_argument('--verbose', '-v', action='store_true',
                        help='verbose warnings.')

    # Process arguments
    args = parser.parse_args()

    lastdirs = multiexp.get_last_dirs(args.dir)

    if lastdirs:
        multiexp.summarise_all(lastdirs, args.verbose)


if __name__ == '__main__':
    main()
