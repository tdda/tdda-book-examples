import os
import sys

from rich.console import Console
from rich.terminal_theme import MONOKAI, DEFAULT_TERMINAL_THEME


def two_col(inpath, col_len=None, gapsize=2):
    stem, ext = os.path.splitext(inpath)
    outpath = stem + '-2col' + ext
    svgpath = stem + '-2col' + '.svg'
    with open(inpath) as f:
        lines = f.readlines()

    n = len(lines)
    n2 = n // 2 + n % 2
    L = max(len(line) for line in lines)
    if col_len:
        n2 = col_len
    gap = ' ' * gapsize

    console = Console(record=True, width=80)

    with open(outpath, 'w') as f:
        for i in range(n2):
            outline = (
                pad(lines[i].rstrip('\n\r'), L)
                    + gap
                    + (lines[i + n2] if i + n2 < n else '\n')
            )
            f.write(outline)
            outline = ''.join(m(c) for c in outline)
            console.print(outline, end='', highlight=False)
    console.save_svg(svgpath, theme=DEFAULT_TERMINAL_THEME)


def m(c):
    if ord(c) >= 0x80 and ord(c) <= 0xA0:
        return ' '
    return c


def pad(s, L):
    return s + ' ' * max(L - len(s), 0)


if __name__ == '__main__':
    two_col(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else None)

