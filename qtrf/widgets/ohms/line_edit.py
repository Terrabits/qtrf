from .helpers                           import prefix_map, units
from qtrf.widgets.float_value.line_edit import FloatValueLineEdit


class OhmsLineEdit(FloatValueLineEdit):
    def __init__(self, parent=None):
        FloatValueLineEdit.__init__(self, parent)
        self.prefix_keys       = prefix_map
        self.include_negative = False
        self.units            = units
        self.update_validator()
