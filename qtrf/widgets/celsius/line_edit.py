from qtrf.widgets.float_value.line_edit import FloatValueLineEdit


class CelsiusLineEdit(FloatValueLineEdit):
    def __init__(self, parent=None):
        FloatValueLineEdit.__init__(self, parent)
        self.decimal_places = 1
        self.prefix_keys     = None
        self.units          = '°C'
        self.update_validator()
