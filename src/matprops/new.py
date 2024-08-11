from utils.args import ArgMap
from matpropsbase import data
import pandas as pd
def AreaProp(db, **kwargs):
    kwargs = ArgMap(kwargs)

    # Build MatData object and infer data
    db = data.Builder(db, kwargs)

    print("Data : ", db.data)
    print("prop title : ", db.prop_titles)
    print("prop description : ", db.prop_descriptions)

dataset = pd.DataFrame(
    {
        'Country': ['France', 'Germany', 'United Arab Emirates'],
        'Men (%)': [60, 80, 30],
        'Capital': ['Paris', 'Berlin', 'Mecca']
    }
)

# Changing the limits
# Limit : 0 -> 1
dataset["Men (%)"] = dataset["Men (%)"]/100
AreaProp(dataset)