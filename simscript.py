import os
import sys

from tdda.utils import find_free_name
from tdda.referencetest.gentest import ExecuteCommand

from simcmd import simcmd, texify_and_report


'''USAGE: python simscript.py scipt.sh [[outpath] width]

Commands in the script will be run, combining stdout and stderr, writing
result to file with a simulated command line at the top
(usually with $).

The result will also be texified.

Outputs will be command.txt.tex and command.txt
if outpath is specified as 'command.txt'
'''

if __name__ == '__main__':
    if len(sys.argv) in (2, 3, 4):
        script = sys.argv[1]
        with open(script) as f:
            lines = [line.strip() for line in f.readlines()]
        outpath = f'{script}.txt' if len(sys.argv) == 2 else sys.argv[2]
        width = 70 if len(sys.argv) < 4 else int(sys.argv[3])
        if os.path.exists(outpath):
            os.unlink(outpath)
        for i, cmd in enumerate(lines):
            with open(outpath, 'a') as f:
                if cmd.startswith('#') or cmd.startswith('set -'):
                    f.write(cmd + '\n\n')
                elif i > 1 and cmd:
                    f.write('\n')
                    simcmd(cmd, outpath, width, mode='a')
        texify_and_report(outpath)
    else:
        print(USAGE, file=sys.stderr)
        sys.exit(1)
