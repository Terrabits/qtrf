from qtrf.widgets.float_value.line_edit import FloatValueLineEdit


class dBLineEdit(FloatValueLineEdit):
    def __init__(self, parent=None):
        FloatValueLineEdit.__init__(self, parent)
        self.prefix_keys = {}
        self.units       = 'dB'
        self.update_validator()
