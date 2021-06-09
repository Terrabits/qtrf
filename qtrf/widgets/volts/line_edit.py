from qtrf.widgets.float_value.line_edit import FloatValueLineEdit
from qtrf.widgets.volts           import prefix_map, units

class VoltsLineEdit(FloatValueLineEdit):
    def __init__(self, parent=None):
        FloatValueLineEdit.__init__(self, parent)
        self.prefix_keys = prefix_map
        self.units      = units
        self.update_validator()
