from matprops.layouts import CLayouts
import math
import warnings

layout = CLayouts()
class PropConfig:
    def __init__(self, dataset=None, title=False, title_loc="tl", labels=False,
                 label_loc="inc", label_col=None, description=False):
        self.title_loc = title_loc
        self.title = title

        self.labels = labels
        self.label_loc = label_loc
        self.label_col = label_col

        self.description = description
        self.description_len = self.description_len_calculator(dataset)

        self.title_layout = None
        self.description_layout = None
        self.label_layout = {}

        self.set_title_layout()
        self.set_description_layout()

    def set_title_layout(self):

        if self.description is None and self.title is not None:
            self.title_layout = [layout.title_locations[self.title_loc][0],
                                 layout.title_locations[self.title_loc][1],
                                 layout.title_locations[self.title_loc][2]]
        elif self.title is not None:
            if self.title_loc == "tl" or self.title_loc == "tr":
                if self.title_loc == "tl":
                    self.title_layout = [layout.title_locations[self.title_loc][0],
                                         layout.title_locations[self.title_loc][
                                             1] + self.description_len / 10, "left"]
                elif self.title_loc == "tr":
                    self.title_layout = [layout.title_locations[self.title_loc][0],
                                         layout.title_locations[self.title_loc][
                                             1] + self.description_len / 10, "right"]
            else:
                self.title_layout = [layout.title_locations[self.title_loc][0],
                                     layout.title_locations[self.title_loc][1],
                                     layout.title_locations[self.title_loc][2]]
        else:
            warnings.warn("Provide title column to get a better chart")

    def set_description_layout(self):
        if self.description is not None:
            if self.title_loc == "tl":
                self.description_layout = [layout.title_locations[self.title_loc][0],
                                           layout.title_locations[self.title_loc][
                                               1] + self.description_len / 10 - 0.1,
                                           "left"]
            elif self.title_loc == "tr":
                self.description_layout = [layout.title_locations[self.title_loc][0],
                                           layout.title_locations[self.title_loc][
                                               1] + self.description_len / 10 - 0.1,
                                           "right"]
            elif self.title_loc == "bl":
                self.description_layout = [layout.title_locations[self.title_loc][0],
                                           layout.title_locations[self.title_loc][
                                               1] - 0.1, "left"]
            elif self.title_loc == "br":  # Original had "bl" twice, corrected to "br"
                self.description_layout = [layout.title_locations[self.title_loc][0],
                                           layout.title_locations[self.title_loc][
                                               1] - 0.1, "right"]

    def description_len_calculator(self, dataset):
        if self.description is not None:
            max_char_per_row = 15
            max_row = 0
            for inner_index, inner_row in dataset.iterrows():
                if len(inner_row[self.description]) > max_char_per_row:
                    row_len = math.ceil(
                        len(inner_row[self.description]) / max_char_per_row)
                    if row_len > max_row:
                        max_row = row_len
                else:
                    max_row = 1
            return max_row
        return 0

    def get_label_layout(self, row, col_name):
        if self.labels is not None and self.label_col is not None:
            # The original code iterated through self.label_col, but get_label_layout
            # is called for a specific column value. Adjusted to use col_name.
            if col_name in self.label_col:  # Check if the current column is meant to have a label
                value = row[col_name]  # Get the specific value for the current column
                if self.label_loc == "inc":
                    self.label_layout[col_name] = [value / 2, value / 2, "center",
                                                   "center"]
                if self.label_loc == "inbl":
                    self.label_layout[col_name] = [0, 0, "left", "bottom"]
                if self.label_loc == "inbr":
                    self.label_layout[col_name] = [value, 0, "right", "bottom"]
                if self.label_loc == "intl":
                    self.label_layout[col_name] = [0 + 0.02, value - 0.02, "left",
                                                   "top"]
                if self.label_loc == "intr":
                    self.label_layout[col_name] = [value - 0.02, value - 0.02, "right",
                                                   "top"]
                if self.label_loc == "outc":
                    self.label_layout[col_name] = [value / 2, value + 0.05, "center",
                                                   "bottom"]  # Adjusted for clarity
                if self.label_loc == "outtl":
                    self.label_layout[col_name] = [0, value + 0.05, "left",
                                                   "bottom"]  # Adjusted
                if self.label_loc == "outtr":
                    self.label_layout[col_name] = [value, value + 0.05, "right",
                                                   "bottom"]  # Adjusted
            return self.label_layout.get(
                col_name)  # Return the layout for the specific column
        return None  # Return None if labels are not enabled or col_name is not in label_col

