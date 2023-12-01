from .helpers                           import prefix_map, units
from qtrf.widgets.float_value.line_edit import FloatValueLineEdit


class AmpsLineEdit(FloatValueLineEdit):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.prefix_keys = prefix_map
        self.units       = units
        self.update_validator()
