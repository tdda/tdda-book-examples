import json
import sys

def replify(inpath, outpath=None, deprint=True):
    """
    Very simple script for making simple python scripts
    """
    if outpath is None:
        outpath = 'repl_' + inpath
    buf = []
    cont = False
    with open(outpath, 'w') as f:
        for line in open(inpath):
            assert "'''" not in line and '"""' not in line
            if (
                line.strip().startswith('print(')
                and line.strip().endswith(')')
                and deprint
            ):
                n = line.find('print')
                pline = line[:n] + line[n + 6:].rstrip()[:-1]
            else:
                pline = line.rstrip()
            leader = '...' if cont else '>>>'
            if "''" not in pline:
                f.write(f"print('{leader}', '''{pline}''')\n")
            elif '""' not in pline:
                f.write(f'print("{leader}", """{pline}""")\n')
            else:
                raise Exception(f'Problem writing: {pline}')
            cont = pline.endswith(',')
            if cont:
                buf.append(line)
            else:
                if buf:
                    for b in buf:
                        f.write(b)
                    buf = []
                f.write(line)
        for b in buf:
            f.write(b)



if __name__ == '__main__':
    if len(sys.argv) in (2, 3):
        replify(*sys.argv[1:])
    else:
        print('USAGE: python replify.py script.py [outpath.py]')
