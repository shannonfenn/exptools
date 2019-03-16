#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os.path as pth
from glob import glob
import re
import natsort
import subprocess as sp


def get_last_dirs(directory):
    expdirs = glob(pth.join(directory, '*/'))
    lastdirs = []

    for expdir in expdirs:
        subdirs = glob(pth.join(expdir, '*/'))
        subdirs = [pth.basename(pth.normpath(d))
                   for d in subdirs]
        subdirs = [d
                   for d in subdirs
                   if re.fullmatch(r'\d+', d)]
        if subdirs:
            lastdir = natsort.natsorted(subdirs)[-1]
            lastdirs.append(pth.join(expdir, lastdir))
    return sorted(lastdirs)


def summarise_all(lastdirs, verbose):
    dir_width = max(len(dirname) for dirname in lastdirs)

    for name, directory in lastdirs:
        if verbose:
            cmd = ['check_run.py', 'sum', '-v', directory]
        else:
            cmd = ['check_run.py', 'sum', directory]
        procout = sp.run(cmd, stdout=sp.PIPE, universal_newlines=True)
        print('{0:<{width}} {1}'.format(name, procout.stdout.strip(),
                                        width=dir_width))
        # print(f'{name}:\t{procout.stdout.strip()}')
