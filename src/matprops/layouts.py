class CLayouts:
    def __init__(self):
        self.title_locations = {
            "tl": (0, 1.1, "left"),
            "tr": (1, 1.1, "right"),
            "bl": (0, -0.1, "left"),
            "br": (1, -0.1, "right"),
        }

    def set_title_location(self, title_locations):
        title_configs = {"tl", "tr", "bl", "br"}
        try:
            if isinstance(title_locations, dict):
                unexpected_keys = set(title_locations.keys()) - title_configs
                if unexpected_keys:
                    print("The title_locations contains unexpected keys:",
                          unexpected_keys)
                else:
                    self.title_locations.update(title_locations)
            else:
                print("The variable is not a dictionary.")
        except:
            print("Unexpected error occurred")