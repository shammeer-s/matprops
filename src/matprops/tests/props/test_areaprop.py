import numpy as np
import pytest
import pandas as pd

from matprops.props import AreaProp

KWARGS = [
    {
        "data" : pd.DataFrame({
            'Country': ['France', 'Germany', 'UAE', 'France', 'Germany'],
            'Men': [0.6, 0.8, 0.3, 0.6, 0.8],
        }),
        "col": "Men",
        "title": "Country",
    },
    {
        "data" : {
            'Country': ['France', 'Germany', 'UAE', 'France', 'Germany'],
            'Men': [0.6, 0.8, 0.3, 0.6, 0.8],
        },
        "col": "Men",
        "title": "Country",
    },
    {
        "data" : np.array([0.6, 0.8, 0.3, 0.6, 0.8]),
        "title": ['France', 'Germany', 'UAE', 'France', 'Germany'],
    },
]

@pytest.mark.parametrize("kwargs", KWARGS)
def test_area_prop(kwargs):
    fig = AreaProp(**kwargs)
    fig.show()
    # Check if the figure are created
    assert fig is not None
