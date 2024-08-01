import matplotlib
import matplotlib.pyplot as plt

from matBase.configs.props import *
from matBase.utils.props import *
from matBase.utils.figure import *


def AreaProp(dataset, col_name, cols=8, labels=True, label_loc="inc", title=None, title_loc="tl", bgcolor="#707070",
             description=None):
    """
    Square area proportional chart
    This function is used to create and customize almost everything in basic square area proportional chart
    Supports only for the percentages(proportions)
    The values of the columns should be between 0 and 1, which is considered as normal percentile.

    :parameter dataset: (pandas d ataframe)
                    May hold a larger number of columns
                    including title, description and proportions
    :parameter col_name: (str)
                Column name for which the proportions to be visualized
    :param cols: (int, default=8)
                 Number of proportion square columns for a single row
    :param labels: (bool, default=True)
                   Bool value denoting the labels visibility
                   True: Visible
                   False: Invisible
    :param label_loc: (str, default="inc" - inner center)
                      String deciding the location of labels in individual props

                      Valid locations,
                      "inc" - inner center
                      "inbl" - inner bottom left
                      "inbr" - inner bottom right
                      "intl" - inner top left
                      "intr" - inner top right
                      "outc" - outer center
                      "outtl" - outer top left
                      "outtr" - outer top right
    :param labelcolor: (str, default="white")
                        Color of the label
                        All hex values, and default color code in matplotlib are supported
    :param title: (str, default=None)
                  Column name of the dataset denoting the title of each prop
                  Each row should be associated with the proportions directly
    :param title_loc: (str, default="tl")
                      String deciding the location of labels in individual props

                      Valid locations,
                      "tl" - top left
                      "tr" - top right
    :param facecolor: (str, default="black")
                      Color of the square prop
                      All hex values, and default color code in matplotlib are supported
    :param bgcolor: (str, default="black")
                    Background color of the props
                    All hex values, and default color code in matplotlib are supported
    :param description: (str, default=None)
                        Column name of the dataset denoting the description of each prop
                        Each row should be associated with the proportions directly
    :return: A square area proportional chart
    """

    # Proportional chart initialize
    prop = PropInit(dataset, cols)
    fig = prop.initialize_figure()

    if isinstance(col_name, str):
        col_name = [col_name]

    if fig:
        # Proportional chart configurations
        pConfig = PropConfig(dataset, title, title_loc, labels, label_loc, col_name, description)

        for index, row in dataset.iterrows():
            ax = fig.add_subplot(prop.max_rows, cols, index + 1)

            ax.axvspan(0, 1, ymax=1, fc=bgcolor, alpha=0.1)

            if pConfig.title is not None:
                ax.text(pConfig.title_layout[0],
                        pConfig.title_layout[1],
                        row[title],
                        fontweight="bold",
                        ha=pConfig.title_layout[2],
                        c="#000")

            if pConfig.description is not None:
                max_char_per_row = 15
                temp_description_layout = pConfig.description_layout
                out_desc_list = [(row[description][i:i + max_char_per_row]) for i in
                                 range(0, len(row[description]), max_char_per_row)]
                for i in out_desc_list:
                    ax.text(temp_description_layout[0],
                            temp_description_layout[1],
                            i,
                            fontweight="normal",
                            ha=pConfig.description_layout[2],
                            c="#000")
                    temp_description_layout = [temp_description_layout[0],
                                               temp_description_layout[1] - 0.1,
                                               temp_description_layout[2]]

            if isinstance(col_name, list):
                if len(col_name) > 3:
                    warnings.warn("Warning: Using more than three columns for proportional charts is not recommended "
                                  "due to potential overcrowding. To ensure clarity and readability, we will only "
                                  "display three columns. If you require specific columns, please update the "
                                  "'col_name' attribute with three specific column names.")
                for col, colour in zip(col_name, ["blue", "green", "red"]):
                    ax.axvspan(0, row[col], ymin=0.01, ymax=row[col], fc=matplotlib.colors.to_hex(colour) + "4D",
                               ec=colour)
                    if pConfig.labels:
                        pConfig.get_label_layout(row)
                        ax.text(pConfig.label_layout[col][0],
                                pConfig.label_layout[col][1],
                                str(row[col] * 100) + "%",
                                c=matplotlib.colors.to_hex(colour),
                                fontsize=7,
                                ha=pConfig.label_layout[col][2],
                                va=pConfig.label_layout[col][3])

            set_axis(ax)

        if prop.max_rows > 1:
            fig.tight_layout()
        plt.show();
    else:
        raise Exception("Exception occurred")


def GridProp(dataset, col_name, cols=8, labels=True, label_loc="inc", title=None, title_loc="tl", bgcolor="#707070",
             description=None):
    num_squares = 10

    square_size = 0.1
    space_size = 0.03

    # Proportional chart initialize
    prop = PropInit(dataset, cols)
    fig = prop.initialize_figure()

    if isinstance(col_name, str):
        col_name = [col_name]

    c_dict = dict(zip(col_name, ["blue", "green", "red"]))

    if fig:
        # Proportional chart configurations
        pConfig = PropConfig(dataset, title, title_loc, labels, label_loc, col_name, description)

        for index, row in dataset.iterrows():
            ax = fig.add_subplot(prop.max_rows, cols, index + 1)

            row_vals = row[col_name].sort_values().index
            iter_tot = 0
            for i in range(len(row_vals)):
                row[row_vals[i]] = row[row_vals[i]] - iter_tot
                iter_tot += row[row_vals[i]]
            # print(row)

            if pConfig.title is not None:
                ax.text(pConfig.title_layout[0],
                        pConfig.title_layout[1]+0.2,
                        row[title],
                        fontweight="bold",
                        ha=pConfig.title_layout[2],
                        c="#000")

            if pConfig.description is not None:
                max_char_per_row = 15
                temp_description_layout = pConfig.description_layout
                out_desc_list = [(row[description][i:i + max_char_per_row]) for i in
                                 range(0, len(row[description]), max_char_per_row)]
                for i in out_desc_list:
                    ax.text(temp_description_layout[0],
                            temp_description_layout[1]+0.2,
                            i,
                            fontweight="normal",
                            ha=pConfig.description_layout[2],
                            c="#000")
                    temp_description_layout = [temp_description_layout[0],
                                               temp_description_layout[1] - 0.1,
                                               temp_description_layout[2]]

            if isinstance(col_name, list):
                if len(col_name) > 3:
                    warnings.warn("Warning: Using more than three columns for proportional charts is not recommended "
                                  "due to potential overcrowding. To ensure clarity and readability, we will only "
                                  "display three columns. If you require specific columns, please update the "
                                  "'col_name' attribute with three specific column names.")

                counter = 0
                iterator = 0
                iterator_flag = True

                # Plot each square in the grid
                for i in range(num_squares):
                    for j in range(num_squares):
                        counter += 1
                        # Calculate the coordinates of the square's corners
                        x1 = j * (square_size + space_size)
                        y1 = i * (square_size + space_size)

                        if iterator_flag:
                            col = row_vals[iterator]
                            print("row_val: ", col, len(col_name))
                            row[col] -= 0.01
                            if row[col] <= 0:
                                print("change")
                                iterator += 1
                                if iterator == len(col_name):
                                    iterator_flag = False

                        if iterator_flag:
                            # Plot the square
                            square = plt.Rectangle((x1, y1), square_size, square_size, linewidth=1, edgecolor=c_dict[col],
                                                   facecolor=matplotlib.colors.to_hex(c_dict[col]) + "4D")
                        else:
                            # Plot the square
                            square = plt.Rectangle((x1, y1), square_size, square_size, linewidth=1,
                                                   edgecolor=matplotlib.colors.to_hex('black') + "4D",
                                                   facecolor='white')
                        ax.add_patch(square)

            set_axis(ax, 0, num_squares * (square_size + space_size))
            set_fig(ax)
        if prop.max_rows > 1:
            fig.tight_layout()
        plt.show();
    else:
        raise Exception("Exception occurred")


def BiProp(dataset, col_name, cols=4, labels=True, label_loc="inc", title=None, title_loc="tl", bgcolor="#707070",
             description=None):
    # Proportional chart initialize
    prop = PropInit(dataset, cols)
    fig = prop.initialize_figure()

    if isinstance(col_name, str):
        col_name = [col_name]

    c_dict = dict(zip(col_name, ["blue", "orange"]))

    if fig:
        # Proportional chart configurations
        pConfig = PropConfig(dataset, title, title_loc, labels, label_loc, col_name, description)

        for index, row in dataset.iterrows():
            ax = fig.add_subplot(prop.max_rows, cols, index + 1)

            row_vals = row[col_name].sort_values().index
            iter_tot = 0
            for i in range(len(row_vals)):
                row[row_vals[i]] = row[row_vals[i]] - iter_tot
                iter_tot += row[row_vals[i]]
            # print(row)

            if pConfig.title is not None:
                ax.text(pConfig.title_layout[0],
                        pConfig.title_layout[1] + 0.2,
                        row[title],
                        fontweight="bold",
                        ha=pConfig.title_layout[2],
                        c="#000")

            if pConfig.description is not None:
                max_char_per_row = 15
                temp_description_layout = pConfig.description_layout
                out_desc_list = [(row[description][i:i + max_char_per_row]) for i in
                                 range(0, len(row[description]), max_char_per_row)]
                for i in out_desc_list:
                    ax.text(temp_description_layout[0],
                            temp_description_layout[1] + 0.2,
                            i,
                            fontweight="normal",
                            ha=pConfig.description_layout[2],
                            c="#000")
                    temp_description_layout = [temp_description_layout[0],
                                               temp_description_layout[1] - 0.1,
                                               temp_description_layout[2]]

            if isinstance(col_name, list):
                if len(col_name) > 3:
                    warnings.warn("Warning: Using more than three columns for proportional charts is not recommended "
                                  "due to potential overcrowding. To ensure clarity and readability, we will only "
                                  "display three columns. If you require specific columns, please update the "
                                  "'col_name' attribute with three specific column names.")

                counter = 0
                iterator = 0
                iterator_flag = True

                # Plot each square in the grid
                for i in range(num_squares):
                    for j in range(num_squares):
                        counter += 1
                        # Calculate the coordinates of the square's corners
                        x1 = j * (square_size + space_size)
                        y1 = i * (square_size + space_size)

                        if iterator_flag:
                            col = row_vals[iterator]
                            print("row_val: ", col, len(col_name))
                            row[col] -= 0.01
                            if row[col] <= 0:
                                print("change")
                                iterator += 1
                                if iterator == len(col_name):
                                    iterator_flag = False

                        if iterator_flag:
                            # Plot the square
                            square = plt.Rectangle((x1, y1), square_size, square_size, linewidth=1,
                                                   edgecolor=c_dict[col],
                                                   facecolor=matplotlib.colors.to_hex(c_dict[col]) + "4D")
                        else:
                            # Plot the square
                            square = plt.Rectangle((x1, y1), square_size, square_size, linewidth=1,
                                                   edgecolor=matplotlib.colors.to_hex('black') + "4D",
                                                   facecolor='white')
                        ax.add_patch(square)

            set_axis(ax, 0, num_squares * (square_size + space_size))
            set_fig(ax)
        if prop.max_rows > 1:
            fig.tight_layout()
        plt.show();
    else:
        raise Exception("Exception occurred")

