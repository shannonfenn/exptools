#! /usr/bin/env python

import argparse
import glob
import itertools
import sys
import os
from os.path import isdir, expanduser, abspath, join
from natsort import natsorted
import exptools.utils as utils


def bundle(dir, num=None, experiments=None):
    if experiments is None:
        experiments = natsorted(glob.glob('{}/tasks/*.exp'.format(dir)))

    if experiments:
        num = min(num, len(experiments))
        return utils.strided(experiments, num)
    if not experiments:
        return None


def dump_new_bundle(dir, num=None, experiments=None):
    bundles = utils.strided(dir, num, experiments)

    if not bundles:
        print("No experiments found.")
        sys.exit(1)
    # find first non-existant */run_<int>/
    dir_generator = (join(dir, str(i))
                     for i in itertools.count())
    run_dir = next(directory
                   for directory in dir_generator
                   if not isdir(directory))
    os.makedirs(run_dir)

    for i, bundle in enumerate(bundles):
        fname = join(run_dir, '{}.explist'.format(i))
        with open(fname, 'w') as f:
            f.write('\n'.join(bundle))
            f.write('\n')

    print('{} bundles created.'.format(len(bundles)))


def main():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('dir', type=utils.directory_type)
    parser.add_argument('--num', '-n', type=int, default=7500)
    parser.add_argument('--infile', '-i', type=argparse.FileType(),
                        help='list of experiments (.exp) to run')

    args = parser.parse_args()

    if not (1 <= args.num <= 7500):
        parser.error('--num must be in [1..7500].')

    if args.infile:
        experiments = [line.strip()
                       for line in args.infile
                       if line.strip()]
        args.infile.close()
    else:
        experiments = None
    bundle(args.dir, args.num, experiments)


if __name__ == '__main__':
    main()
