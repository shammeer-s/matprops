from matBase.configs.props import PropConfig
from matprops.utils.common import infer_and_validate_kwargs
from matBase.data.MatData import MatData

def AreaProp(data, props=8, width=18, **kwargs):
    defaults = {
        'bgcolor': '#707070',
        'prop_label': 'default2',
        'param3': 'default3'
    }

    # validate allowed keyword arguments
    infer_and_validate_kwargs(**kwargs)

    # Build MatData object and infer data
    db = MatData(data, **kwargs)

    # Initialize prop configuration
    prop = PropConfig(db, props)
    fig = prop.get_propFigure(width)

    for index, row in enumerate(zip(list(zip(*db.data)), db.prop_titles, db.prop_descriptions)):
        d_list, title, description = row
        ax = fig.add_subplot(prop.prop_rows, props, index + 1)

        ax.axvspan(0, 1, ymax=1, fc=bgcolor, alpha=0.1)
