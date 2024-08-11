from matpropsbase import utils
from .common import infer_and_validate_kwargs

class ArgMap:
    def __init__(self, kwargs):
        # Validate permitted arguments
        # infer_and_validate_kwargs(kwargs)
        self.kwargs = kwargs
        caller = utils.get_function_stack()
        method = getattr(self, caller)
        method()

    def AreaProp(self):
        self.kwargs = {
            **{
                "width" : 18,
                "props" : 8,
                "labels" : True,
                "label_loc" : "inc",
                "title" : None,
                "title_loc" : "tl",
                "facecolor" : "#707070",
                "description" : None
            }, **self.kwargs
        }