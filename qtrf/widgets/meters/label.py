from .helpers                        import prefix_map, units
from qtrf.widgets.float_value.label  import FloatValueLabel


class MetersLabel(FloatValueLabel):

    def __init__(self, parent):
        super().__init__(parent)
        self.prefix_keys = prefix_map
        self.units      = units
