import numpy as np
import pandas as pd

ptype_map = {
    'area': {
        "function": 'AreaProp',
        "min_ndim": 1,
        "max_ndim": 1
    },
    'split': {
        "function": 'SplitProp',
        "min_ndim": 2,
        "max_ndim": 3
    },
    'stack': {
        "function": 'StackProp',
        "min_ndim": 2,
        "max_ndim": 3
    },
    'bi': {
        "function": 'BiProp',
        "min_ndim": 2,
        "max_ndim": 2
    },
}


class DataConstruct:
    def __init__(self, data, col=None, title=None, ptype=None):
        self.dtype = self._detect_type(data)
        self.dlen = None
        self.ptype = ptype
        self.ndim = 0
        self.titles, self.data = self._transformer(data, col, title)
        self._iterator_index = 0

        self.validate()

    def validate(self):
        if self.ptype not in ptype_map:
            raise ValueError(f"Invalid ptype: {self.ptype}. Supported types are: {list(ptype_map.keys())}")

        ptype_info = ptype_map[self.ptype]
        if self.ndim < ptype_info['min_ndim'] or self.ndim > ptype_info['max_ndim']:
            raise ValueError(
                f"Data with ndim={self.ndim} is not supported for ptype '{self.ptype}'. "
                f"Expected between {ptype_info['min_ndim']} and {ptype_info['max_ndim']} dimensions."
            )

    def _detect_type(self, data):
        type_map = {
            np.ndarray: 'numpy',
            pd.DataFrame: 'pandas',
            dict: 'dict'
        }
        for t, name in type_map.items():
            if isinstance(data, t):
                return name
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
        arr = np.asarray(data)
        self.ndim = arr.shape[1]
        self.dlen = arr.shape[0]

        if isinstance(titles, str):
            raise ValueError("For numpy data, titles as string is not allowed")

        return self._process_titles(titles), arr

    def _pandas_transformer(self, data, col, titles):
        if col is None:
            arr = data.values
        elif isinstance(col, list):
            arr = data[col].values
        else:
            arr = data[[col]].values  # force 2D if single col

        if isinstance(titles, str):
            titles = data[titles].tolist()

        self.ndim = arr.shape[1]
        self.dlen = arr.shape[0]
        return self._process_titles(titles), arr

    def _dict_transformer(self, data, col, titles):
        if col is None:
            arr = np.array(list(data.values())).T  # assume uniform-length values
        elif isinstance(col, list):
            arr = np.array([data[k] for k in col]).T
        else:
            arr = np.array(data[col])

            if arr.ndim == 1:
                arr = arr[:, None]  # reshape to (n,1)

        if isinstance(titles, str):
            titles = data[titles]

        self.ndim = arr.shape[1]
        self.dlen = arr.shape[0]
        return self._process_titles(titles), arr

    def _transformer(self, data, col, titles):
        if self.dtype == 'numpy':
            return self._numpy_transformer(data, titles)
        elif self.dtype == 'pandas':
            return self._pandas_transformer(data, col, titles)
        elif self.dtype == 'dict':
            return self._dict_transformer(data, col, titles)
        else:
            raise TypeError("Unsupported data type for transformation.")

    def __iter__(self):
        self._iterator_index = 0
        return self

    def __next__(self):
        if self._iterator_index >= self.dlen:
            raise StopIteration
        title = (
            self.titles[self._iterator_index]
            if self.titles and self._iterator_index < len(self.titles)
            else None
        )
        data_slice = self.data[self._iterator_index]
        self._iterator_index += 1
        return title, data_slice

    def __len__(self):
        return self.dlen if self.dlen is not None else 0

    def get_data(self):
        return self.data
