import matplotlib
from matplotlib.colors import ListedColormap
from itertools import cycle, islice
import matplotlib.cm as cm
import numpy as np

class ColorConfig:
    def __init__(self, cmap=None, n=None):
        self.default = ['red', 'green', 'blue']
        self.n = n
        self.cmap = self._set_cmap(cmap)
        self._colors = self._generate_colors()

    def _set_cmap(self, cmap):
        if cmap is None:
            return ListedColormap(self.default)
        elif isinstance(cmap, list):
            return ListedColormap(cmap)
        else:
            raise TypeError("cmap must be None to set default, or a list of colors.")

    def _generate_colors(self):
        if self.n is None:
            if hasattr(self.cmap, 'colors'):
                return list(self.cmap.colors)
            else:
                raise ValueError("`n` must be specified when using a continuous colormap.")

        return list(islice(cycle(self.cmap.colors), self.n))


    def get_cmap(self):
        return ListedColormap(self._colors)

    def __iter__(self):
        self._iter_index = 0
        return self

    def __next__(self):
        if self.n is None:
            raise ValueError("Cannot iterate when `n` is not set.")
        if self._iter_index >= self.n:
            raise StopIteration
        color = self._colors[self._iter_index]
        self._iter_index += 1
        return color
