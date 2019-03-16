#! /usr/bin/env python

import glob
import argparse
import os.path
from natsort import natsorted
import exptools.utils as utils
import exptools.singleexp as singleexp


def concatenate(partials, outstream):
    for fname in partials:
        with open(fname, 'r') as f:
            for line in f:
                line = line.strip()
                if any(line.startswith(c) for c in [',', '[', ']']):
                    line = line[1:]
                if line:
                    outstream.write(line)
                    outstream.write('\n')


def process(run_dir, fname=None, mode='x'):
    if not os.path.isdir(run_dir):
        raise ValueError('{} doesn\'t exist'.format(run_dir))
    partials = glob.glob(os.path.join(run_dir, '*.json'))
    partials = natsorted(partials)
    if not fname:
        fname = f'{os.path.normpath(run_dir)}.json'
    with open(fname, mode) as f:
        concatenate(partials, f)


def main():
    parser = argparse.ArgumentParser(description='joins <run>/*.json')
    parser.add_argument('dir', type=utils.directory_type)
    parser.add_argument('run', nargs='?', type=str)
    parser.add_argument('--outfile', '-o', type=str,
                        help=('output file, default: <dir>/<run>.json'))
    parser.add_argument('--force', '-f', action='store_true',
                        help='overwrite existing files.')
    args = parser.parse_args()

    if not args.run and args.outfile:
        print('Can\'t specify -o for multiple runs.')
        return

    if args.force:
        mode = 'w'
    else:
        mode = 'x'

    if args.run:
        run_dir = os.path.join(args.dir, args.run)
        process(run_dir, args.outfile, mode)
    else:
        for run_dir in singleexp.get_run_dirs(args.dir):
            process(run_dir, args.outfile, mode)


if __name__ == '__main__':
    main()
