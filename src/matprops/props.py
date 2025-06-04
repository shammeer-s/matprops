import matplotlib
import matplotlib.pyplot as plt

import math
import pandas as pd

from matprops.data import construct

def prop(ax, value, title, color):
    ax.add_patch(plt.Rectangle((0, 0), 1, 1, color="#707070", alpha=0.1))
    ax.add_patch(plt.Rectangle((0, 0), value, value, facecolor=matplotlib.colors.to_hex(color) + "4D", edgecolor=color))
    ax.text(0, 1.1, title, ha="left", va="center", color="black", fontsize=10, fontweight="bold")
    ax.text(value/2, value/2, f"{int(value*100)}%", ha="center", va="center", color=color, fontsize=8)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('equal')
    ax.axis("off")
    return ax

def AreaProp(
        data,
        col=None,
        title=None,
        labels=True,
        cols=3,
        color="blue"
):
    prop_data = construct(data, col=col, title=title)

    max_rows = math.ceil(prop_data.dlen / cols) if prop_data.dlen > cols else 1 # Todo
    fig, axs = plt.subplots(max_rows, 3)  # Todo

    # Plot data
    for ax, data in zip(axs.flat, prop_data):
        title, value = data
        ax = prop(ax, value, title, color)

    # Hide unused axes
    for ax in axs.flat[prop_data.dlen:]:
        ax.set_visible(False)

    return fig
