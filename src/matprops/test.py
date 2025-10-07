# Pandas - DataFrame Support
import pandas as pd

# Matprops
from matprops import props

# Creating a dataframe with the help of pandas
dataset = pd.DataFrame(
    {
        'Country': ['France', 'Germany', 'United Arab Emirates'],
        'Men': [50, 60, 50],
        'Women': [30, 20, 25],
        'Trans': [20, 20, 25],
        'Capital': ['Paris', 'Berlin', 'Mecca']
    }
)


dataset["Men"] = dataset["Men"]/100
dataset["Women"] = dataset["Women"]/100
dataset["Trans"] = dataset["Trans"]/100

fig = props.BiProp(dataset, ["Men", "Women"], title="Country")
fig.show()