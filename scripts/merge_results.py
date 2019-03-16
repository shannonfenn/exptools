#! /usr/bin/env python

import argparse
import re
import glob
import natsort


def process(input_fnames):
    # build a mapping with 'id' keys
    # this allows later records with the
    # same id to override previous records
    id_map = {}
    for fname in input_fnames:
        with open(fname) as f:
            for line in f:
                match = re.search(pattern=r'id":\s?(\d+)(,|\})',
                                  string=line)
                key = match.group(1)
                id_map[key] = line

    for line in id_map.values():
        print(line, end='')  # lines already contain newlines


def main():
    parser = argparse.ArgumentParser(description='combine results')
    parser.add_argument('inputs', type=str, nargs='*',
                        help='[later will overwrite keys of earlier]')
    args = parser.parse_args()

    if args.inputs:
        input_fnames = args.inputs
    else:
        input_fnames = glob.glob('*.json')
        input_fnames = [fname
                        for fname in input_fnames
                        if re.fullmatch(r'\d+\.json', fname)]
        input_fnames = natsort.natsorted(input_fnames)
    process(input_fnames)


if __name__ == '__main__':
    main()
