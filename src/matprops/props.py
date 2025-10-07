import matplotlib
import matplotlib.pyplot as plt

import math

import numpy as np
from matplotlib.patches import Rectangle

from matprops.config import ColorConfig
from matprops.data import DataConstruct

def AreaProp(
        data,
        col=None,
        title=None,
        labels=True,
        cols=3,
        color="blue"
):
    prop_data = DataConstruct(data, col=col, title=title, ptype="area")

    max_rows = math.ceil(prop_data.dlen / cols) if prop_data.dlen > cols else 1 # Todo
    fig, axs = plt.subplots(max_rows, 3)  # Todo

    # Plot data
    for ax, data in zip(axs.flat, prop_data):
        title, value = data
        ax.add_patch(plt.Rectangle((0, 0), 1, 1, color="#707070", alpha=0.1))
        ax.add_patch(plt.Rectangle((0, 0), value, value, facecolor=matplotlib.colors.to_hex(color) + "4D", edgecolor=color))
        ax.text(0, 1.1, title, ha="left", va="center", color="black", fontsize=10, fontweight="bold")

        if labels:
            ax.text(value / 2, value / 2, f"{int(value * 100)}%", ha="center", va="center", color=color, fontsize=8)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('equal')
        ax.axis("off")

    # Hide unused axes
    for ax in axs.flat[prop_data.dlen:]:
        ax.set_visible(False)

    return fig


def SplitProp(
        data,
        col=None,
        title=None,
        labels=True,
        cols=3,
        cmap=None
):
    prop_data = DataConstruct(data, col=col, title=title, ptype="split")

    max_rows = math.ceil(prop_data.dlen / cols) if prop_data.dlen > cols else 1  # Todo
    fig, axs = plt.subplots(max_rows, 3)  # Todo

    cmap = ColorConfig(cmap, n=prop_data.ndim)

    # Plot data
    for ax, data in zip(axs.flat, prop_data):
        title, value = data
        position = 0

        if sum(value) > 1:
            raise ValueError("The sum of the values must not exceed 1.0 for SplitProp.")

        for patch, color in zip(value, cmap):
            ax.add_patch(plt.Rectangle((position, 0), patch, 1, facecolor=matplotlib.colors.to_hex(color) + "4D", edgecolor=color))

            if labels:
                ax.text(position + patch / 2, 0.5, f"{int(patch * 100)}%", ha="center", va="center", color=color, fontsize=8)

            position += patch

        ax.add_patch(plt.Rectangle((0, 0), 1, 1, color="#707070", alpha=0.1))
        ax.text(0, 1.1, title, ha="left", va="center", color="black", fontsize=10, fontweight="bold")
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('equal')
        ax.axis("off")

    # Hide unused axes
    for ax in axs.flat[prop_data.dlen:]:
        ax.set_visible(False)

    return fig


def StackProp(
        data,
        col=None,
        title=None,
        labels=True,
        cols=3,
        cmap=None
):
    prop_data = DataConstruct(data, col=col, title=title, ptype="stack")

    max_rows = math.ceil(prop_data.dlen / cols) if prop_data.dlen > cols else 1  # Todo
    fig, axs = plt.subplots(max_rows, 3)  # Todo

    cmap = ColorConfig(cmap, n=prop_data.ndim)

    # Plot data
    for ax, data in zip(axs.flat, prop_data):
        title, value = data

        for patch, color in zip(value, cmap):
            ax.add_patch(plt.Rectangle((0, 0), patch, patch, facecolor=matplotlib.colors.to_hex(color) + "4D", edgecolor=color))

            if labels:
                ax.text(patch-0.08, patch, f"{int(patch * 100)}%", ha="left", va="bottom", color=color, fontsize=8)

        ax.add_patch(plt.Rectangle((0, 0), 1, 1, color="#707070", alpha=0.1))
        ax.text(0, 1.1, title, ha="left", va="center", color="black", fontsize=10, fontweight="bold")
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('equal')
        ax.axis("off")

    # Hide unused axes
    for ax in axs.flat[prop_data.dlen:]:
        ax.set_visible(False)

    return fig


def BiProp(
        data,
        col=None,
        title=None,
        labels=True,
        cols=3,
        cmap=None,
        orientation='horizontal'
):
    padding = 0.05
    prop_data = DataConstruct(data, col=col, title=title, ptype="bi")
    total_items = len(prop_data)
    rows = math.ceil(total_items / cols)

    fig, axs = plt.subplots(rows, cols, figsize=(4 * cols, 2 * rows))
    # Ensure axs is always 2D for consistent indexing
    if rows == 1 and cols == 1:
        axs = np.array([[axs]])
    elif rows == 1:
        axs = np.array([axs])
    elif cols == 1:
        axs = np.array([[ax] for ax in axs])
    axs_flat = axs.flatten()
    cmap_obj = ColorConfig(cmap=cmap, n=2)
    color1, color2 = cmap_obj.colors

    for ax, (_, values) in zip(axs_flat, prop_data):
        patch1, patch2 = values

        mx = float("-inf")

        if orientation == 'horizontal':
            ax.add_patch(Rectangle((0, 0), patch1, patch1, facecolor=matplotlib.colors.to_hex(color1) + "4D", edgecolor=matplotlib.colors.to_hex(color1)))
            ax.add_patch(Rectangle((patch1 + padding, 0), patch2, patch2, facecolor=matplotlib.colors.to_hex(color2) + "4D", edgecolor=matplotlib.colors.to_hex(color2)))
            if labels:
                ax.text(patch1 / 2, patch1 / 2, f"{int(patch1 * 100)}%", ha="center", va="center", color=color1, fontsize=8)
                ax.text(patch1 + padding + (patch2 / 2), patch2 / 2, f"{int(patch2 * 100)}%", ha="center", va="center", color=color2, fontsize=8)

            mx = max(mx, max(patch1 + padding, patch2 + padding))

            ax.set_aspect('auto')
            plt.xlim(0, max(1, patch1 + patch2 + padding))
            ax.set_ylim(0, 1.2)

        else:
            ax.add_patch(Rectangle((0, 0), patch2, patch2, facecolor=matplotlib.colors.to_hex(color2) + "4D", edgecolor=matplotlib.colors.to_hex(color2)))
            ax.add_patch(Rectangle((0, patch2 + padding), patch1, patch1, facecolor=matplotlib.colors.to_hex(color1) + "4D", edgecolor=matplotlib.colors.to_hex(color1)))
            if labels:
                ax.text(patch2 / 2, patch2 / 2, f"{int(patch2 * 100)}%", ha="center", va="center", color=color2, fontsize=8)
                ax.text(patch1 / 2, patch2 + padding + patch1 / 2, f"{int(patch1 * 100)}%", ha="center", va="center", color=color1, fontsize=8)

            mx = max(mx, max(patch1 + padding, patch2 + padding))

            # ax.set_aspect('auto')
            ax.set_xlim(xmin=0.1, xmax=1.3)
            ax.set_xbound(lower=0.0, upper=1)
            ax.set_ylim(0, max(1, patch1 + patch2 + padding))

    for ax, (title, values) in zip(axs_flat, prop_data):
        if orientation == 'horizontal':
            ax.text(0, mx, str(title), ha="left", va="center", color="black", fontsize=10, fontweight="bold")
        elif orientation=="vertical":
            ax.text(mx, 1, str(title), ha="left", va="center", color="black", fontsize=10, fontweight="bold")
        ax.axis('equal')
        # ax.set_adjustable('box')

        ax.axis("off")

    # Hide unused axes
    for ax in axs_flat[len(prop_data):]:
        ax.set_visible(False)
        ax.axis("off")

    return fig