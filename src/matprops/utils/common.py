import json
from matpropsbase.utils import common as utils

def infer_and_validate_kwargs(kwargs):
    method = utils.get_function_stack()
    with open("rules.json", 'r') as file:
        data = json.load(file)
        if method in data:
            for arg in kwargs.keys():
                if arg not in data[method]:
                    raise ValueError("Unexpected argument found, refer documentation for the list of valid arguments")