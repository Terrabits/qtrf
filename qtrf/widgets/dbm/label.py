from qtrf.widgets.float_value.label import FloatValueLabel


class dBmLabel(FloatValueLabel):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.prefix_keys = {}
        self.units       = 'dBm'
