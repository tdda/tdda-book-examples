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

def texify(inpath, outpath=None, maxLen=80):
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
                if len(line) > maxLen:
                    outlines.append(line[:maxLen] + '\n')
                    outlines.append(line[maxLen:])
                else:
                    outlines.append(line)
            for line in outlines:
                if line.startswith('$'):
                    fw.write('\\pui{' + line[2:-1] + '}\n')
                else:
                    L = (uc.normalize('NFC', line)
                           .replace(r'\n', r"\eol")
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
    texify(*sys.argv[1:])

