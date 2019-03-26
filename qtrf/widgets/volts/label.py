from qtrf.widgets.value.label import ValueLabel
from qtrf.widgets.volts       import prefix_map, units

class VoltsLabel(ValueLabel):
    def __init__(self, parent=None):
        ValueLabel.__init__(self, parent)
        self.prefix_map = prefix_map
        self.units      = units
