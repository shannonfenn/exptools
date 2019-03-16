from os.path import expanduser, isdir


def directory_type(directory):
    # Handle tilde
    directory = expanduser(directory)
    if isdir(directory):
        return directory
    else:
        raise Exception('{0} is not a valid path'.format(directory))


def strided(l, n):
    sublists = [[] for i in range(n)]
    for i, item in enumerate(l):
        sublists[i % n].append(item)
    return sublists
