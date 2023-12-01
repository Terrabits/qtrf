from .helpers                       import prefix_map, units
from qtrf.widgets.float_value.label import FloatValueLabel


class AmpsLabel(FloatValueLabel):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.prefix_keys = prefix_map
        self.units       = units
