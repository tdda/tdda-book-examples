# Check two json files after pretty printing and possible exclusions
# are the same.

import json
import os
import sys

USAGE = '''python json-diff-except.py f1.json f2.json [strings] [--no-clobber]

where

  [strings] is an optional list of strings that cause lines to be ignored.

Prints nothing and exits with code 0 if JSON is the same after
pretty printing and excluding lines containing specified strings.

Writes temporary normalized versions to /tmp and suggests diff command
if they are different, then exits with code 1.

Use -n or --no-clobber to prevent overwriting files in /tmp.
'''


def main(path1, path2, *exclusions, noclobber=False):
    with open(path1) as f:
        c1 = json.load(f)
    with open(path2) as f:
        c2 = json.load(f)
    lines1 = exclude(json.dumps(c1, indent=4).splitlines(), exclusions)
    lines2 = exclude(json.dumps(c2, indent=4).splitlines(), exclusions)
    if lines1 != lines2:
        p1 = write_tmp(lines1, path1, noclobber=noclobber)
        p2 = write_tmp(lines2, path2, noclobber=noclobber)
        print('JSON differs after exclusion and normalization.')
        print(f'diff {p1} {p2}')
        sys.exit(1)


def write_tmp(lines, path, outdir='/tmp', noclobber=False):
    if noclobber:
        outpath = free_path(outdir, os.path.basename(path))
    else:
        outpath = os.path.join(outdir, os.path.basename(path))
    with open(outpath, 'w') as f:
        f.write('\n'.join(lines))
    return outpath


def free_path(dir_, name):
    disamb = ''
    name, ext = os.path.splitext(name)
    path = os.path.join(dir_, f'{name}{disamb}{ext}')
    while os.path.exists(path):
        disamb = int(disamb) + 1 if disamb else 1
        path = os.path.join(dir_, f'{name}{disamb}{ext}')
    return path


def exclude(lines, exclusions):
    for exc in exclusions:
        lines = [line for line in lines if exc not in line]
    return lines


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(USAGE)
        sys.exit(1)
    else:
        args = [a for a in sys.argv[1:] if not a in ('-n', '--no-clobber')]
        noclobber = '-n' in sys.argv or '--no-clobber' in sys.argv
        main(*args, noclobber=noclobber)
