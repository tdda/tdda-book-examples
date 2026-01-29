import os
import sys


def wrap(path, N=None, sep=None, blank_between=True, show=True):

    N = 80 if N is None else int(N)
    sep = ',' if sep is None else sep
    with open(path) as f:
        lines = [line.rstrip() for line in f.readlines()]
    out = []
    while any(lines):
        n = find_common_split_field(lines, N, sep)
        for i, line in enumerate(lines):
            left, right = split_line_before(line, n, sep)
            out.append(left)
            lines[i] = right
        if any(lines) and blank_between:
            out.append('')
    result = '\n'.join(out)
    if show:
        print(result)
    return result


def split_line_before(line, nth, sep=','):
    i = 1
    p = line.find(sep, 0)
    while i < nth:
        if p == -1:
            break
        i += 1
        p = line.find(sep, p + 1)
    if p == -1:
        return line, ''
    else:
        return line[:p + 1], line[p+1:]


def find_common_split_field(lines, N=80, sep=','):
    return min(find_split_field(line, N, sep) for line in lines)


def find_split_field(line, N=80, sep=','):
    i = 0
    p = 0
    done = False
    while not done:
        pos = line.find(sep, p)
        if pos < N and pos != -1:
            p = pos + 1
            i += 1
        else:
            done = True
    if pos == -1 and len(line) < N:
        return i + 1
    else:
        return max(i, 1)  # Always allow 1, even if it blows the limit


if __name__ == '__main__':
    if not len(sys.argv) in (2, 3):
        print('USAGE: python wrap_all.py file [[max-len] sep\n',
              'Wraps a CSV or similar at the number of columns given\n'
              'with the same number of fields on each line',
              file=sys.stderr)
        sys.exit(1)
    wrap(*sys.argv[1:])

