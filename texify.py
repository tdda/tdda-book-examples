import os
import sys
import unicodedata as uc

QDD = uc.normalize('NFC', 'q̣̇')
DA = uc.lookup('DOT ABOVE')
DB = uc.lookup('ONE DOT LEADER')
VS = uc.lookup('OPEN BOX')
TAB = chr(9)

TRANS1 = str.maketrans({
    '{': r'\{',
    '}': r'\}',
    '✔': r'\cmark',
    '✘': r'\xmark',
    '✓': r'\cmark',
    '✗': r'\xmark',
    '∅': r'\nullmark',
})

TRANS2 = str.maketrans({
    "'": r'\textquotesingle{}',
    'é': r"\'e",
    DA: r'\highdot',
    DB: r'\lowdot',
    VS: r'\visiblespace',
    TAB: r'\visibletab{}',
    '∞': r'$\codeinfty$',
    '–': r'-',
})


def split(line, maxLen):
    out = []
    while len(line) > maxLen:
        out.append(line[:maxLen])
        line = line[maxLen:]
    out.append(line)
    return '\n'.join(out)


def texify(inpath, outpath=None, maxLen=None, repipe=None):
    maxLen = int(maxLen) if maxLen else 80
    base, ext = os.path.splitext(inpath)
    outpath = outpath or (base + '-tex' + ext)
    with open(inpath) as f:
        with open(outpath, 'w') as fw:
            lines = f.readlines()
            while lines and not lines[0].strip():
                lines = lines[1:]
            while lines and not lines[-1].strip():
                lines = lines[:-1]
            outlines = []
            for line in lines:
                outlines.append(split(line, maxLen))

            if repipe:  # Re-join consectutive commands without output with |
                i = 0
                while i < len(outlines) - 1:
                    L, M = outlines[i], outlines[i + 1]
                    if L.startswith('+') and M.startswith('+'):
                        outlines[i] = L.rstrip() + ' | ' + M[2:]
                        outlines = outlines[:i+1] + outlines[i+2:]
                    else:
                        i += 1

            for line in outlines:
                if line.startswith('$') or line.startswith('+'):
                    fw.write('\\pui{' + line[2:-1] + '}\n')
                else:
                    L = (uc.normalize('NFC', line)
                           .replace(r'\n', r"\eol{}")
                           .replace(QDD, r"\qBA")
                           .translate(TRANS1)
                           .replace(r'\u', r'\u{}')
                           .replace(r'\U', r'\U{}')
                           .replace(r'\t', r'\textbackslash{t}')
                           .translate(TRANS2)
                    )

                    if L.rstrip().endswith('\\'):
                        p = L.rfind('\\')
                        L = L[:p] + '\\textbackslash\n'
                    fw.write(L)
    print(f'Written {outpath}.')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        texify(*sys.argv[1:])
    else:
        print('USAGE: python texify.py input [oupath [LEN [R]]]')
        print('LEN is line length (default 80)')
        print('R is for repipe (join consecutive + line with pipes)')
