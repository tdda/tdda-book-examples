import math
import random
import numpy as np


N = 1024
RADIUS = 4
SPACING = 10
OFFSET = int(SPACING / 2) - RADIUS
BORDER = 20
INSET = int(BORDER / 2)


def experimentally_determine_luck(n):
    alive = list(range(n))
    pops = [alive]
    n_alive = len(alive)
    rounds = 0

    while n_alive > 1:
        survive = random.getrandbits(n_alive)
        new_alive = [k for i, k in enumerate(alive) if survive & (1 << i)]
        n_now_alive = len(new_alive)
        if n_now_alive > 0:
            alive = new_alive
            n_alive = n_now_alive
        pops.append(alive)
        rounds += 1
        print(n_alive, end=' ')
    print()
    return pops


def show_pops(pops):
    pop_rows = len(pops) // 4 + (1 if len(pops) % 4 > 0 else 0)

    n = len(pops[0])  # All alive in first pop
    n_cols = int(math.sqrt(n))
    n_rows = n // n_cols + (1 if n % n_cols else 0)
    pop_width = n_cols * SPACING + BORDER * 2
    pop_height = n_rows * SPACING + BORDER * 2
    (plot_width, plot_height) = (pop_width * 4, pop_height * pop_rows)
    out = ['<svg xmlns="http://www.w3.org/2000/svg" '
           'xmlns:xlink="http://www.w3.org/1999/xlink" '
           f'width="{plot_width}" height="{plot_height}" '
           f'viewBox="0 0 {plot_width} {plot_height}" '
           'preserveAspectRatio="xMinYMin meet">']
    for i, pop in enumerate(pops):
        pop_row = i // 4
        pop_col = i % 4
        xTL, yTL = (pop_col * pop_width + INSET, pop_row * pop_height+ INSET)
        xBR, yBR = (xTL + pop_width, yTL + pop_height)
        out.append(f'<rect x="{xTL}" y="{yTL}" '
                   f'width="{pop_width - BORDER}" '
                   f'height="{pop_height - BORDER}" '
                   f'style="fill:none;stroke:black"/>')
        for p in pop:
            row, col = p // n_cols, p % n_cols
            x = pop_col * pop_width  + BORDER + col * SPACING + RADIUS + OFFSET
            y = pop_row * pop_height + BORDER + row * SPACING + RADIUS + OFFSET
            out.append('<circle '
                       f'cx="{x}" cy="{y}" r="{RADIUS}" '
                       f'style="fill:black;stroke:black"/>')

    out.append('</svg>\n')
    with open('generations.svg', 'w') as f:
        f.write('\n'.join(out))
    print('Written generations.svg.')


if __name__ == '__main__':
    pops = experimentally_determine_luck(N)
    luckiest = pops[-1][0]
    n_rounds = len(pops) - 1
    print(f'Luckiest is {luckiest} ({n_rounds} elimination rounds)')
    show_pops(pops)

