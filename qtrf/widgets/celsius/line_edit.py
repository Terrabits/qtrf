from qtrf.widgets.float_value.line_edit import FloatValueLineEdit


class CelsiusLineEdit(FloatValueLineEdit):
    def __init__(self, parent=None):
        FloatValueLineEdit.__init__(self, parent)
        self.prefix_keys    = {}
        self.units          = '°C'
        self.decimal_places = 1
        self.update_validator()
