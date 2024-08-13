from matpropsbase import utils

class ArgMap:
    def __init__(self, kwargs):
        # Validate permitted arguments
        # infer_and_validate_kwargs(kwargs)
        self.kwargs = kwargs
        self.dataParams = None
        self.colorParams = None
        self.layoutParams = None
        caller = utils.get_function_stack()
        caller_method = getattr(self, caller)
        caller_method()
        self.update_kwargs()

    def update_kwargs(self):
        for key in self.kwargs.keys():
            if key in self.colorParams.keys():
                self.colorParams[key] = self.kwargs[key]
            elif key in self.dataParams.keys():
                self.dataParams[key] = self.kwargs[key]
            elif key in self.layoutParams.keys():
                self.layoutParams[key] = self.kwargs[key]
            else:
                raise ValueError("Invalid parameters has been passed for the method")

    def AreaProp(self):
        self.colorParams = {
            "facecolor": "#707070"
        }
        self.dataParams = {
            "labels": True,
            "title": None,
            "description": None,
        }
        self.layoutParams = {
            "width": 18,
            "props": 8,
        }

