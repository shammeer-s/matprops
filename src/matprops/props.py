import matplotlib
import matplotlib.pyplot as plt

import math
import warnings

from matprops.utils import *
from matprops import config


def AreaProp(dataset, col_name, cols=8, labels=True, label_loc="inc", title=None,
             title_loc="tl", bgcolor="#707070",
             description=None,
             labelcolor="white"):

    fig = plt.figure()
    max_rows = math.ceil(len(dataset) / cols) if len(dataset) > cols else 1
    if dataset is not None and cols is not None:
        fig = plt.figure(figsize=(18, 2 * max_rows))

    if isinstance(col_name, str):
        col_name = [col_name]

    if fig:
        pConfig = config.PropConfig(dataset, title, title_loc, labels, label_loc, col_name,
                             description)

        for index, row in dataset.iterrows():
            ax = fig.add_subplot(max_rows, cols, index + 1)

            ax.axvspan(0, 1, ymax=1, fc=bgcolor, alpha=0.1)

            if pConfig.title is not None:
                # Use transform=ax.transAxes for coordinates relative to the Axes (0,0 to 1,1)
                # and va="bottom" for consistent alignment for top titles, "top" for bottom titles.
                # Title layout calculation now determines the y-coordinate directly.
                ax.text(pConfig.title_layout[0],
                        pConfig.title_layout[1],
                        row[title],
                        fontweight="bold",
                        ha=pConfig.title_layout[2],
                        va="bottom" if pConfig.title_loc in ["tl", "tr"] else "top",
                        c="#000", transform=ax.transAxes)

            if pConfig.description is not None:
                max_char_per_row = 15
                out_desc_list = [(row[description][i:i + max_char_per_row]) for i in
                                 range(0, len(row[description]), max_char_per_row)]

                # Start rendering description from the calculated layout position
                desc_x, desc_y, desc_ha = pConfig.description_layout

                # Adjust starting y for multiple lines, making sure it stacks downwards.
                # If title is at top, description starts below it.
                if pConfig.title is not None and pConfig.title_loc in ["tl", "tr"]:
                    current_y = pConfig.title_layout[
                                    1] - 0.06  # Start just below the title
                else:
                    current_y = desc_y  # Use the calculated base description y

                for i, line in enumerate(out_desc_list):
                    ax.text(desc_x,
                            current_y,
                            line,
                            fontweight="normal",
                            ha=desc_ha,
                            va="top",  # Stack lines downwards from the current_y
                            c="#000", transform=ax.transAxes)
                    current_y -= 0.05  # Line spacing, empirical value

            if isinstance(col_name, list):
                if len(col_name) > 3:
                    warnings.warn(
                        "Warning: Using more than three columns for proportional charts is not recommended "
                        "due to potential overcrowding. To ensure clarity and readability, we will only "
                        "display three columns. If you require specific columns, please update the "
                        "'col_name' attribute with three specific column names.")
                    display_cols = col_name[:3]
                else:
                    display_cols = col_name

                # Assign distinct colors dynamically, similar to previous version.
                prop_colors = ["blue", "green", "red"]

                for i, col in enumerate(display_cols):
                    current_color = prop_colors[
                        i % len(prop_colors)]  # Cycle through colors

                    # Ensure proportion values are between 0 and 1
                    prop_value = row[col]
                    if not (0 <= prop_value <= 1):
                        warnings.warn(
                            f"Value for column '{col}' at index {index} is {prop_value}. "
                            "Proportions should be between 0 and 1. Clamping for visualization.")
                        prop_value = max(0.0,
                                         min(1.0, prop_value))  # Clamp to valid range

                    ax.axvspan(0, prop_value, ymin=0.01, ymax=prop_value,
                               fc=matplotlib.colors.to_hex(current_color) + "4D",
                               ec=current_color)

                    if pConfig.labels:
                        label_layout = pConfig.get_label_layout(row, col)
                        if label_layout:
                            ax.text(label_layout[0],
                                    label_layout[1],
                                    f"{prop_value * 100:.1f}%",
                                    # Format to one decimal place
                                    c=matplotlib.colors.to_hex(current_color),
                                    # Use specific color for label
                                    fontsize=7,
                                    ha=label_layout[2],
                                    va=label_layout[3])

            set_axis(ax)

        if max_rows > 1:
            fig.tight_layout()
        return fig
    else:
        raise Exception("Exception occurred: Figure initialization failed.")