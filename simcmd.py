import os
import sys

from tdda.utils import find_free_name
from tdda.referencetest.gentest import ExecuteCommand
from texify import texify

'''USAGE: python simcmd 'command to simulate' [outpath]

Command will be run, combining stdout and stderr, writing
result to file with a simulated command line at the top
(usually with $).

The result will also be texified.

Outputs will be command.txt.tex and command.txt
if outpath is specified as 'command.txt'
'''

PROMPT = '$ '

def free_path(path, dir_):
    """
    Return a version of path that does not exist in dir_.
    """
    files = os.listdir(dir_)
    if path in files:
        n = 1
        stem, ext = os.path.splitext(path)
        candidate = f'{stem}_{n}{ext}'
        while candidate in files:
            n += 1
            candidate = f'{stem}_{n}{ext}'
        path = candidate
    return path


def simcmd(cmd, outpath=None):
    cwd = os.getcwd()
    if outpath is None:
        clean = ''.join((c if c.isalnum() else '_') for c in cmd)
        outpath = free_path(f'{clean}.txt', cwd)
    texpath = outpath + '.tex'
    command = cmd + f' 2>&1'
    command_line = PROMPT + cmd
    r = ExecuteCommand(command, cwd)
    end = '\n' if not r.out.endswith('\n') else ''
    with open(outpath, 'w') as f:
        f.write(f'{command_line}\n{r.out}{end}')
    print(f'Written {outpath}')
    texify(outpath, texpath, 70)


if __name__ == '__main__':
    if len(sys.argv) in (2, 3):
        simcmd(*sys.argv[1:])
    else:
        print(USAGE, file=sys.stderr)
        sys.exit(1)
