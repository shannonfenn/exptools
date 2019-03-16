import sys
import rapidjson as json


def is_memorised(record):
    if record['learner'] == 'ecc_member':
        # this learner uses bagging so gets non zero trg error even when mem'd
        return sum(record['best_err']) == 0
    else:
        return record['trg_err'] == 0


def non_memorised(fname, fast=True):
    with open(fname, 'r') as f:
        records = [json.loads(line) for line in f if line.strip()]
    return [record['id']
            for record in records
            if not is_memorised(record)]


def summary(fname, verbose):
    num_succeeded = num_failed = num_error = 0
    try:
        with open(fname, 'r') as stream:
            lines = [line for line in stream if line.strip()]
    except OSError as e:
        if verbose:
            print(f'Warning: could not read {fname}\n{e}',
                  file=sys.stderr)

    for line in lines:
        try:
            record = json.loads(line)
        except (ValueError, TypeError) as e:
            if verbose:
                print(f'Warning: bad json line {fname}\n{e}',
                      file=sys.stderr)
            num_error += 1
        else:
            if is_memorised(record):
                num_succeeded += 1
            else:
                num_failed += 1
    return num_succeeded, num_failed, num_error
