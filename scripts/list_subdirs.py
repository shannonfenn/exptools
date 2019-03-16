#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import exptools.utils as utils
import exptools.singleexp as singleexp


def main():
    parser = argparse.ArgumentParser(description='list integer subdirectories')
    parser.add_argument('dir', type=utils.directory_type)
    parser.add_argument('--last', '-l', action='store_true',
                        help='only print final subdir.')

    # Process arguments
    args = parser.parse_args()

    if args.last:
        subdirs = singleexp.get_last_dirs(args.dir)
    else:
        subdirs = singleexp.get_run_dirs(args.dir)

    if subdirs:
        print(subdirs)


if __name__ == '__main__':
    main()
