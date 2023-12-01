from qtrf.widgets.float_value.label import FloatValueLabel
from qtrf.widgets.volts       import prefix_map, units

class VoltsLabel(FloatValueLabel):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.prefix_keys = prefix_map
        self.units      = units
