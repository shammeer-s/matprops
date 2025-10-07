import numpy as np
import pytest
import pandas as pd

from matprops.props import StackProp

KWARGS = [
    {
        "data" : pd.DataFrame({
            'Country': ['France', 'Germany', 'UAE', 'India', 'Japan'],
            'Men': [0.6, 0.8, 0.3, 0.6, 0.4],
            'Women': [0.4, 0.2, 0.7, 0.3, 0.2],
        }),
        "col": ["Men", "Women"],
        "title": "Country",
    },
    {
        "data" : {
            'Country': ['France', 'Germany', 'UAE', 'India', 'Japan'],
            'Men': [0.6, 0.8, 0.3, 0.6, 0.4],
            'Women': [0.4, 0.2, 0.7, 0.3, 0.2],
        },
        "col": ["Men", "Women"],
        "title": "Country",
    },
    {
        "data" : np.array([
            [0.6, 0.8, 0.3, 0.6, 0.4],
            [0.4, 0.2, 0.7, 0.3, 0.2]
        ]),
        "title": ['France', 'Germany', 'UAE', 'India', 'Japan'],
    },
]

@pytest.mark.parametrize("kwargs", KWARGS)
def test_area_prop(kwargs):
    fig = StackProp(**kwargs)
    fig.show()
    assert fig is not None
