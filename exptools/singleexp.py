import os.path as pth
from glob import glob
import re
import natsort


def get_run_dirs(expdir):
    subdirs = glob(pth.join(expdir, '*/'))
    subdirs = [pth.basename(pth.normpath(d))
               for d in subdirs]
    subdirs = [d
               for d in subdirs
               if re.fullmatch(r'\d+', d)]
    subdirs = natsort.natsorted(subdirs)
    subdirs = [pth.join(expdir, d)
               for d in subdirs]
    return subdirs


def get_last_run_dir(expdir):
    subdirs = get_run_dirs(expdir)
    if subdirs:
        return subdirs[-1]
    else:
        return None
