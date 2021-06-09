from .helpers                           import prefix_map, units
from qtrf.widgets.float_value.line_edit import FloatValueLineEdit


class SecondsLineEdit(FloatValueLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.prefix_keys      = prefix_map
        self.units            = units
        self.include_negative = False
        self.update_validator()
