import os
import sys

from tdda.utils import find_free_name
from tdda.referencetest.gentest import ExecuteCommand
from texify import texify

'''USAGE: python simcmd 'command to simulate' [[outpath] width]
   or: python simcmd ./f [[outpath] width] to read the command from file f

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


def simcmd(cmd, outpath=None, width=70, mode='w'):
    cwd = os.getcwd()
    if outpath is None:
        clean = ''.join((c if c.isalnum() else '_') for c in cmd)
        outpath = free_path(f'{clean}.txt', cwd)
    command = cmd + f' 2>&1'
    command_line = PROMPT + cmd
    r = ExecuteCommand(command, cwd)
    end = '\n' if not r.out.endswith('\n') else ''
    with open(outpath, mode) as f:
        f.write(f'{command_line}\n{r.out}{end}')
    return outpath


def texify_and_report(outpath):
    texpath = outpath + '.tex'
    print(f'Written {outpath}.')
    if os.path.exists(texpath):
        os.unlink(texpath)
    texify(outpath, texpath, 80)


if __name__ == '__main__':
    if len(sys.argv) in (2, 3, 4):
        cmd = sys.argv[1]
        if cmd.startswith('./'):
            path = cmd[2:]
            with open(path) as f:
                cmd = f.read().strip()
        outpath = None if len(sys.argv) == 2 else sys.argv[2]
        width = 70 if len(sys.argv) < 4 else int(sys.argv[3])
        outpath = simcmd(cmd, outpath, width)
        texify_and_report(outpath)
    else:
        print(USAGE, file=sys.stderr)
        sys.exit(1)
