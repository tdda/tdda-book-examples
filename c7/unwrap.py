import json
import sys

def unwrap(inpath, outpath):
    r"""
    Removes and \veol entries from inpath, )which should be JSON),
    joining such lines back together and dumps the JSON with indent 2
    to outpath (thus normalizing).
    """
    with open(inpath) as f:
        inlines = f.readlines()
    outlines = []
    i = 0
    while i < len(inlines):
        line = inlines[i]
        if line.rstrip().endswith(r'\veol'):
            line = line.rstrip()[:-5] + inlines[i + 1].lstrip()
            i += 1
        outlines.append(line)
        i += 1
    o = json.loads(''.join(outlines))
    with open(outpath, 'w') as f:
        json.dump(o, f, indent=2)


if __name__ == '__main__':
    if len(sys.argv) == 3:
        unwrap(sys.argv[1], sys.argv[2])
    else:
        print('USAGE: python unwrap.py in.json out.json')
