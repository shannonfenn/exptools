import rapidjson as json


def is_memorised(record):
    if record['learner'] == 'ecc_member':
        # this learner uses bagging so gets non zero trg error even when mem'd
        return sum(record['best_err']) == 0
    else:
        return record['trg_err'] == 0


def non_memorised(stream, fast=True):
    records = [json.loads(line)
               for line in stream
               if line.strip()]
    return [record['id']
            for record in records
            if not is_memorised(record)]


def summary(stream, swallow_errors):
    num_succeeded = num_failed = num_error = 0
    lines = [line
             for line in stream
             if line.strip()]
    for line in lines:
        try:
            record = json.loads(line)
        except (ValueError, TypeError) as err:
            if swallow_errors:
                num_error += 1
            else:
                raise err
        else:
            if is_memorised(record):
                num_succeeded += 1
            else:
                num_failed += 1
    return num_succeeded, num_failed, num_error
