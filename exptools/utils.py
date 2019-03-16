from os.path import abspath, expanduser, isdir


def directory_type(directory):
    # Handle tilde
    directory = abspath(expanduser(directory))
    if isdir(directory):
        return directory
    else:
        raise Exception('{0} is not a valid path'.format(directory))


def strided(l, n):
    sublists = [[] for i in range(n)]
    for i, item in enumerate(l):
        sublists[i % n].append(item)
    return sublists
