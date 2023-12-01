from qtrf.widgets.float_value.line_edit import FloatValueLineEdit


class CelsiusLineEdit(FloatValueLineEdit):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.prefix_keys    = {}
        self.units          = '°C'
        self.decimal_places = 1
        self.update_validator()
