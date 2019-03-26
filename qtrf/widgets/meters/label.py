from qtrf.widgets.meters       import prefix_map, units
from qtrf.widgets.value.label  import ValueLabel

class MetersLabel(ValueLabel):
    def __init__(self, parent=None):
        ValueLabel.__init__(self, parent)
        self.prefix_map = prefix_map
        self.units      = units
