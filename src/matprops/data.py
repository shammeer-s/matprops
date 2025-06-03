import numpy as np
import pandas as pd

class construct:
    def __init__(self, data, col=None, title=None):
        self.dtype = self._detect_type(data)
        self.titles, self.data = self._transformer(data, col, title)

    def _detect_type(self, data):
        if isinstance(data, np.ndarray):
            return 'numpy'
        elif isinstance(data, pd.DataFrame):
            return 'pandas'
        elif isinstance(data, dict):
            return 'dict'
        else:
            raise TypeError("Data must be a numpy.ndarray, pandas.DataFrame, or dict.")

    def _process_titles(self, titles):
        if titles is None or isinstance(titles, str):
            return None
        elif isinstance(titles, np.ndarray):
            return titles.tolist()
        elif isinstance(titles, list):
            return titles
        raise TypeError("Invalid type for titles.")

    def _numpy_transformer(self, data, titles):
        arr = np.array(data)
        if titles is not None and isinstance(titles, str):
            raise ValueError("For numpy data sequence, titles as string is not allowed")
        return self._process_titles(titles), arr

    def _pandas_transformer(self, data, col, titles):
        arr = data[col if col is not None else 0].values
        if isinstance(titles, str):
            titles = data[titles].values.tolist()
        ptitles = self._process_titles(titles)
        return ptitles if ptitles is not None else titles, arr

    def _dict_transformer(self, data, col, titles):
        arr = np.array(data[col if col is not None else 0])
        if isinstance(titles, str):
            titles = data[titles]
        ptitles = self._process_titles(titles)
        return ptitles if ptitles is not None else titles, arr

    def _transformer(self, data, col, titles):
        if self.dtype == 'numpy':
            return self._numpy_transformer(data, titles)
        elif self.dtype == 'pandas':
            return self._pandas_transformer(data, col, titles)
        elif self.dtype == 'dict':
            return self._dict_transformer(data, col, titles)
        else:
            raise TypeError("Unsupported data type for transformation.")

    def get_data(self):
        return self.data