#!/usr/bin/env python3
# encoding: utf-8
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--backend")
parser.add_argument("--dpi", type=int)
args = parser.parse_args()

import matplotlib as mpl
mpl.use(args.backend)
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    fig, (_, ax) = plt.subplots(1, 2, figsize=(1.6, 1.0))

    scale = 0.8
    offset_x, offset_y, offset_1Mx, offset_1My = list(
        np.array([3, 2, 1, 0]) * scale
    )

    arrowprops = {}
    shift = 0.045

    ax_limLX, ax_limHX = -0.03, 1.2
    ax_limLY, ax_limHY = -0.5, 3.0
    ax.set_xlim(ax_limLX, ax_limHX)
    ax.set_ylim(ax_limLY, ax_limHY)
   
    def calc(x, y):
        return ((x - ax_limLX) / (ax_limHX - ax_limLX), (y - ax_limLY) / (ax_limHY - ax_limLY))

    ax.annotate('', xy=calc(0 - shift, offset_x), xycoords='axes fraction',
                xytext=calc(1 + shift, offset_x),
                arrowprops=arrowprops,
                )
    ax.annotate('', xy=(0 - shift, offset_y), xycoords='data',
                xytext=(2 + shift, offset_y),
                arrowprops=arrowprops,
                )

    fn = f'test_{args.backend}_{args.dpi}.pdf'

    print(f"used backend {mpl.get_backend()} and dpi {args.dpi}, saving as {fn}")

    fig.savefig(fn, dpi=args.dpi)
