#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os.path as pth
from glob import glob
import exptools.singleexp as singleexp
import exptools.singlerun as singlerun


def get_last_dirs(directory):
    expdirs = glob(pth.join(directory, '*/'))
    lastdirs = []
    for expdir in expdirs:
        last_subdir = singleexp.get_last_run_dir(expdir)
        if last_subdir:
            lastdirs.append(last_subdir)
    return sorted(lastdirs)


def summarise_all(directories, swallow_errors):
    dir_width = max(len(dirname) for dirname in directories)

    for directory in directories:
        n_rem, n_succ, n_failed, n_err = singlerun.summary(
            directory, swallow_errors)
        print(f'{directory:<{dir_width}} '
              f'rem: {n_rem:>4} mem: {n_succ:>4} '
              f'not-mem: {n_failed:>4} json-err: {n_err:>4}')
