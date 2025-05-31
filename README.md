# Matprops
**matprops** is a Python library for visualizing proportional data. It is build above matplotlib (the visualization library). Understanding proportional data is quite easy but when it comes to bigger picture we lack of seeing everything 

## Installation
Binary installers for the latest released version are available at the [Python
Package Index (PyPI)](https://pypi.org/project/matprops/)

```sh
# PyPI
pip install matprops
```

The source code is currently hosted on [GitHub](https://github.com/sharajmohamars/matprops.git)


## Area proportional chart
Area proportional charts also known as square area proportional charts is a very easy and basic proportional chart to know first in list. matprops provide a lage amount of customization in creating square area proportional charts

```python
# Pandas - DataFrame Support
import pandas as pd

# Matprops
from matprops import props
```

props is a subclass doing its work for simple proportional charts 

```python
# Creating a dataframe with the help of pandas
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
```

Reducing the limits is mandatory as the matprops is all about proportional charts we need to get the value down to 0 -> 1 range. Ignoring the limits may cause unexpected warnings and errors

Simple square area proportional charts are capable of showing some insights through this data
```python
fig = props.AreaProp(dataset, "Men (%)", labels=True, title="Country", description="Capital")
fig.show()
```

![Output](https://github.com/shammeer-s/matprops/blob/master/output.png?raw=true)

Try customizing the graph with everything possible

**matprops** provides fast and reliable data visualizations for proportional data. matprops currently work only for labelled data for which it is found to be more helpful in defining proportions. matprops aims to move more than proportional charts in upcoming versions. We have enough proportional chart libraries around the Python community, but the thing that differs matprops is its creativity and customization. Some rare visualizations are about to be worked on matprops soon

