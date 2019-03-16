import glob
from os.path import join, basename, splitext
from natsort import natsorted
import rapidjson as json
import pickle
import gzip
import exptools.singlefile as sf


def all_experiments(directory):
    bundles = glob.glob(join(directory, '*.explist'))
    all_exps = []
    for explist in bundles:
        with open(explist) as f:
            bunch = [line
                     for line in f.read().splitlines()
                     if line]
            all_exps.extend(bunch)
    return all_exps


def remaining_experiments(directory, fast=True):
    all_json = glob.glob(join(directory, '*.json'))

    finished_ids = []
    for jsonfile in all_json:
        with open(jsonfile) as f:
            records = [json.loads(line) for line in f if line.strip()]
        finished_ids.extend(record['id'] for record in records)

    explist = all_experiments(directory)
    expmap = dict()

    for exp in explist:
        if fast:
            eid = int(splitext(basename(exp))[0])
        else:
            with gzip.open(exp, 'rb') as f:
                eid = pickle.load(f)['id']
        expmap[eid] = exp
    if len(expmap) != len(explist):
        raise ValueError('.exp files with duplicate ids!')

    remaining = natsorted(exp_filename
                          for i, exp_filename in expmap.items()
                          if i not in finished_ids)
    return remaining


def non_memorised_experiments(directory, fast=True):
    all_json = glob.glob(join(directory, '*.json'))

    failed_ids = []
    for fname in all_json:
        with open(fname) as f:
            failed_ids.extend(sf.non_memorised(f))

    explist = all_experiments(directory)
    expmap = dict()

    for exp in explist:
        if fast:
            eid = int(splitext(basename(exp))[0])
        else:
            with gzip.open(exp, 'rb') as f:
                eid = pickle.load(f)['id']
        expmap[eid] = exp
    if len(expmap) != len(explist):
        raise ValueError('.exp files with duplicate ids!')

    failed_ids = natsorted(failed_ids)
    failed_paths = (expmap[i] for i in failed_ids)
    return failed_paths


def summary(directory, swallow_errors):
    all_json = glob.glob(join(directory, '*.json'))

    num_exp = len(all_experiments(directory))
    num_succeeded = num_failed = num_error = 0
    for fname in all_json:
        try:
            with open(fname) as f:
                s, f, e = sf.summary(f, swallow_errors)
        except OSError as err:
            if not swallow_errors:
                raise err
        num_succeeded += s
        num_failed += f
        num_error += e
    num_remaining = num_exp - num_succeeded - num_failed - num_error
    return num_remaining, num_succeeded, num_failed, num_error
