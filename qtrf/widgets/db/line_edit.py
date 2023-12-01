from qtrf.widgets.float_value.line_edit import FloatValueLineEdit


class dBLineEdit(FloatValueLineEdit):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.prefix_keys = {}
        self.units       = 'dB'
        self.update_validator()
